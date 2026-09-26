"""
SQL GROUP BY / ORDER BY Tutorial Animation
==========================================

Single-scene Manim animation for a SQL tutorial.

The animation progresses through eight SQL examples:

    1. GROUP BY
    2. SUM + GROUP BY
    3. ORDER BY Price
    4. ORDER BY Price DESC
    5. ORDER BY ProductName
    6. Multiple columns
    7. Multiple columns with ASC / DESC
    8. GROUP BY + ORDER BY

Visual style:
    - Dracula colour palette
    - Dark macOS-style terminal
    - JetBrains Mono / Nerd Font
    - Slow, readable animations
    - Minimal transitions
    - Persistent terminal
    - Query -> Result relationship
    - Result tables drawn like a CLI (psql/mysql) table: bordered grid,
      left-aligned columns

No rendering is performed by this file.

Example:

    python -B -m manim -pqh sql_animation.py SQLTutorial

"""

import sys

# Prevent Python from creating __pycache__
sys.dont_write_bytecode = True

import re
from html import escape

from manim import *


# =============================================================================
# DRACULA PALETTE
# =============================================================================

BACKGROUND = "#282A36"
TERMINAL_BG = "#1E1F29"
TITLE_BAR = "#21222C"
BORDER = "#44475A"
DIVIDER = "#44475A"

FOREGROUND = "#F8F8F2"
COMMENT = "#6272A4"

PURPLE = "#BD93F9"
PINK = "#FF79C6"
CYAN = "#8BE9FD"
GREEN = "#50FA7B"
YELLOW = "#F1FA8C"
ORANGE = "#FFB86C"
RED = "#FF5555"

# Main SQL accent.
SQL_ACCENT = PURPLE


# =============================================================================
# TYPOGRAPHY
# =============================================================================

# A Nerd Font patched variant of JetBrains Mono. This must be installed on
# the machine doing the rendering (Pango resolves fonts by family name from
# the system font list) - e.g. install the "JetBrainsMono Nerd Font" family
# from https://www.nerdfonts.com/font-downloads and refresh the font cache.
# If it isn't installed, Pango will silently fall back to a default font
# rather than erroring, so double check the rendered output if glyphs look
# generic.
MONO = "JetBrainsMono Nerd Font"


# =============================================================================
# GLOBAL TIMING
# =============================================================================

# These are intentionally much slower than the previous version.

TERMINAL_ENTER_TIME = 1.0

# Minimum time used for typing a line.
TYPING_MIN_TIME = 0.55

# Approximate time per character.
TYPING_TIME_PER_CHARACTER = 0.035

# Time between SQL lines.
LINE_PAUSE = 0.20

# Pause after completing a query.
QUERY_PAUSE = 1.3

# Time spent transforming the terminal.
SPLIT_TIME = 1.5

# Time used to reveal table rows.
ROW_REVEAL_TIME = 0.45

# Time between table rows.
ROW_REVEAL_PAUSE = 0.18

# How long conceptual highlights remain visible.
HIGHLIGHT_IN_TIME = 0.45
HIGHLIGHT_HOLD_TIME = 0.9
HIGHLIGHT_OUT_TIME = 0.45

# Pause between examples.
EXAMPLE_PAUSE = 1.5


# =============================================================================
# SQL EXAMPLES
# =============================================================================

