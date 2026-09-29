"""
Python Classes Tutorial Animation
==========================================

Single-scene Manim animation for a Python classes tutorial, refactored
from the SQL query/result-table version.

The animation progresses through three runnable Python examples, each
building on the last:

    1. Class attributes + creating an object
    2. __init__() and self (per-instance attributes)
    3. __str__() (custom string representation)

Visual style:
    - Dracula colour palette
    - Dark macOS-style terminal
    - JetBrains Mono / Nerd Font
    - Slow, readable animations
    - Minimal transitions
    - Persistent terminal
    - Code -> Output relationship (instead of Query -> Result)
    - Output pane styled like a REPL: each statement is echoed with a
      ">>> " prompt, followed by its printed result, revealed one
      statement at a time.
"""

# Imports

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

# Main Python accent.
PYTHON_ACCENT = PURPLE


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

TERMINAL_ENTER_TIME = 1.0

# Minimum time used for typing a line.
TYPING_MIN_TIME = 0.55

# Approximate time per character.
TYPING_TIME_PER_CHARACTER = 0.035

# Time between code lines.
LINE_PAUSE = 0.20

# Pause after completing the code block.
CODE_PAUSE = 1.3

# Time spent transforming the terminal.
SPLIT_TIME = 1.5

# Time used to reveal a REPL statement + its result.
ROW_REVEAL_TIME = 0.45

# Time between REPL rows.
ROW_REVEAL_PAUSE = 0.18

# How long conceptual highlights remain visible.
HIGHLIGHT_IN_TIME = 0.45
HIGHLIGHT_HOLD_TIME = 0.9
HIGHLIGHT_OUT_TIME = 0.45

# Pause between examples.
EXAMPLE_PAUSE = 1.5


# =============================================================================
# PYTHON CLASSES EXAMPLES
# =============================================================================
#
# Each example's "code" is the full snippet shown (typed) in the left pane.
# "repl" is the sequence of statements that actually produce visible
# output when the snippet runs - each one is echoed in the right pane as
# ">>> <statement>" followed by its printed result, one at a time.
#
# "highlights" pairs specific code lines with specific repl rows to draw
# out a concept (e.g. self.colour = colour <-> the printed colour values).

EXAMPLES = [
    {
        "title": "Class Attributes + Objects",
        "code": """class HiluxSurf:

    make = "Toyota"
    model = "Hilux Surf"
    year = 1994


surf1 = HiluxSurf()

print(surf1.make)
print(surf1.model)
print(surf1.year)""",
        "repl": [
            {"statement": "print(surf1.make)", "result": "Toyota"},
            {"statement": "print(surf1.model)", "result": "Hilux Surf"},
            {"statement": "print(surf1.year)", "result": "1994"},
        ],
        "highlights": [
            {
                # make / model / year are class attributes - shared by
                # every instance.
                "code_lines": [2, 3, 4],
                "repl_rows": [0, 1, 2],
            },
        ],
    },
    {
        "title": "__init__() and self",
        "code": """class HiluxSurf:

    make = "Toyota"
    model = "Hilux Surf"
    year = 1994

    def __init__(self, colour, engine):

        self.colour = colour
        self.engine = engine


surf1 = HiluxSurf("Red", "3.0L Diesel")
surf2 = HiluxSurf("Baby Blue", "2.4L Diesel")

print(surf1.colour)
print(surf2.colour)""",
        "repl": [
            {"statement": "print(surf1.colour)", "result": "Red"},
            {"statement": "print(surf2.colour)", "result": "Baby Blue"},
        ],
        "highlights": [
            {
                # __init__ runs automatically when the object is created.
                "code_lines": [5],
                "repl_rows": [],
            },
            {
                # self.colour = colour: each instance gets its own copy.
                "code_lines": [7, 8],
                "repl_rows": [0, 1],
            },
        ],
    },
    {
        "title": "__str__() Method",
        "code": """class HiluxSurf:

    make = "Toyota"
    model = "Hilux Surf"
    year = 1994

    def __init__(self, colour, engine):

        self.colour = colour
        self.engine = engine

    def __str__(self):

        return f"{self.year} {self.make} {self.model} - {self.colour}, {self.engine}"


surf1 = HiluxSurf("Red", "3.0L Diesel")
surf2 = HiluxSurf("Baby Blue", "2.4L Diesel")

print(surf1)
print(surf2)""",
        "repl": [
            {
                "statement": "print(surf1)",
                "result": "1994 Toyota Hilux Surf - Red, 3.0L Diesel",
            },
            {
                "statement": "print(surf2)",
                "result": "1994 Toyota Hilux Surf - Baby Blue, 2.4L Diesel",
            },
        ],
        "highlights": [
            {
                # __str__ controls what printing the object shows.
                "code_lines": [10, 12],
                "repl_rows": [0, 1],
            },
        ],
    },
]


