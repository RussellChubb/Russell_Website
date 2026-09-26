import sys

# Prevent Python from creating __pycache__
sys.dont_write_bytecode = True

from manim import *


# =============================================================================
# DRACULA PALETTE
# =============================================================================

BACKGROUND = "#282A36"
TERMINAL_BG = "#1E1F29"
TITLE_BAR = "#21222C"
BORDER = "#44475A"
FOREGROUND = "#F8F8F2"
COMMENT = "#6272A4"
PURPLE = "#BD93F9"
GREEN = "#50FA7B"
YELLOW = "#F1FA8C"
RED = "#FF5555"

MONO = "JetBrainsMono Nerd Font"


# =============================================================================
# TIMING
# =============================================================================

TERMINAL_ENTER_TIME = 0.8
ROW_REVEAL_TIME = 0.45
ROW_REVEAL_PAUSE = 0.12


# =============================================================================
# CUSTOMER TABLE
# =============================================================================

HEADERS = [
    "CustomerID",
    "CustomerName",
    "ContactName",
    "Address",
    "City",
    "PostalCode",
    "Country",
]

ROWS = [
    [
        "1",
        "Coastal Surf Co.",
        "Oscar Macdonald",
        "14 Harbour Road",
        "Brighton",
        "BN1 4QF",
        "UK",
    ],
    [
        "2",
        "Alpine Outdoor Gear",
        "Kian Knight",
        "27 Bergstrasse",
        "Munich",
        "80331",
        "Germany",
    ],
    [
        "3",
        "Pacific Wave Supplies",
        "Jock Adams",
        "82 Ocean Avenue",
        "Sydney",
        "NSW 2000",
        "Australia",
    ],
    [
        "4",
        "North Shore Adventures",
        "Liam Barnes",
        "51 Beach Road",
        "Vancouver",
        "V6K 2G2",
        "Canada",
    ],
    [
        "5",
        "Atlantic Surfwear",
        "Jake Faville",
        "9 Seaview Terrace",
        "Cork",
        "T12 X2F5",
        "Ireland",
    ],
]


# =============================================================================
# HELPERS
# =============================================================================

def fit_to_max(mobject, max_width=None, max_height=None):
    """Shrink only if the object exceeds the supplied bounds."""
    scale_factor = 1.0

    if max_width is not None and mobject.width > max_width:
        scale_factor = min(scale_factor, max_width / mobject.width)

    if max_height is not None and mobject.height > max_height:
        scale_factor = min(scale_factor, max_height / mobject.height)

    if scale_factor < 1.0:
        mobject.scale(scale_factor)


# =============================================================================
# TERMINAL WINDOW
# =============================================================================

class TerminalWindow(VGroup):

    def __init__(
        self,
        width=13.4,
        height=7.1,
        **kwargs,
    ):
        super().__init__(**kwargs)

        self.body = RoundedRectangle(
            corner_radius=0.18,
            width=width,
            height=height,
            fill_color=TERMINAL_BG,
            fill_opacity=1,
            stroke_color=BORDER,
            stroke_width=1.2,
        )

        self.title_bar = Rectangle(
            width=width - 0.02,
            height=0.45,
            fill_color=TITLE_BAR,
            fill_opacity=1,
            stroke_width=0,
        )

        self.title_bar.move_to(
            self.body.get_top() + DOWN * 0.225
        )

        self.red = Dot(radius=0.055, color=RED)
        self.yellow = Dot(radius=0.055, color=YELLOW)
        self.green = Dot(radius=0.055, color=GREEN)

        dots = VGroup(
            self.red,
            self.yellow,
            self.green,
        )

        dots.arrange(RIGHT, buff=0.11)

        dots.move_to(
            self.body.get_left()
            + RIGHT * 0.32
            + UP * (height / 2 - 0.225)
        )

        self.title = Text(
            "customers",
            font=MONO,
            font_size=12,
            color=COMMENT,
        )

        self.title.move_to(self.title_bar.get_center())

        self.add(
            self.body,
            self.title_bar,
            self.red,
            self.yellow,
            self.green,
            self.title,
        )


# =============================================================================
# RESULT TABLE
# =============================================================================

