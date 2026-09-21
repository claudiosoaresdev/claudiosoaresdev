import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from textpath import text_to_path

FONT = "/Users/claudiosoares/www/claudiosoaresdev/portfolio/assets/fonts/Orbitron-Bold.ttf"
W, H = 1200, 260
M = 44  # margin

def t(text, size, tracking):
    return text_to_path(FONT, text, size, tracking)

NAME = "CLAUDIO SOARES"
EYEBROW = "// SOFTWARE ENGINEER"
STACK = "ANDROID / IOS / KOTLIN MULTIPLATFORM / FLUTTER / NODE.JS"
LEFT = "SÃO PAULO / BR"
RIGHT = "06 YRS / MOBILE + BACKEND"

def grid(accent):
    parts = [f'<g stroke="{accent}" stroke-width="1" opacity="0.05">']
    for x in range(0, W + 1, 48):
        parts.append(f'<line x1="{x}" y1="0" x2="{x}" y2="{H}"/>')
    for y in range(0, H + 1, 48):
        parts.append(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}"/>')
    parts.append("</g>")
    return "".join(parts)

def brackets(accent):
    a, o = 30, 0.55
    c = []
    for (x, y, dx, dy) in [(M, M, 1, 1), (W - M, M, -1, 1), (M, H - M, 1, -1), (W - M, H - M, -1, -1)]:
        c.append(
            f'<path d="M{x} {y + dy * a} L{x} {y} L{x + dx * a} {y}" fill="none" '
            f'stroke="{accent}" stroke-width="2" opacity="{o}"/>'
        )
    return "".join(c)

def ticks(accent):
    """Small readout ticks on the left and right rails."""
    c = []
    for i in range(9):
        y = 66 + i * 16
        ln = 14 if i % 3 == 0 else 7
        op = 0.5 if i % 3 == 0 else 0.22
        c.append(f'<line x1="{M - 20}" y1="{y}" x2="{M - 20 + ln}" y2="{y}" stroke="{accent}" stroke-width="2" opacity="{op}"/>')
        c.append(f'<line x1="{W - M + 20}" y1="{y}" x2="{W - M + 20 - ln}" y2="{y}" stroke="{accent}" stroke-width="2" opacity="{op}"/>')
    return "".join(c)

def build(dark=True):
    if dark:
        bg, name_c, accent, muted = "#0A0A0A", "#F2F2F0", "#A9FE00", "#C9C7BB"
        scan_op, glow_op = "0.10", "0.55"
    else:
        bg, name_c, accent, muted = "#F2F2F0", "#0A0A0A", "#7CBA00", "#55554E"
        scan_op, glow_op = "0.14", "0.45"

    name_d, name_w = t(NAME, 58, 5)
    eye_d, eye_w = t(EYEBROW, 13, 5.5)
    stack_d, stack_w = t(STACK, 13, 3.2)
    left_d, _ = t(LEFT, 10, 3)
    right_d, right_w = t(RIGHT, 10, 3)

    cx = W / 2
    name_x, name_y = cx - name_w / 2, 150
    eye_x, eye_y = cx - eye_w / 2, 92
    stack_x, stack_y = cx - stack_w / 2, 196
    rule_y = 170

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Claudio Soares — Software Engineer">
  <title>Claudio Soares — Software Engineer</title>
  <defs>
    <linearGradient id="scan" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="{accent}" stop-opacity="0"/>
      <stop offset="50%" stop-color="{accent}" stop-opacity="{scan_op}"/>
      <stop offset="100%" stop-color="{accent}" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="rule" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{accent}" stop-opacity="0"/>
      <stop offset="50%" stop-color="{accent}" stop-opacity="{glow_op}"/>
      <stop offset="100%" stop-color="{accent}" stop-opacity="0"/>
    </linearGradient>
    <radialGradient id="vig" cx="50%" cy="46%" r="72%">
      <stop offset="60%" stop-color="{bg}" stop-opacity="0"/>
      <stop offset="100%" stop-color="{bg}" stop-opacity="0.85"/>
    </radialGradient>
    <clipPath id="frame"><rect x="0" y="0" width="{W}" height="{H}"/></clipPath>
  </defs>

  <rect width="{W}" height="{H}" fill="{bg}"/>
  {grid(accent)}

  <g clip-path="url(#frame)">
    <rect x="0" y="-70" width="{W}" height="70" fill="url(#scan)">
      <animate attributeName="y" from="-70" to="{H}" dur="7s" repeatCount="indefinite"/>
    </rect>
  </g>

  <rect width="{W}" height="{H}" fill="url(#vig)"/>
  {brackets(accent)}
  {ticks(accent)}

  <g transform="translate({eye_x} {eye_y})" fill="{accent}" opacity="0.9">
    <path d="{eye_d}"/>
  </g>

  <g transform="translate({name_x} {name_y})" fill="{name_c}">
    <path d="{name_d}"/>
  </g>

  <g>
    <line x1="{M + 40}" y1="{rule_y}" x2="{W - M - 40}" y2="{rule_y}" stroke="{accent}" stroke-width="1" opacity="0.22"/>
    <rect x="{M + 40}" y="{rule_y - 1}" width="220" height="2" fill="url(#rule)">
      <animate attributeName="x" values="{M + 40};{W - M - 260};{M + 40}" dur="9s" repeatCount="indefinite" calcMode="spline" keyTimes="0;0.5;1" keySplines="0.4 0 0.2 1;0.4 0 0.2 1"/>
    </rect>
  </g>

  <g transform="translate({stack_x} {stack_y})" fill="{muted}">
    <path d="{stack_d}"/>
  </g>

  <g transform="translate({M + 16} {H - 22})" fill="{muted}" opacity="0.75">
    <path d="{left_d}"/>
  </g>
  <circle cx="{M + 2}" cy="{H - 26}" r="3.5" fill="{accent}">
    <animate attributeName="opacity" values="1;0.15;1" dur="2.4s" repeatCount="indefinite"/>
  </circle>

  <g transform="translate({W - M - right_w} {H - 22})" fill="{muted}" opacity="0.75">
    <path d="{right_d}"/>
  </g>
</svg>
'''

if __name__ == "__main__":
    import pathlib, sys
    out = pathlib.Path(sys.argv[1])
    out.mkdir(parents=True, exist_ok=True)
    (out / "header-dark.svg").write_text(build(True))
    (out / "header-light.svg").write_text(build(False))
    print("written", out)