# =============================================================================
# PYTHON SYNTAX HIGHLIGHTING
# =============================================================================

PY_KEYWORDS = {
    "class",
    "def",
    "return",
    "if",
    "elif",
    "else",
    "for",
    "while",
    "in",
    "import",
    "from",
    "as",
    "and",
    "or",
    "not",
    "is",
    "pass",
    "break",
    "continue",
    "lambda",
    "yield",
    "with",
    "try",
    "except",
    "finally",
    "raise",
    "global",
    "nonlocal",
    "del",
    "assert",
    "True",
    "False",
    "None",
}

PY_BUILTINS = {
    "print",
    "len",
    "str",
    "int",
    "float",
    "list",
    "dict",
    "set",
    "tuple",
    "super",
    "isinstance",
    "range",
    "type",
}


def syntax_highlight_python(line):
    """
    Apply Dracula-style syntax highlighting to one line of Python.
    """

    if not line.strip():
        return " "

    tokens = re.findall(
        r"__[A-Za-z_]+__"
        r"|f\"[^\"]*\""
        r"|f'[^']*'"
        r"|\"[^\"]*\""
        r"|'[^']*'"
        r"|[A-Za-z_][A-Za-z0-9_]*"
        r"|\d+(?:\.\d+)?"
        r"|[(),.:=\[\]{}]"
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

        if re.fullmatch(r"__[A-Za-z_]+__", token):

            # Dunder / magic methods - __init__, __str__, etc. These are
            # the conceptual focus of the tutorial, so they get their own
            # colour rather than blending in as a plain identifier.
            output.append(
                f'<span foreground="{CYAN}">{escaped}</span>'
            )

        elif token == "self":

            # self gets its own colour - it is the single most important
            # concept in this tutorial and deserves to stand out from
            # both keywords and ordinary identifiers.
            output.append(
                f'<span foreground="{PINK}">{escaped}</span>'
            )

        elif token in PY_KEYWORDS:

            output.append(
                f'<span foreground="{PURPLE}">{escaped}</span>'
            )

        elif token in PY_BUILTINS:

            output.append(
                f'<span foreground="{CYAN}">{escaped}</span>'
            )

        elif (
            token.startswith("f\"")
            or token.startswith("f'")
            or (token.startswith("\"") and token.endswith("\""))
            or (token.startswith("'") and token.endswith("'"))
        ):

            output.append(
                f'<span foreground="{YELLOW}">{escaped}</span>'
            )

        elif re.fullmatch(r"\d+(?:\.\d+)?", token):

            output.append(
                f'<span foreground="{ORANGE}">{escaped}</span>'
            )

        elif token in {"(", ")", ",", ".", ":", "=", "[", "]", "{", "}"}:

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
    space, so every example renders at the same natural font size and
    only a genuinely oversized example gets shrunk.
    """

    scale_factor = 1.0

    if max_width is not None and mobject.width > max_width:
        scale_factor = min(scale_factor, max_width / mobject.width)

    if max_height is not None and mobject.height > max_height:
        scale_factor = min(scale_factor, max_height / mobject.height)

    if scale_factor < 1.0:
        mobject.scale(scale_factor)


# =============================================================================
# PYTHON CODE OBJECT
# =============================================================================

class PythonCode(VGroup):

    def __init__(
        self,
        source,
        font_size=25,
        line_spacing=0.27,
        **kwargs,
    ):
        super().__init__(**kwargs)

        self.source = source
        self.lines = []
        # Tracks which entries in self.lines are blank spacer lines, so the
        # typing loop can skip them without relying on whitespace-only text
        # objects (which have no glyph points and crash bounding-box calls).
        self.is_blank = []
        # Leading-space count per line. Pango/MarkupText ink extents don't
        # include leading whitespace, so aligning every line's own left
        # edge (below) would otherwise erase indentation entirely. Indent
        # is stripped before highlighting and re-applied as an explicit
        # shift afterwards.
        self.indents = []

        # Reference glyph to measure one monospace character's advance
        # width at this font size, used to re-apply indentation below.
        reference_char = Text(
            "M",
            font=MONO,
            font_size=font_size,
        )
        char_width = reference_char.width

        for raw_line in source.splitlines():

            is_blank = not raw_line.strip()
            indent = len(raw_line) - len(raw_line.lstrip(" "))
            content = raw_line.lstrip(" ")

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
                    syntax_highlight_python("x"),
                    font=MONO,
                    font_size=font_size,
                )
                line.set_opacity(0)
                indent = 0
            else:
                line = MarkupText(
                    syntax_highlight_python(content),
                    font=MONO,
                    font_size=font_size,
                )

            self.lines.append(line)
            self.is_blank.append(is_blank)
            self.indents.append(indent)

        self.add(*self.lines)

        self.arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=line_spacing,
        )

        # Re-apply indentation now that lines are vertically arranged and
        # share a common (zero-indent) left edge.
        for line, indent in zip(self.lines, self.indents):

            if indent:
                line.shift(
                    RIGHT * indent * char_width
                )

    def highlight_line(
        self,
        index,
        opacity=0.13,
    ):
        """
        Subtle Dracula-purple highlight behind a code line.
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
            "python",
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
# REPL OUTPUT PANE
# =============================================================================

class ReplPane(VGroup):
    """
    A REPL-style output pane: each entry is a ">>> <statement>" prompt
    line followed by its printed result line, styled like a Python
    interactive shell. Entries are revealed one at a time, top to bottom.
    """

    def __init__(
        self,
        entries,
        font_size=18,
        prompt_color=GREEN,
        statement_font_size=None,
        row_spacing=0.14,
        block_spacing=0.30,
        **kwargs,
    ):
        super().__init__(**kwargs)

        self.entries = entries
        statement_font_size = statement_font_size or font_size

        self.blocks = []

        for entry in entries:

            prompt = Text(
                ">>> ",
                font=MONO,
                font_size=statement_font_size,
                color=prompt_color,
            )

            statement = MarkupText(
                syntax_highlight_python(entry["statement"]),
                font=MONO,
                font_size=statement_font_size,
            )

            statement_line = VGroup(prompt, statement)
            statement_line.arrange(RIGHT, buff=0.03)

            result = Text(
                entry["result"],
                font=MONO,
                font_size=font_size,
                color=FOREGROUND,
            )

            block = VGroup(statement_line, result)
            block.arrange(
                DOWN,
                aligned_edge=LEFT,
                buff=row_spacing,
            )

            # Blocks start invisible; reveal_row() fades each one in, in
            # order, so the pane fills top-to-bottom like a live shell.
            block.set_opacity(0)

            self.blocks.append(block)

        self.add(*self.blocks)

        self.arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=block_spacing,
        )

    def reveal_row(self, index):

        return self.blocks[index].animate.set_opacity(1)

    def highlight_row(
        self,
        index,
        opacity=0.12,
    ):

        block = self.blocks[index]

        rectangle = RoundedRectangle(
            corner_radius=0.05,
            width=block.width + 0.30,
            height=block.height + 0.16,
            stroke_width=0,
            fill_color=PURPLE,
            fill_opacity=opacity,
        )

        rectangle.move_to(block)

        return rectangle


