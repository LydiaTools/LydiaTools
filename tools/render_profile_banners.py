#!/usr/bin/env python3
"""Render the English LydiaTools profile banners from real project screenshots.

Requires Pillow. Run from any directory with:
    python3 tools/render_profile_banners.py
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
SCALE = 2

INK = "#0d1828"
PANEL = "#111f32"
WHITE = "#f7f9f7"
TEXT = "#c5d1dd"
MUTED = "#91a9be"
RULE = "#34475d"

PROJECTS = [
    ("browser-agent-recovery.png", "BROWSER RELIABILITY", "Browser Agent Blueprint", "Verify a save before retrying.", "#91d9e6"),
    ("covercalc-cost-comparison.png", "GARDEN BUYING", "CoverCalc Pro", "Compare bags, bulk and delivery.", "#f2c66d"),
    ("social-post-image-maker-en.png", "SOCIAL VISUALS", "Social Post Image Maker", "One idea, four native layouts.", "#8fe1b8"),
    ("longform-atlas-ip-plan.png", "CREATOR PUBLISHING", "Global Longform SEO Studio", "Plan articles around a creator identity.", "#d0b8ff"),
    ("notesignal-popup-empty.png", "SOURCE-LINKED RESEARCH", "Xiaohongshu NoteSignal", "Keep visible notes tied to sources.", "#f5a9b8"),
    ("foreign-trade-demo.png", "TRADE INQUIRIES", "Lydia Foreign Trade System", "Review evidence before follow-up.", "#f0a66a"),
    ("say-it-plainly-v0.9.0.png", "PRACTICAL REPLIES", "Say It Plainly", "Turn a message into clear next steps.", "#91d9e6"),
    ("desktop-flow-capture-proof.png", "DESKTOP CAPTURE", "Desktop Flow", "Save a task before switching apps.", "#f2c66d"),
    ("xiaoran-output-excerpt.png", "CONTENT RESEARCH", "Xiaoran Topic Assistant", "Shape research into usable topic briefs.", "#8fe1b8"),
    ("biefangong-v0.1.0.png", "SCOPE CHANGES", "Scope Check", "Compare a request with the agreed scope.", "#d0b8ff"),
    ("skin-workshop-library.png", "CODEX THEMING", "Codex Skin Workshop", "My enhancements and skins; original app by luhaozwork.", "#f5a9b8"),
]

FEATURED_PROJECTS = PROJECTS[:9]


def load_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    if bold:
        candidates = [
            "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
            "/System/Library/Fonts/Supplemental/Arial.ttf",
            "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf",
        ]
    else:
        candidates = [
            "/System/Library/Fonts/Supplemental/Arial.ttf",
            "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
            "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
        ]
    for path in candidates:
        if Path(path).exists():
            return ImageFont.truetype(path, size * SCALE)
    return ImageFont.load_default()


def wrap_text(text: str, font: ImageFont.FreeTypeFont, width: int) -> list[str]:
    max_width = width * SCALE
    lines: list[str] = []
    current = ""
    for word in text.split():
        candidate = word if not current else f"{current} {word}"
        if current and font.getlength(candidate) > max_width:
            lines.append(current)
            current = word
        else:
            current = candidate
    if current:
        lines.append(current)
    return lines


def draw_tracked(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str,
                 font: ImageFont.FreeTypeFont, fill: str, tracking: int) -> None:
    x, y = xy
    for character in text:
        draw.text((x * SCALE, y * SCALE), character, font=font, fill=fill)
        x += round(font.getlength(character) / SCALE) + tracking


def draw_lines(draw: ImageDraw.ImageDraw, xy: tuple[int, int], lines: list[str],
               font: ImageFont.FreeTypeFont, fill: str, line_height: int) -> None:
    x, y = xy
    for line in lines:
        draw.text((x * SCALE, y * SCALE), line, font=font, fill=fill)
        y += line_height


def fitted_preview(filename: str, size: tuple[int, int]) -> Image.Image:
    source = Image.open(ASSETS / filename).convert("RGB")
    centering = (0.5, 0.12) if filename == "skin-workshop-library.png" else (0.5, 0.5)
    return ImageOps.fit(source, (size[0] * SCALE, size[1] * SCALE),
                        method=Image.Resampling.LANCZOS, centering=centering)


def draw_card(canvas: Image.Image, project: tuple[str, str, str, str, str],
              x: int, y: int, width: int, mobile: bool) -> None:
    filename, category, name, value, accent = project
    draw = ImageDraw.Draw(canvas)
    card_height = 112 if mobile else 152
    card_bottom = y + card_height
    draw.rounded_rectangle(
        (x * SCALE, y * SCALE, (x + width) * SCALE, card_bottom * SCALE),
        radius=10 * SCALE, fill=PANEL,
    )
    draw.rounded_rectangle(
        (x * SCALE, y * SCALE, (x + width) * SCALE, (y + 4) * SCALE),
        radius=2 * SCALE, fill=accent,
    )

    image_height = 38 if mobile else 66
    image_y = y + (7 if mobile else 8)
    preview = fitted_preview(filename, (width - 16, image_height))
    mask = Image.new("L", preview.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle(
        (0, 0, preview.width - 1, preview.height - 1), radius=6 * SCALE, fill=255,
    )
    canvas.paste(preview, ((x + 8) * SCALE, image_y * SCALE), mask)

    category_font = load_font(7 if mobile else 9, bold=True)
    name_font = load_font(10 if mobile else 15, bold=True)
    value_font = load_font(8 if mobile else 10, bold=False)
    text_x = x + 8
    content_width = width - 16
    draw.text((text_x * SCALE, (y + image_height + (9 if mobile else 11)) * SCALE),
              category, font=category_font, fill=accent)

    name_y = y + image_height + (21 if mobile else 26)
    name_lines = wrap_text(name, name_font, content_width)[:2]
    name_line_height = 12 if mobile else 18
    draw_lines(draw, (text_x, name_y), name_lines, name_font, WHITE, name_line_height)

    value_y = name_y + len(name_lines) * name_line_height + (1 if mobile else 2)
    value_lines = wrap_text(value, value_font, content_width)[:2]
    draw_lines(draw, (text_x, value_y), value_lines, value_font, TEXT, 10 if mobile else 12)


def finish(canvas: Image.Image, destination: Path) -> None:
    canvas.convert("RGB").save(destination, format="PNG", optimize=True)


def draw_feature_card(canvas: Image.Image, project: tuple[str, str, str, str, str],
                      x: int, y: int, width: int, mobile: bool) -> None:
    filename, category, name, value, accent = project
    draw = ImageDraw.Draw(canvas)
    card_height = 142 if mobile else 178
    image_height = 56 if mobile else 98
    image_top = y + (8 if mobile else 9)
    inset = 8 if mobile else 12
    image_width = width - inset * 2
    draw.rounded_rectangle(
        (x * SCALE, y * SCALE, (x + width) * SCALE, (y + card_height) * SCALE),
        radius=(10 if mobile else 12) * SCALE, fill=PANEL,
    )
    draw.rounded_rectangle(
        (x * SCALE, y * SCALE, (x + width) * SCALE, (y + 4) * SCALE),
        radius=2 * SCALE, fill=accent,
    )
    preview = fitted_preview(filename, (image_width, image_height))
    mask = Image.new("L", preview.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle(
        (0, 0, preview.width - 1, preview.height - 1), radius=6 * SCALE, fill=255,
    )
    canvas.paste(preview, ((x + inset) * SCALE, image_top * SCALE), mask)

    text_x = x + inset
    content_width = width - inset * 2
    category_size = 7 if mobile else 9
    name_size = 10 if mobile else 16
    value_size = 8 if mobile else 11
    category_top = image_top + image_height + (7 if mobile else 9)
    category_font = load_font(category_size, bold=True)
    name_font = load_font(name_size, bold=True)
    value_font = load_font(value_size)
    draw.text((text_x * SCALE, category_top * SCALE), category,
              font=category_font, fill=accent)

    name_top = category_top + (12 if mobile else 16)
    name_lines = wrap_text(name, name_font, content_width)[:2]
    name_line_height = 12 if mobile else 19
    draw_lines(draw, (text_x, name_top), name_lines, name_font, WHITE, name_line_height)

    value_top = name_top + len(name_lines) * name_line_height + (0 if mobile else 2)
    value_lines = wrap_text(value, value_font, content_width)[:2]
    draw_lines(draw, (text_x, value_top), value_lines, value_font, TEXT,
               10 if mobile else 13)


def render_featured_desktop() -> None:
    width, height = 1200, 900
    canvas = Image.new("RGBA", (width * SCALE, height * SCALE), INK)
    draw = ImageDraw.Draw(canvas)
    draw.ellipse((1075 * SCALE, -170 * SCALE, 1370 * SCALE, 125 * SCALE), fill="#1c2d49")
    draw.ellipse((-145 * SCALE, 835 * SCALE, 100 * SCALE, 1070 * SCALE), fill="#123447")

    draw_tracked(draw, (42, 15), "INDEPENDENT MAKER · PRACTICAL SOFTWARE",
                 load_font(12, bold=True), MUTED, 2)
    title_font = load_font(154, bold=True)
    draw.text((39 * SCALE, 34 * SCALE), "Lydia", font=title_font, fill=WHITE)
    draw.text((39 * SCALE, 147 * SCALE), "Tools", font=title_font, fill=WHITE)
    draw.text((640 * SCALE, 82 * SCALE), "Small tools for",
              font=load_font(31, bold=True), fill=TEXT)
    draw.text((640 * SCALE, 124 * SCALE), "clearer next steps.",
              font=load_font(27), fill=TEXT)
    draw.text((642 * SCALE, 190 * SCALE), "9 PROJECTS · REAL SCREENS",
              font=load_font(12, bold=True), fill="#9ad9d0")
    draw.line((40 * SCALE, 308 * SCALE, 1160 * SCALE, 308 * SCALE), fill=RULE, width=2 * SCALE)

    margin, gap = 40, 20
    card_width = (width - margin * 2 - gap * 2) // 3
    for index, project in enumerate(FEATURED_PROJECTS):
        row, column = divmod(index, 3)
        draw_feature_card(canvas, project, margin + column * (card_width + gap),
                          320 + row * 188, card_width, mobile=False)
    finish(canvas, ASSETS / "hero-v17.png")


def render_featured_mobile() -> None:
    width, height = 390, 975
    canvas = Image.new("RGBA", (width * SCALE, height * SCALE), INK)
    draw = ImageDraw.Draw(canvas)
    draw.ellipse((290 * SCALE, -82 * SCALE, 466 * SCALE, 96 * SCALE), fill="#1c2d49")
    draw.ellipse((-72 * SCALE, 890 * SCALE, 76 * SCALE, 1040 * SCALE), fill="#123447")

    draw_tracked(draw, (17, 11), "INDEPENDENT MAKER · PRACTICAL SOFTWARE",
                 load_font(7, bold=True), MUTED, 1)
    title_font = load_font(68, bold=True)
    draw.text((15 * SCALE, 25 * SCALE), "Lydia", font=title_font, fill=WHITE)
    draw.text((15 * SCALE, 76 * SCALE), "Tools", font=title_font, fill=WHITE)
    draw.text((18 * SCALE, 158 * SCALE), "Small tools for clearer next steps.",
              font=load_font(14), fill=TEXT)
    draw_tracked(draw, (19, 179), "9 PROJECTS · REAL SCREENS",
                 load_font(7, bold=True), "#9ad9d0", 0)
    draw.line((17 * SCALE, 197 * SCALE, 373 * SCALE, 197 * SCALE), fill=RULE, width=2 * SCALE)

    margin, gap = 17, 10
    card_width = (width - margin * 2 - gap) // 2
    for index, project in enumerate(FEATURED_PROJECTS):
        row, column = divmod(index, 2)
        y = 208 + row * 152
        if index == len(FEATURED_PROJECTS) - 1 and len(FEATURED_PROJECTS) % 2:
            draw_feature_card(canvas, project, margin, y, width - margin * 2, mobile=True)
        else:
            draw_feature_card(canvas, project, margin + column * (card_width + gap),
                              y, card_width, mobile=True)
    finish(canvas, ASSETS / "hero-mobile-v17.png")


def render_desktop() -> None:
    width, height = 1200, 930
    canvas = Image.new("RGBA", (width * SCALE, height * SCALE), INK)
    draw = ImageDraw.Draw(canvas)
    draw.ellipse((1060 * SCALE, -190 * SCALE, 1380 * SCALE, 130 * SCALE), fill="#1c2d49")
    draw.ellipse((-140 * SCALE, 820 * SCALE, 90 * SCALE, 1050 * SCALE), fill="#123447")

    draw_tracked(draw, (42, 20), "INDEPENDENT MAKER · PRACTICAL SOFTWARE",
                 load_font(13, bold=True), MUTED, 2)
    draw_tracked(draw, (40, 45), "LydiaTools", load_font(156, bold=True), WHITE, -5)
    draw.text((916 * SCALE, 77 * SCALE), "Practical software.",
              font=load_font(24, bold=True), fill=TEXT)
    draw.text((916 * SCALE, 111 * SCALE), "Clearer next steps.",
              font=load_font(21), fill=TEXT)
    draw_tracked(draw, (918, 151), "11 PROJECTS · REAL SCREENS",
                 load_font(9, bold=True), MUTED, 1)
    draw.rounded_rectangle((918 * SCALE, 176 * SCALE, 1090 * SCALE, 209 * SCALE),
                           radius=14 * SCALE, outline="#42617d", width=1 * SCALE)
    draw.text((931 * SCALE, 185 * SCALE), "TOOLS WITH A PURPOSE",
              font=load_font(8, bold=True), fill="#9ad9d0")
    draw.line((40 * SCALE, 232 * SCALE, 1160 * SCALE, 232 * SCALE), fill=RULE, width=2 * SCALE)

    margin, gap, card_width = 40, 20, 360
    x_positions = [margin + i * (card_width + gap) for i in range(3)]
    for index, project in enumerate(PROJECTS):
        row, column = divmod(index, 3)
        if row == 3:
            wide_width = 550
            x = margin + column * (wide_width + gap)
            draw_card(canvas, project, x, 758, wide_width, mobile=False)
        else:
            draw_card(canvas, project, x_positions[column], 246 + row * 170, card_width, mobile=False)

    finish(canvas, ASSETS / "hero-v14.png")


def render_mobile() -> None:
    width, height = 390, 930
    canvas = Image.new("RGBA", (width * SCALE, height * SCALE), INK)
    draw = ImageDraw.Draw(canvas)
    draw.ellipse((285 * SCALE, -95 * SCALE, 470 * SCALE, 90 * SCALE), fill="#1c2d49")
    draw.ellipse((-70 * SCALE, 790 * SCALE, 75 * SCALE, 940 * SCALE), fill="#123447")

    draw_tracked(draw, (17, 13), "INDEPENDENT MAKER · PRACTICAL SOFTWARE",
                 load_font(8, bold=True), MUTED, 1)
    draw_tracked(draw, (17, 34), "LydiaTools", load_font(57, bold=True), WHITE, -2)
    draw.text((19 * SCALE, 99 * SCALE), "Practical software. Clearer next steps.",
              font=load_font(15), fill=TEXT)
    draw_tracked(draw, (19, 125), "11 TOOLS · REAL SCREENS · CLEAR STATUS",
                 load_font(7, bold=True), MUTED, 0)
    draw.line((17 * SCALE, 151 * SCALE, 373 * SCALE, 151 * SCALE), fill=RULE, width=2 * SCALE)

    margin, gap, card_width = 17, 10, 173
    x_positions = [margin, margin + card_width + gap]
    for index, project in enumerate(PROJECTS):
        row, column = divmod(index, 2)
        if index == len(PROJECTS) - 1:
            draw_card(canvas, project, margin, 165 + row * 119, width - margin * 2, mobile=True)
        else:
            draw_card(canvas, project, x_positions[column], 165 + row * 119, card_width, mobile=True)

    finish(canvas, ASSETS / "hero-mobile-v14.png")


if __name__ == "__main__":
    render_desktop()
    render_mobile()
    render_featured_desktop()
    render_featured_mobile()
    print("Rendered v14 portfolio banners and v17 nine-project banners")
