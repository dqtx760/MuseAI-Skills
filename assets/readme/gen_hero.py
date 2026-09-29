#!/usr/bin/env python3
# Generate assets/readme/hero.svg for the MuseAI-Skills README.
# Pure SVG (no raster, no external fonts). Self-contained dark banner.
import math, xml.sax.saxutils as su

W, H = 1200, 380
cx, cy = 892, 196          # center of the skill-graph (right panel)
R = 142                    # orbit radius for category nodes
node_r = 27                # category node radius

# (label, color) -- 10 categories that sum to 68 skills
cats = [
    ("工作流", "#8b5cf6"),
    ("文档",   "#6366f1"),
    ("旅行",   "#0ea5e9"),
    ("办公",   "#14b8a6"),
    ("社交",   "#f59e0b"),
    ("购物",   "#ec4899"),
    ("健康",   "#22c55e"),
    ("音视频", "#a855f7"),
    ("设备",   "#f97316"),
    ("产品",   "#e2e8f0"),
]

parts = []
parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
             f'width="100%" role="img" font-family="-apple-system,BlinkMacSystemFont,'
             f'&quot;Segoe UI&quot;,Roboto,&quot;PingFang SC&quot;,&quot;Microsoft YaHei&quot;,sans-serif">')
parts.append('<title>MuseAI-Skills · muse.ai 技能与 Hatch 运行环境非官方存档（68 技能 / 40 权限清单 / 12 评测场景）</title>')

# defs
parts.append('<defs>')
parts.append('<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">'
             '<stop offset="0" stop-color="#0b1020"/>'
             '<stop offset="1" stop-color="#141d33"/></linearGradient>')
parts.append('<linearGradient id="hub" x1="0" y1="0" x2="1" y2="1">'
             '<stop offset="0" stop-color="#a78bfa"/>'
             '<stop offset="1" stop-color="#7c3aed"/></linearGradient>')
parts.append('<radialGradient id="glow" cx="0.5" cy="0.5" r="0.5">'
             '<stop offset="0" stop-color="#7c3aed" stop-opacity="0.30"/>'
             '<stop offset="1" stop-color="#7c3aed" stop-opacity="0"/></radialGradient>')
parts.append('</defs>')

# background
parts.append(f'<rect x="0" y="0" width="{W}" height="{H}" rx="18" fill="url(#bg)"/>')
# subtle depth circle behind graph
parts.append(f'<circle cx="{cx}" cy="{cy}" r="176" fill="url(#glow)"/>')

# ---- Left panel ----
parts.append(f'<text x="44" y="66" fill="#94a3b8" font-size="15" letter-spacing="2">'
             'MUSE.AI · 技能文档与 HATCH 运行环境</text>')
parts.append(f'<text x="42" y="132" fill="#f8fafc" font-size="62" font-weight="800">'
             'MuseAI-Skills</text>')
parts.append(f'<text x="44" y="172" fill="#cbd5e1" font-size="22">'
             'muse.ai 技能与运行环境的非官方存档</text>')
parts.append(f'<text x="44" y="206" fill="#94a3b8" font-size="16">'
             '68 个随包技能 · 40 份权限清单 · 12 份评测场景 · 仅供技术研究</text>')

# stat chips
chips = [("68", "随包技能"), ("40", "权限清单"), ("12", "评测场景")]
chip_w, chip_h, gap = 156, 46, 14
x0 = 44
y0 = 244
for i, (big, small) in enumerate(chips):
    x = x0 + i * (chip_w + gap)
    parts.append(f'<rect x="{x}" y="{y0}" width="{chip_w}" height="{chip_h}" rx="11" '
                 f'fill="#16213a" stroke="#2c3a5c"/>')
    parts.append(f'<text x="{x+18}" y="{y0+30}" fill="#f8fafc" font-size="22" font-weight="700">{big}</text>')
    parts.append(f'<text x="{x+48}" y="{y0+29}" fill="#94a3b8" font-size="15">{small}</text>')

# official-archive pill
px, py, pw, ph = 44, 312, 250, 32
parts.append(f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="16" fill="#1b1326" stroke="#6d28d9"/>')
parts.append(f'<circle cx="{px+18}" cy="{py+ph/2}" r="5" fill="#a78bfa"/>')
parts.append(f'<text x="{px+32}" y="{py+21}" fill="#c4b5fd" font-size="15">非官方存档 · Unofficial Archive</text>')

# ---- Right panel: skill graph ----
# connecting lines first (under nodes)
for i, (label, color) in enumerate(cats):
    ang = math.radians(-90 + i * 36)
    nx = cx + R * math.cos(ang)
    ny = cy + R * math.sin(ang)
    parts.append(f'<line x1="{cx}" y1="{cy}" x2="{nx:.1f}" y2="{ny:.1f}" '
                 f'stroke="#475569" stroke-width="1.4" opacity="0.55"/>')

# central hub
parts.append(f'<circle cx="{cx}" cy="{cy}" r="48" fill="url(#hub)"/>')
parts.append(f'<circle cx="{cx}" cy="{cy}" r="48" fill="none" stroke="#c4b5fd" stroke-opacity="0.5"/>')
parts.append(f'<text x="{cx}" y="{cy-2}" fill="#ffffff" font-size="26" font-weight="800" '
             f'text-anchor="middle">Muse</text>')
parts.append(f'<text x="{cx}" y="{cy+20}" fill="#ede9fe" font-size="13" '
             f'text-anchor="middle" opacity="0.9">muse.ai</text>')

# category nodes
for i, (label, color) in enumerate(cats):
    ang = math.radians(-90 + i * 36)
    nx = cx + R * math.cos(ang)
    ny = cy + R * math.sin(ang)
    parts.append(f'<circle cx="{nx:.1f}" cy="{ny:.1f}" r="{node_r}" fill="{color}" '
                 f'stroke="#0b1020" stroke-width="2"/>')
    parts.append(f'<text x="{nx:.1f}" y="{ny+6:.1f}" fill="#0b1020" font-size="18" '
                 f'font-weight="700" text-anchor="middle">{label}</text>')

# caption
parts.append(f'<text x="{cx}" y="{H-20}" fill="#64748b" font-size="14" text-anchor="middle">'
             '中心为 Muse，外圈为 10 类共 68 个随包技能</text>')

parts.append('</svg>')

svg = "\n".join(parts)
with open("assets/readme/hero.svg", "w", encoding="utf-8") as f:
    f.write(svg)

# validate
import xml.dom.minidom as md
md.parseString(svg)
print("hero.svg written, bytes:", len(svg.encode("utf-8")))