# =============================================================================
# MAIN SCENE
# =============================================================================

class PythonClassesTutorial(Scene):

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
        # Run each Python example
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
        Play one complete Python example.

        The terminal itself remains on screen between examples.
        """

        # ---------------------------------------------------------------------
        # Create code
        # ---------------------------------------------------------------------

        code = PythonCode(
            example["code"],
            font_size=24,
        )

        # Left-align the code with a buffer from the terminal's left edge,
        # instead of centering it in the terminal. The buffer and the max
        # width are both derived from the terminal's own width so they
        # stay consistent if TerminalWindow's size ever changes.
        left_buffer = terminal.width_value * 0.25
        right_margin = 0.6
        max_code_width = (
            terminal.width_value
            - left_buffer
            - right_margin
        )

        # Vertical bound too - without this, longer examples (more code
        # lines, e.g. the __init__/__str__ ones) can render taller than
        # the terminal itself and overflow top/bottom. Shrink-only, same
        # as the width bound, so short examples stay at full size.
        max_code_height = (
            terminal.height_value
            - 1.3
        )

        # Only shrink if the code genuinely doesn't fit - never scale up
        # a short snippet to fill the same space as a long one.
        fit_to_max(
            code,
            max_width=max_code_width,
            max_height=max_code_height,
        )

        code.move_to(
            terminal.content_center()
            + DOWN * 0.05
        )

        code.align_to(
            terminal.body,
            LEFT,
        )

        code.shift(
            RIGHT * left_buffer
        )

        # ---------------------------------------------------------------------
        # Type code, line by line
        # ---------------------------------------------------------------------
        # Note: `code` (the VGroup) is intentionally NOT added to the scene
        # here. Each Write(line) below adds that one line as it's drawn, so
        # the snippet appears progressively instead of popping in fully and
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

            # Cap individual lines so very long ones do not become
            # absurdly slow.
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
        # Let viewer read completed code
        # ---------------------------------------------------------------------

        self.wait(CODE_PAUSE)

        # ---------------------------------------------------------------------
        # Create REPL output pane
        # ---------------------------------------------------------------------

        repl = ReplPane(
            entries=example["repl"],
        )

        # Same shrink-only rule as the code: don't stretch a short REPL
        # trace up to fill the pane.
        fit_to_max(repl, max_width=5.6, max_height=4.85)

        # Position output in right-hand pane.
        repl.move_to(
            terminal.get_center()
            + RIGHT * 3.20
            + DOWN * 0.20
        )

        # ---------------------------------------------------------------------
        # Create left/right labels
        # ---------------------------------------------------------------------

        code_label = Text(
            "PYTHON CODE",
            font=MONO,
            font_size=12,
            color=COMMENT,
        )

        code_label.move_to(
            terminal.get_center()
            + LEFT * 3.20
            + UP * 2.65
        )

        output_label = Text(
            "OUTPUT",
            font=MONO,
            font_size=12,
            color=COMMENT,
        )

        output_label.move_to(
            terminal.get_center()
            + RIGHT * 3.20
            + UP * 2.65
        )

        # ---------------------------------------------------------------------
        # Target position for code
        # ---------------------------------------------------------------------

        code_target = code.copy()

        fit_to_max(code_target, max_width=5.30, max_height=4.8)

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
                code_label,
                shift=DOWN * 0.08,
            ),
            FadeIn(
                output_label,
                shift=DOWN * 0.08,
            ),
            terminal.divider.animate.set_opacity(1),
            run_time=SPLIT_TIME,
        )

        # ---------------------------------------------------------------------
        # Reveal the REPL rows, one statement + result at a time
        # ---------------------------------------------------------------------

        for row_index in range(
            len(repl.blocks)
        ):

            self.play(
                repl.reveal_row(row_index),
                run_time=ROW_REVEAL_TIME,
            )

            self.wait(
                ROW_REVEAL_PAUSE
            )

        self.add(repl)

        # ---------------------------------------------------------------------
        # Concept highlights
        # ---------------------------------------------------------------------

        for highlight in example["highlights"]:

            self.perform_highlight(
                code,
                repl,
                highlight,
            )

        # ---------------------------------------------------------------------
        # Hold result
        # ---------------------------------------------------------------------

        self.wait(EXAMPLE_PAUSE)

        # ---------------------------------------------------------------------
        # Clear code/output but keep terminal
        # ---------------------------------------------------------------------

        self.play(
            FadeOut(code),
            FadeOut(repl),
            FadeOut(code_label),
            FadeOut(output_label),
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
        repl,
        highlight,
    ):
        """
        Perform one conceptual highlight.

        Code lines and REPL rows can be highlighted independently, so a
        concept like "self.colour = colour" can be tied visually to the
        printed values it produces.
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

        repl_highlights = VGroup()

        for row_index in highlight.get(
            "repl_rows",
            [],
        ):

            repl_highlights.add(
                repl.highlight_row(
                    row_index
                )
            )

        all_highlights = VGroup(
            code_highlights,
            repl_highlights,
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