EXAMPLES = [
    {
        "title": "GROUP BY",
        "query": """SELECT Country, COUNT(CustomerID) AS [Number of Customers]

FROM Customers

GROUP BY Country;""",
        "headers": [
            "Country",
            "Number of Customers",
        ],
        "rows": [
            ["UK", "428"],
            ["Germany", "312"],
            ["Australia", "197"],
            ["Canada", "154"],
            ["Ireland", "83"],
        ],
        "highlights": [
            {
                "code_lines": [4],
                "table_columns": [0],
                "table_rows": [],
            },
        ],
    },
    {
        "title": "SUM + GROUP BY",
        "query": """SELECT CustomerID, SUM(Total) AS [Total Sales]

FROM Sales

GROUP BY CustomerID;""",
        "headers": [
            "CustomerID",
            "Total Sales",
        ],
        "rows": [
            ["1001", "£1,250"],
            ["1002", "£890"],
            ["1003", "£2,430"],
            ["1004", "£675"],
            ["1005", "£1,720"],
        ],
        "highlights": [
            {
                "code_lines": [0],
                "table_columns": [1],
                "table_rows": [],
            },
            {
                "code_lines": [4],
                "table_columns": [0],
                "table_rows": [],
            },
        ],
    },
    {
        "title": "ORDER BY Price",
        "query": """SELECT *

FROM Products

ORDER BY Price;""",
        "headers": [
            "Product",
            "Price",
        ],
        "rows": [
            ["Reef Surf Wax", "24.99"],
            ["Leash 7ft", "34.99"],
            ["3/2mm Wetsuit", "129.99"],
            ["6' Fish Surfboard", "449.99"],
            ["7' Funboard", "599.99"],
        ],
        "highlights": [
            {
                "code_lines": [4],
                "table_columns": [1],
                "table_rows": [0, 1, 2, 3, 4],
            },
        ],
    },
    {
        "title": "ORDER BY Price DESC",
        "query": """SELECT *

FROM Products

ORDER BY Price DESC;""",
        "headers": [
            "Product",
            "Price",
        ],
        "rows": [
            ["7' Funboard", "599.99"],
            ["6' Fish Surfboard", "449.99"],
            ["3/2mm Wetsuit", "129.99"],
            ["Leash 7ft", "34.99"],
            ["Reef Surf Wax", "24.99"],
        ],
        "highlights": [
            {
                "code_lines": [4],
                "table_columns": [1],
                "table_rows": [0, 1, 2, 3, 4],
            },
        ],
    },
    {
        "title": "ORDER BY ProductName",
        "query": """SELECT *

FROM Products

ORDER BY ProductName;""",
        "headers": [
            "Product",
        ],
        "rows": [
            ["3/2mm Wetsuit"],
            ["6' Fish Surfboard"],
            ["7' Funboard"],
            ["Leash 7ft"],
            ["Reef Surf Wax"],
        ],
        "highlights": [
            {
                "code_lines": [4],
                "table_columns": [0],
                "table_rows": [0, 1, 2, 3, 4],
            },
        ],
    },
    {
        "title": "MULTIPLE COLUMNS",
        "query": """SELECT *

FROM Customers

ORDER BY Country, CustomerName;""",
        "headers": [
            "Country",
            "Customer",
        ],
        "rows": [
            ["Australia", "Pacific Wave Supplies"],
            ["Canada", "North Shore Adventures"],
            ["Germany", "Alpine Outdoor Gear"],
            ["Ireland", "Atlantic Surfwear"],
            ["UK", "Coastal Surf Co."],
            ["UK", "Highland Surf Co."],
            ["UK", "Seaside Boards"],
        ],
        "highlights": [
            {
                "code_lines": [4],
                "table_columns": [0],
                "table_rows": [],
            },
            {
                "code_lines": [4],
                "table_columns": [1],
                "table_rows": [4, 5, 6],
            },
        ],
    },
    {
        "title": "ASC + DESC",
        "query": """SELECT *

FROM Customers

ORDER BY Country ASC, CustomerName DESC;""",
        "headers": [
            "Country",
            "Customer",
        ],
        "rows": [
            ["Australia", "Pacific Wave Supplies"],
            ["Canada", "North Shore Adventures"],
            ["Germany", "Alpine Outdoor Gear"],
            ["Ireland", "Atlantic Surfwear"],
            ["UK", "Seaside Boards"],
            ["UK", "Highland Surf Co."],
            ["UK", "Coastal Surf Co."],
        ],
        "highlights": [
            {
                "code_lines": [4],
                "table_columns": [0],
                "table_rows": [],
            },
            {
                "code_lines": [4],
                "table_columns": [1],
                "table_rows": [4, 5, 6],
            },
        ],
    },
    {
        "title": "GROUP BY + ORDER BY",
        "query": """SELECT Country, COUNT(CustomerID) AS [Number of Customers]

FROM Customers

GROUP BY Country

ORDER BY COUNT(CustomerID) DESC;""",
        "headers": [
            "Country",
            "Number of Customers",
        ],
        "rows": [
            ["UK", "428"],
            ["Germany", "312"],
            ["Australia", "197"],
            ["Canada", "154"],
            ["Ireland", "83"],
        ],
        "highlights": [
            {
                "code_lines": [0],
                "table_columns": [1],
                "table_rows": [],
            },
            {
                "code_lines": [4],
                "table_columns": [0],
                "table_rows": [],
            },
            {
                "code_lines": [6],
                "table_columns": [1],
                "table_rows": [0, 1, 2, 3, 4],
            },
        ],
    },
]


