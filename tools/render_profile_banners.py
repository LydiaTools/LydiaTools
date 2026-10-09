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
    ("longform-atlas-ip-plan.png", "CREATOR PUBLISHING", "Global Longform SEO Studio", "Plan evidence-led articles around your IP.", "#d0b8ff"),
    ("notesignal-popup-empty.png", "SOURCE-LINKED RESEARCH", "Xiaohongshu NoteSignal", "Keep visible notes tied to sources.", "#f5a9b8"),
    ("foreign-trade-demo.png", "TRADE INQUIRIES", "Lydia Foreign Trade System", "Review evidence before follow-up.", "#f0a66a"),
]


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
    return ImageOps.fit(source, (size[0] * SCALE, size[1] * SCALE),
                        method=Image.Resampling.LANCZOS, centering=(0.5, 0.5))


def draw_card(canvas: Image.Image, project: tuple[str, str, str, str, str],
              x: int, y: int, width: int, mobile: bool) -> None:
    filename, category, name, value, accent = project
    draw = ImageDraw.Draw(canvas)
    card_height = 112 if mobile else 140
    card_bottom = y + card_height
    draw.rounded_rectangle(
        (x * SCALE, y * SCALE, (x + width) * SCALE, card_bottom * SCALE),
        radius=10 * SCALE, fill=PANEL,
    )
    draw.rounded_rectangle(
        (x * SCALE, y * SCALE, (x + width) * SCALE, (y + 4) * SCALE),
        radius=2 * SCALE, fill=accent,
    )

    image_height = 40 if mobile else 72
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

    name_y = y + image_height + (21 if mobile else 28)
    name_lines = wrap_text(name, name_font, content_width)[:2]
    name_line_height = 12 if mobile else 18
    draw_lines(draw, (text_x, name_y), name_lines, name_font, WHITE, name_line_height)

    value_y = name_y + len(name_lines) * name_line_height + (1 if mobile else 2)
    value_lines = wrap_text(value, value_font, content_width)[:2]
    draw_lines(draw, (text_x, value_y), value_lines, value_font, TEXT, 10 if mobile else 12)


def finish(canvas: Image.Image, destination: Path) -> None:
    canvas.convert("RGB").save(destination, format="PNG", optimize=True)


def render_desktop() -> None:
    width, height = 1200, 720
    canvas = Image.new("RGBA", (width * SCALE, height * SCALE), INK)
    draw = ImageDraw.Draw(canvas)
    draw.ellipse((1060 * SCALE, -190 * SCALE, 1380 * SCALE, 130 * SCALE), fill="#1c2d49")
    draw.ellipse((-140 * SCALE, 590 * SCALE, 90 * SCALE, 820 * SCALE), fill="#123447")

    draw_tracked(draw, (46, 25), "INDEPENDENT MAKER · PRACTICAL SOFTWARE",
                 load_font(13, bold=True), MUTED, 2)
    draw_tracked(draw, (20, 42), "LydiaTools", load_font(270, bold=True), WHITE, -27)
    draw.text((50 * SCALE, 350 * SCALE), "Small tools. Clearer next steps.",
              font=load_font(25), fill=TEXT)
    draw_tracked(draw, (50, 383), "BROWSER RECOVERY · GARDEN BUYING · CREATOR TOOLS · RESEARCH",
                 load_font(11, bold=True), MUTED, 1)
    draw.rounded_rectangle((1000 * SCALE, 346 * SCALE, 1158 * SCALE, 379 * SCALE),
                           radius=14 * SCALE, outline="#42617d", width=1 * SCALE)
    draw.text((1012 * SCALE, 354 * SCALE), "6 REAL PROJECTS", font=load_font(10, bold=True), fill="#9ad9d0")
    draw.line((40 * SCALE, 405 * SCALE, 1160 * SCALE, 405 * SCALE), fill=RULE, width=2 * SCALE)

    margin, gap, card_width = 40, 20, 360
    x_positions = [margin + i * (card_width + gap) for i in range(3)]
    for index, project in enumerate(PROJECTS):
        row, column = divmod(index, 3)
        draw_card(canvas, project, x_positions[column], 418 + row * 147, card_width, mobile=False)

    finish(canvas, ASSETS / "hero-v12.png")


def render_mobile() -> None:
    width, height = 390, 560
    canvas = Image.new("RGBA", (width * SCALE, height * SCALE), INK)
    draw = ImageDraw.Draw(canvas)
    draw.ellipse((285 * SCALE, -95 * SCALE, 470 * SCALE, 90 * SCALE), fill="#1c2d49")
    draw.ellipse((-70 * SCALE, 495 * SCALE, 75 * SCALE, 640 * SCALE), fill="#123447")

    draw_tracked(draw, (17, 13), "INDEPENDENT MAKER · PRACTICAL SOFTWARE",
                 load_font(8, bold=True), MUTED, 1)
    draw_tracked(draw, (12, 31), "LydiaTools", load_font(92, bold=True), WHITE, -12)
    draw.text((19 * SCALE, 141 * SCALE), "Small tools. Clearer next steps.",
              font=load_font(15), fill=TEXT)
    draw_tracked(draw, (19, 164), "6 TOOLS · REAL SCREENS · CLEAR STATUS",
                 load_font(7, bold=True), MUTED, 0)
    draw.line((17 * SCALE, 184 * SCALE, 373 * SCALE, 184 * SCALE), fill=RULE, width=2 * SCALE)

    margin, gap, card_width = 17, 10, 173
    x_positions = [margin, margin + card_width + gap]
    for index, project in enumerate(PROJECTS):
        row, column = divmod(index, 2)
        draw_card(canvas, project, x_positions[column], 192 + row * 120, card_width, mobile=True)

    finish(canvas, ASSETS / "hero-mobile-v12.png")


if __name__ == "__main__":
    render_desktop()
    render_mobile()
    print("Rendered assets/hero-v12.png and assets/hero-mobile-v12.png")