class ResultTable(VGroup):
    """
    CLI-style customer table with a bordered grid.

    Columns are left-aligned and sized from the widest value in each column.
    Rows start hidden and can be revealed from top to bottom.
    """

    def __init__(
        self,
        headers,
        rows,
        font_size=16,
        header_font_size=16,
        cell_padding_x=0.30,
        row_height=0.58,
        border_color=BORDER,
        **kwargs,
    ):
        super().__init__(**kwargs)

        self.headers = headers
        self.data = rows
        self.row_height = row_height

        column_count = len(headers)
        row_count = len(rows)

        # ---------------------------------------------------------------------
        # Build text
        # ---------------------------------------------------------------------

        header_cells = [
            Text(
                header,
                font=MONO,
                font_size=header_font_size,
                color=PURPLE,
                weight="BOLD",
            )
            for header in headers
        ]

        body_cells = [
            [
                Text(
                    str(value),
                    font=MONO,
                    font_size=font_size,
                    color=FOREGROUND,
                )
                for value in row
            ]
            for row in rows
        ]

        # ---------------------------------------------------------------------
        # Calculate column widths
        # ---------------------------------------------------------------------

        column_widths = []

        for col in range(column_count):
            widest = header_cells[col].width

            for row in body_cells:
                widest = max(widest, row[col].width)

            column_widths.append(widest + cell_padding_x)

        column_lefts = []
        running = 0.0

        for width in column_widths:
            column_lefts.append(running)
            running += width

        table_width = running
        table_height = row_height * (row_count + 1)

        # ---------------------------------------------------------------------
        # Position cells
        # ---------------------------------------------------------------------

        def place_left(cell, col, row_top):
            cell.move_to(
                RIGHT * (
                    column_lefts[col]
                    + cell.width / 2
                )
                + DOWN * (
                    row_top
                    + row_height / 2
                )
            )

        for col, cell in enumerate(header_cells):
            place_left(cell, col, 0)

        self.header_cells = VGroup(*header_cells)
        self.rows = []

        for row_index, row in enumerate(body_cells):
            row_group = VGroup(*row)

            for col, cell in enumerate(row):
                place_left(
                    cell,
                    col,
                    row_height * (row_index + 1),
                )

            # Rows are initially invisible.
            row_group.set_opacity(0)
            self.rows.append(row_group)

        # ---------------------------------------------------------------------
        # Grid lines
        # ---------------------------------------------------------------------

        self.h_lines = []
        self.v_lines = []

        def h_line(y):
            line = Line(
                ORIGIN,
                RIGHT * table_width,
                color=border_color,
                stroke_width=1,
            )

            line.move_to(
                RIGHT * (table_width / 2)
                + DOWN * y
            )

            self.h_lines.append(line)
            return line

        def v_line(x):
            line = Line(
                ORIGIN,
                DOWN * table_height,
                color=border_color,
                stroke_width=1,
            )

            line.move_to(
                RIGHT * x
                + DOWN * (table_height / 2)
            )

            self.v_lines.append(line)
            return line

        border_lines = VGroup()

        # Top border, header separator, bottom border.
        border_lines.add(h_line(0))
        border_lines.add(h_line(row_height))
        border_lines.add(h_line(table_height))

        # Left edge, internal column rules, right edge.
        border_lines.add(v_line(0))

        for left in column_lefts[1:]:
            border_lines.add(v_line(left))

        border_lines.add(v_line(table_width))

        self.border_lines = border_lines

        self.add(self.header_cells)
        self.add(self.border_lines)

        for row_group in self.rows:
            self.add(row_group)

        self.table_width = table_width
        self.table_height = table_height

    def reveal_row(self, index):
        return self.rows[index].animate.set_opacity(1)


# =============================================================================
# MAIN SCENE
# =============================================================================

class CustomerTable(Scene):

    def construct(self):

        self.camera.background_color = BACKGROUND

        # ---------------------------------------------------------------------
        # Terminal
        # ---------------------------------------------------------------------

        terminal = TerminalWindow()

        terminal.scale(0.96)

        self.play(
            FadeIn(
                terminal,
                shift=UP * 0.10,
            ),
            terminal.animate.scale(1 / 0.96),
            run_time=TERMINAL_ENTER_TIME,
        )

        # ---------------------------------------------------------------------
        # Create table
        # ---------------------------------------------------------------------

        table = ResultTable(
            headers=HEADERS,
            rows=ROWS,
            font_size=16,
            header_font_size=16,
            cell_padding_x=0.30,
            row_height=0.58,
        )

        # The seven-column table is deliberately allowed to use most of the
        # terminal width, while retaining a small margin on either side.
        fit_to_max(
            table,
            max_width=12.35,
            max_height=5.65,
        )

        table.move_to(
            terminal.get_center()
            + DOWN * 0.20
        )

        # ---------------------------------------------------------------------
        # Reveal table
        # ---------------------------------------------------------------------

        self.play(
            Create(table.border_lines),
            FadeIn(table.header_cells),
            run_time=0.6,
        )

        for row_index in range(len(table.rows)):
            self.play(
                table.reveal_row(row_index),
                run_time=ROW_REVEAL_TIME,
            )

            self.wait(ROW_REVEAL_PAUSE)

        # ---------------------------------------------------------------------
        # Leave the completed table on screen.
        # ---------------------------------------------------------------------

        self.wait(2.0)


# =============================================================================
# RENDER
# =============================================================================

# High quality:
# python -B -m manim -pqh customer_table_animation.py CustomerTable
#
# Lower quality preview:
# python -B -m manim -pql customer_table_animation.py CustomerTable
