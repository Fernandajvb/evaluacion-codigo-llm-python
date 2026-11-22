from PIL import Image, ImageDraw, ImageFont
from pathlib import Path


OUT = Path("grafico_hallazgos_seguridad.png")


def get_font(size, bold=False):
    names = [r"C:\Windows\Fonts\arialbd.ttf" if bold else r"C:\Windows\Fonts\arial.ttf"]
    for name in names:
        if Path(name).exists():
            return ImageFont.truetype(name, size)
    return ImageFont.load_default()


image = Image.new("RGB", (1100, 640), "white")
draw = ImageDraw.Draw(image)
title = get_font(30, True)
body = get_font(24)
small = get_font(20)
draw.text((65, 30), "Hallazgos bloqueantes de Semgrep por modelo", font=title, fill="black")

left, top, right, bottom = 120, 120, 1020, 510
draw.line((left, top, left, bottom), fill="black", width=3)
draw.line((left, bottom, right, bottom), fill="black", width=3)
for value in range(0, 10, 2):
    y = bottom - (value / 9) * (bottom - top)
    draw.line((left, y, right, y), fill="#D9D9D9", width=1)
    draw.text((78, y - 12), str(value), font=small, fill="black")

models = ["DeepSeek", "Qwen", "GLM"]
direct = [6, 5, 8]
security = [4, 3, 7]
centers = [280, 570, 860]
for center, model, first, second in zip(centers, models, direct, security):
    scale = (bottom - top) / 9
    x1, x2 = center - 58, center + 12
    y1, y2 = bottom - first * scale, bottom - second * scale
    draw.rectangle((x1, y1, x1 + 52, bottom), fill="#4F81BD")
    draw.rectangle((x2, y2, x2 + 52, bottom), fill="#A6A6A6")
    draw.text((x1 + 14, y1 - 28), str(first), font=small, fill="black")
    draw.text((x2 + 14, y2 - 28), str(second), font=small, fill="black")
    bbox = draw.textbbox((0, 0), model, font=body)
    draw.text((center - (bbox[2] - bbox[0]) / 2, 530), model, font=body, fill="black")

draw.rectangle((360, 575, 382, 597), fill="#4F81BD")
draw.text((392, 572), "Prompt directo", font=small, fill="black")
draw.rectangle((600, 575, 622, 597), fill="#A6A6A6")
draw.text((632, 572), "Prompt de seguridad", font=small, fill="black")
image.save(OUT)