# =============================================================================
# SQL SYNTAX HIGHLIGHTING
# =============================================================================

SQL_KEYWORDS = {
    "SELECT",
    "FROM",
    "GROUP",
    "BY",
    "ORDER",
    "ASC",
    "DESC",
    "AS",
    "WHERE",
    "HAVING",
    "AND",
    "OR",
    "JOIN",
    "INNER",
    "LEFT",
    "RIGHT",
    "ON",
    "LIMIT",
    "DISTINCT",
}

SQL_FUNCTIONS = {
    "COUNT",
    "SUM",
    "AVG",
    "MIN",
    "MAX",
}


def syntax_highlight_sql(line):
    """
    Apply Dracula-style syntax highlighting to one SQL line.
    """

    if not line.strip():
        return " "

    tokens = re.findall(
        r"\[[^\]]+\]"
        r"|[A-Za-z_][A-Za-z0-9_]*"
        r"|\d+(?:\.\d+)?"
        r"|'[^']*'"
        r"|[(),;*=]"
        r"|\s+"
        r"|.",
        line,
    )

    output = []

    for token in tokens:

        escaped = escape(token, quote=False)

        if token.isspace():
            output.append(escaped)
            continue

        upper = token.upper()

        if upper in SQL_KEYWORDS:

            output.append(
                f'<span foreground="{PURPLE}">{escaped}</span>'
            )

        elif upper in SQL_FUNCTIONS:

            output.append(
                f'<span foreground="{CYAN}">{escaped}</span>'
            )

        elif token.startswith("'") and token.endswith("'"):

            output.append(
                f'<span foreground="{YELLOW}">{escaped}</span>'
            )

        elif token.startswith("[") and token.endswith("]"):

            output.append(
                f'<span foreground="{GREEN}">{escaped}</span>'
            )

        elif re.fullmatch(r"\d+(?:\.\d+)?", token):

            output.append(
                f'<span foreground="{ORANGE}">{escaped}</span>'
            )

        elif token in {"(", ")", ",", ";", "*", "="}:

            output.append(
                f'<span foreground="{COMMENT}">{escaped}</span>'
            )

        else:

            output.append(
                f'<span foreground="{FOREGROUND}">{escaped}</span>'
            )

    return "".join(output)


# =============================================================================
# SIZING HELPER
# =============================================================================

def fit_to_max(mobject, max_width=None, max_height=None):
    """
    Shrink `mobject` uniformly (preserving its aspect ratio, and therefore
    its font size relative to itself) only if it exceeds the given bounds.

    This deliberately never scales something *up* to fill the available
    space. Using scale_to_fit_width/height unconditionally was why text
    sizing "blew out" between examples: a short query or a single-column
    table would get stretched to fill the same box as a long query or a
    wide table, making its font size balloon relative to its neighbours.
    With this, every example renders at the same natural font size, and
    only the rare example that's actually too big to fit gets shrunk.
    """

    scale_factor = 1.0

    if max_width is not None and mobject.width > max_width:
        scale_factor = min(scale_factor, max_width / mobject.width)

    if max_height is not None and mobject.height > max_height:
        scale_factor = min(scale_factor, max_height / mobject.height)

    if scale_factor < 1.0:
        mobject.scale(scale_factor)


# =============================================================================
# SQL CODE OBJECT
# =============================================================================

class SQLCode(VGroup):

    def __init__(
        self,
        sql,
        font_size=25,
        line_spacing=0.27,
        **kwargs,
    ):
        super().__init__(**kwargs)

        self.sql = sql
        self.lines = []
        # Tracks which entries in self.lines are blank spacer lines, so the
        # typing loop can skip them without relying on whitespace-only text
        # objects (which have no glyph points and crash bounding-box calls).
        self.is_blank = []

        for raw_line in sql.splitlines():

            is_blank = not raw_line.strip()

            if is_blank:
                # A MarkupText built from pure whitespace has no rendered
                # glyphs, so it ends up with an empty points array. Any
                # later call that needs its bounding box (get_center,
                # .width, arrange, etc.) then throws
                # "IndexError: too many indices for array: array is
                # 1-dimensional, but 2 were indexed". Build an invisible
                # placeholder with real geometry instead, purely to hold
                # the line's vertical spacing.
                line = MarkupText(
                    syntax_highlight_sql("x"),
                    font=MONO,
                    font_size=font_size,
                )
                line.set_opacity(0)
            else:
                line = MarkupText(
                    syntax_highlight_sql(raw_line),
                    font=MONO,
                    font_size=font_size,
                )

            self.lines.append(line)
            self.is_blank.append(is_blank)

        self.add(*self.lines)

        self.arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=line_spacing,
        )

    def highlight_line(
        self,
        index,
        opacity=0.13,
    ):
        """
        Subtle Dracula-purple highlight behind a SQL line.
        """

        line = self.lines[index]

        rectangle = RoundedRectangle(
            corner_radius=0.05,
            width=line.width + 0.18,
            height=line.height + 0.10,
            stroke_width=0,
            fill_color=PURPLE,
            fill_opacity=opacity,
        )

        rectangle.move_to(line)

        return rectangle


# =============================================================================
# TERMINAL
# =============================================================================

class TerminalWindow(VGroup):

    def __init__(
        self,
        width=13.4,
        height=7.1,
        **kwargs,
    ):
        super().__init__(**kwargs)

        self.width_value = width
        self.height_value = height

        # Main terminal body.
        self.body = RoundedRectangle(
            corner_radius=0.18,
            width=width,
            height=height,
            fill_color=TERMINAL_BG,
            fill_opacity=1,
            stroke_color=BORDER,
            stroke_width=1.2,
        )

        # Title bar.
        self.title_bar = Rectangle(
            width=width - 0.02,
            height=0.45,
            fill_color=TITLE_BAR,
            fill_opacity=1,
            stroke_width=0,
        )

        self.title_bar.move_to(
            self.body.get_top()
            + DOWN * 0.225
        )

        # macOS controls.
        self.red = Dot(
            radius=0.055,
            color=RED,
        )

        self.yellow = Dot(
            radius=0.055,
            color=YELLOW,
        )

        self.green = Dot(
            radius=0.055,
            color=GREEN,
        )

        dots = VGroup(
            self.red,
            self.yellow,
            self.green,
        )

        dots.arrange(
            RIGHT,
            buff=0.11,
        )

        dots.move_to(
            self.body.get_left()
            + RIGHT * 0.32
            + UP * (
                height / 2
                - 0.225
            )
        )

        self.title = Text(
            "sql",
            font=MONO,
            font_size=12,
            color=COMMENT,
        )

        self.title.move_to(
            self.title_bar.get_center()
        )

        # Vertical divider.
        self.divider = Line(
            UP * 2.75,
            DOWN * 2.75,
            color=DIVIDER,
            stroke_width=1,
        )

        self.divider.move_to(
            self.body.get_center()
        )

        self.divider.set_opacity(0)

        self.add(
            self.body,
            self.title_bar,
            self.red,
            self.yellow,
            self.green,
            self.title,
            self.divider,
        )

    def content_center(self):

        return (
            self.body.get_center()
            + DOWN * 0.25
        )


# =============================================================================
# RESULT TABLE
# =============================================================================

class ResultTable(VGroup):
    """
    A CLI-style result table: a bordered grid (outer box, header rule, and
    a vertical rule between every column) with every column left-aligned,
    similar to what psql / mysql print to a terminal. Rows are ordered and
    revealed top-to-bottom, matching the order they're given in.
    """

    def __init__(
        self,
        headers,
        rows,
        font_size=18,
        header_font_size=18,
        cell_padding_x=0.35,
        row_height=0.52,
        border_color=BORDER,
        **kwargs,
    ):
        super().__init__(**kwargs)

        self.headers = headers
        self.data = rows
        self.row_height = row_height

        column_count = len(headers)
        row_count = len(rows)

        # ---- Build all text first so column widths reflect real glyphs ----

        header_cells = [
            Text(
                h,
                font=MONO,
                font_size=header_font_size,
                color=PURPLE,
                weight="BOLD",
            )
            for h in headers
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

        # ---- Column widths / left edges, terminal-table style ----

        column_widths = []

        for col in range(column_count):

            widest = header_cells[col].width

            for row in body_cells:
                widest = max(widest, row[col].width)

            column_widths.append(widest + cell_padding_x)

        column_lefts = []
        running = 0.0

        for w in column_widths:
            column_lefts.append(running)
            running += w

        table_width = running
        table_height = row_height * (row_count + 1)

        # Local frame: (0, 0) is the table's top-left corner, +x is right,
        # "row_top" grows downward (row 0 sits directly under the header).

        def place_left(cell, col, row_top):
            cell.move_to(
                RIGHT * (column_lefts[col] + cell.width / 2)
                + DOWN * (row_top + row_height / 2)
            )

        for col, cell in enumerate(header_cells):
            place_left(cell, col, 0)

        self.header_cells = VGroup(*header_cells)

        self.rows = []

        for r, row in enumerate(body_cells):

            row_group = VGroup(*row)

            for col, cell in enumerate(row):
                # +1 because row 0 is placed just below the header row.
                place_left(cell, col, row_height * (r + 1))

            # Rows start invisible; reveal_row() fades each one in, in
            # order, so the table fills top-to-bottom.
            row_group.set_opacity(0)

            self.rows.append(row_group)

        # ---- Border / grid lines ----

        self.h_lines = []
        self.v_lines = []

        def h_line(y):
            line = Line(
                ORIGIN,
                RIGHT * table_width,
                color=border_color,
                stroke_width=1,
            )
            line.move_to(RIGHT * (table_width / 2) + DOWN * y)
            self.h_lines.append(line)
            return line

        def v_line(x):
            line = Line(
                ORIGIN,
                DOWN * table_height,
                color=border_color,
                stroke_width=1,
            )
            line.move_to(RIGHT * x + DOWN * (table_height / 2))
            self.v_lines.append(line)
            return line

        border_lines = VGroup()

        # Top border, header separator, bottom border (h_lines[0]/[-1] are
        # used later for column-highlight height).
        border_lines.add(h_line(0))
        border_lines.add(h_line(row_height))
        border_lines.add(h_line(table_height))

        # Left edge, every interior column rule, right edge (v_lines[i]/
        # [i+1] bracket column i, used later for column highlights).
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

    def highlight_row(
        self,
        index,
        opacity=0.12,
    ):

        row = self.rows[index]

        x_left = self.v_lines[0].get_x()
        x_right = self.v_lines[-1].get_x()

        rectangle = Rectangle(
            width=abs(x_right - x_left),
            height=row.height + 0.12,
            stroke_width=0,
            fill_color=PURPLE,
            fill_opacity=opacity,
        )

        rectangle.move_to(
            [
                (x_left + x_right) / 2,
                row.get_y(),
                0,
            ]
        )

        return rectangle

    def highlight_column(
        self,
        index,
        opacity=0.10,
    ):

        x_left = self.v_lines[index].get_x()
        x_right = self.v_lines[index + 1].get_x()
        y_top = self.h_lines[0].get_y()
        y_bottom = self.h_lines[-1].get_y()

        rectangle = Rectangle(
            width=abs(x_right - x_left),
            height=abs(y_top - y_bottom),
            stroke_width=0,
            fill_color=PURPLE,
            fill_opacity=opacity,
        )

        rectangle.move_to(
            [
                (x_left + x_right) / 2,
                (y_top + y_bottom) / 2,
                0,
            ]
        )

        return rectangle


# =============================================================================
# MAIN SCENE
# =============================================================================

class SQLTutorial(Scene):

    def construct(self):

        self.camera.background_color = BACKGROUND

        # ---------------------------------------------------------------------
        # Initial terminal
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
        # Run each SQL example
        # ---------------------------------------------------------------------

        for example_index, example in enumerate(EXAMPLES):

            self.play_example(
                terminal,
                example,
                example_index,
            )

        # Leave the final result on screen briefly.
        self.wait(2.0)

    # =========================================================================
    # EXAMPLE
    # =========================================================================

    def play_example(
        self,
        terminal,
        example,
        example_index,
    ):
        """
        Play one complete SQL example.

        The terminal itself remains on screen between examples.
        """

        # ---------------------------------------------------------------------
        # Create query
        # ---------------------------------------------------------------------

        code = SQLCode(
            example["query"],
            font_size=24,
        )

        # Only shrink if the query genuinely doesn't fit - never scale up
        # a short query to fill the same space as a long one.
        fit_to_max(code, max_width=10.7)

        code.move_to(
            terminal.content_center()
            + DOWN * 0.05
        )

        # ---------------------------------------------------------------------
        # Type query, line by line
        # ---------------------------------------------------------------------
        # Note: `code` (the VGroup) is intentionally NOT added to the scene
        # here. Each Write(line) below adds that one line as it's drawn, so
        # the query appears progressively instead of popping in fully and
        # then being "re-written" on top of itself.

        for line, is_blank in zip(code.lines, code.is_blank):

            if is_blank:

                self.wait(LINE_PAUSE)
                continue

            # Estimate typing duration from visible character count.
            clean_text = re.sub(
                r"<[^>]+>",
                "",
                line.text,
            )

            duration = max(
                TYPING_MIN_TIME,
                len(clean_text)
                * TYPING_TIME_PER_CHARACTER,
            )

            # Cap individual lines so very long SELECT statements do not
            # become absurdly slow.
            duration = min(
                duration,
                1.8,
            )

            self.play(
                Write(line),
                run_time=duration,
            )

            self.wait(LINE_PAUSE)

        # ---------------------------------------------------------------------
        # Let viewer read completed query
        # ---------------------------------------------------------------------

        self.wait(QUERY_PAUSE)

        # ---------------------------------------------------------------------
        # Create result table
        # ---------------------------------------------------------------------

        table = ResultTable(
            headers=example["headers"],
            rows=example["rows"],
        )

        # Same shrink-only rule as the query: don't stretch a small table
        # (e.g. a single-column one) up to fill the pane.
        fit_to_max(table, max_width=5.6, max_height=4.85)

        # Position result in right-hand pane.
        table.move_to(
            terminal.get_center()
            + RIGHT * 3.20
            + DOWN * 0.20
        )

        # ---------------------------------------------------------------------
        # Create left/right labels
        # ---------------------------------------------------------------------

        query_label = Text(
            "SQL QUERY",
            font=MONO,
            font_size=12,
            color=COMMENT,
        )

        query_label.move_to(
            terminal.get_center()
            + LEFT * 3.20
            + UP * 2.65
        )

        result_label = Text(
            "QUERY RESULT",
            font=MONO,
            font_size=12,
            color=COMMENT,
        )

        result_label.move_to(
            terminal.get_center()
            + RIGHT * 3.20
            + UP * 2.65
        )

        # ---------------------------------------------------------------------
        # Target position for SQL
        # ---------------------------------------------------------------------

        code_target = code.copy()

        fit_to_max(code_target, max_width=5.30)

        code_target.move_to(
            terminal.get_center()
            + LEFT * 3.20
            + DOWN * 0.05
        )

        # ---------------------------------------------------------------------
        # Split terminal
        # ---------------------------------------------------------------------

        self.play(
            Transform(
                code,
                code_target,
            ),
            FadeIn(
                query_label,
                shift=DOWN * 0.08,
            ),
            FadeIn(
                result_label,
                shift=DOWN * 0.08,
            ),
            terminal.divider.animate.set_opacity(1),
            run_time=SPLIT_TIME,
        )

        # ---------------------------------------------------------------------
        # Reveal the border grid, then the result table row-by-row,
        # top to bottom
        # ---------------------------------------------------------------------

        self.play(
            Create(table.border_lines),
            FadeIn(table.header_cells),
            run_time=0.5,
        )

        for row_index in range(
            len(table.rows)
        ):

            self.play(
                table.reveal_row(row_index),
                run_time=ROW_REVEAL_TIME,
            )

            self.wait(
                ROW_REVEAL_PAUSE
            )

        self.add(table)

        # ---------------------------------------------------------------------
        # Concept highlights
        # ---------------------------------------------------------------------

        for highlight in example["highlights"]:

            self.perform_highlight(
                code,
                table,
                highlight,
            )

        # ---------------------------------------------------------------------
        # Hold result
        # ---------------------------------------------------------------------

        self.wait(EXAMPLE_PAUSE)

        # ---------------------------------------------------------------------
        # Clear query/result but keep terminal
        # ---------------------------------------------------------------------

        self.play(
            FadeOut(code),
            FadeOut(table),
            FadeOut(query_label),
            FadeOut(result_label),
            terminal.divider.animate.set_opacity(0),
            run_time=0.9,
        )

        # Small pause before next example.
        self.wait(0.5)

    # =========================================================================
    # HIGHLIGHTING
    # =========================================================================

    def perform_highlight(
        self,
        code,
        table,
        highlight,
    ):
        """
        Perform one conceptual highlight.

        Code lines, table columns and rows can be highlighted independently.
        """

        code_highlights = VGroup()

        for line_index in highlight.get(
            "code_lines",
            [],
        ):

            code_highlights.add(
                code.highlight_line(
                    line_index
                )
            )

        table_highlights = VGroup()

        for column_index in highlight.get(
            "table_columns",
            [],
        ):

            table_highlights.add(
                table.highlight_column(
                    column_index
                )
            )

        for row_index in highlight.get(
            "table_rows",
            [],
        ):

            table_highlights.add(
                table.highlight_row(
                    row_index
                )
            )

        all_highlights = VGroup(
            code_highlights,
            table_highlights,
        )

        self.add(all_highlights)

        # Fade in slowly.
        self.play(
            FadeIn(
                all_highlights,
                shift=RIGHT * 0.03,
            ),
            run_time=HIGHLIGHT_IN_TIME,
        )

        # Keep it visible long enough to be understood.
        self.wait(
            HIGHLIGHT_HOLD_TIME
        )

        # Fade out.
        self.play(
            FadeOut(
                all_highlights,
                shift=LEFT * 0.03,
            ),
            run_time=HIGHLIGHT_OUT_TIME,
        )

        self.remove(
            all_highlights
        )


# =============================================================================
# END
# =============================================================================

"""
Render examples:

    python -B -m manim -pqh sql_animation.py SQLTutorial

Preview at lower quality:

    python -B -m manim -pql sql_animation.py SQLTutorial

The scene intentionally contains no code that automatically renders itself.
"""