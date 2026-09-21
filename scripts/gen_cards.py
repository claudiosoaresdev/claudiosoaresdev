import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from textpath import text_to_path

FONT = "/Users/claudiosoares/www/claudiosoaresdev/portfolio/assets/fonts/Orbitron-Bold.ttf"
W, H = 800, 450
M = 40

def t(s, size, tr): return text_to_path(FONT, s, size, tr)

def palette(dark):
    if dark:
        return dict(bg="#0A0A0A", fg="#F2F2F0", accent="#A9FE00", muted="#C9C7BB", chip="#A9FE0014")
    return dict(bg="#F2F2F0", fg="#0A0A0A", accent="#7CBA00", muted="#55554E", chip="#7CBA0014")

def grid(accent):
    p = [f'<g stroke="{accent}" stroke-width="1" opacity="0.05">']
    for x in range(0, W + 1, 40): p.append(f'<line x1="{x}" y1="0" x2="{x}" y2="{H}"/>')
    for y in range(0, H + 1, 40): p.append(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}"/>')
    p.append("</g>")
    return "".join(p)

def brackets(accent):
    a = 26
    out = []
    for (x, y, dx, dy) in [(M, M, 1, 1), (W - M, M, -1, 1), (M, H - M, 1, -1), (W - M, H - M, -1, -1)]:
        out.append(f'<path d="M{x} {y+dy*a} L{x} {y} L{x+dx*a} {y}" fill="none" stroke="{accent}" stroke-width="2" opacity="0.5"/>')
    return "".join(out)

def chips(items, x, y, c):
    out, cx = [], x
    for it in items:
        d, w = t(it, 11, 2.2)
        bw = w + 26
        out.append(f'<rect x="{cx:.1f}" y="{y-16}" width="{bw:.1f}" height="24" rx="4" fill="{c["chip"]}" stroke="{c["accent"]}" stroke-opacity="0.35"/>')
        out.append(f'<g transform="translate({cx+13:.1f} {y})" fill="{c["accent"]}" opacity="0.95"><path d="{d}"/></g>')
        cx += bw + 10
    return "".join(out)

def schematic_auth(c):
    a, m = c["accent"], c["muted"]
    boxes = [("CLIENT", 70), ("API", 330), ("DB", 590)]
    out = [f'<g opacity="0.85">']
    for label, x in boxes:
        d, w = t(label, 11, 2)
        out.append(f'<rect x="{x}" y="330" width="140" height="52" rx="6" fill="none" stroke="{a}" stroke-opacity="0.45" stroke-width="1.5"/>')
        out.append(f'<g transform="translate({x + 70 - w/2:.1f} 361)" fill="{m}"><path d="{d}"/></g>')
    for x0 in (210, 470):
        out.append(f'<line x1="{x0}" y1="356" x2="{x0+120}" y2="356" stroke="{a}" stroke-opacity="0.3" stroke-dasharray="4 5"/>')
        out.append(f'<circle cy="356" r="4" fill="{a}"><animate attributeName="cx" values="{x0};{x0+120}" dur="2.2s" repeatCount="indefinite"/><animate attributeName="opacity" values="0;1;0" dur="2.2s" repeatCount="indefinite"/></circle>')
    out.append("</g>")
    return "".join(out)

def schematic_sync(c):
    a, m = c["accent"], c["muted"]
    out = [f'<g opacity="0.85">']
    out.append(f'<rect x="70" y="326" width="180" height="60" rx="6" fill="none" stroke="{a}" stroke-opacity="0.45" stroke-width="1.5"/>')
    d, w = t("SNAPSHOT", 11, 2)
    out.append(f'<g transform="translate({160 - w/2:.1f} 361)" fill="{m}"><path d="{d}"/></g>')
    out.append(f'<rect x="530" y="326" width="200" height="60" rx="6" fill="none" stroke="{a}" stroke-opacity="0.45" stroke-width="1.5"/>')
    d2, w2 = t("OFFLINE CLIENT", 11, 2)
    out.append(f'<g transform="translate({630 - w2/2:.1f} 361)" fill="{m}"><path d="{d2}"/></g>')
    d3, w3 = t("DELTA", 10, 2)
    out.append(f'<g transform="translate({390 - w3/2:.1f} 338)" fill="{a}" opacity="0.9"><path d="{d3}"/></g>')
    out.append(f'<line x1="256" y1="356" x2="524" y2="356" stroke="{a}" stroke-opacity="0.3" stroke-dasharray="4 5"/>')
    for delay in ("0s", "0.7s", "1.4s"):
        out.append(f'<circle cy="356" r="4" fill="{a}"><animate attributeName="cx" values="256;524" dur="2.1s" begin="{delay}" repeatCount="indefinite"/><animate attributeName="opacity" values="0;1;0" dur="2.1s" begin="{delay}" repeatCount="indefinite"/></circle>')
    out.append("</g>")
    return "".join(out)

CARDS = {
    "card-auth": dict(index="// 03", title="AUTH API TEMPLATE",
                      tagline="JWT RS256, REFRESH ROTATION, EMAIL VERIFICATION",
                      chips=["NESTJS", "PRISMA", "REDIS", "VITEST E2E"], schematic=schematic_auth),
    "card-sync": dict(index="// 04", title="OFFLINE-FIRST SYNC",
                      tagline="SNAPSHOT + DELTA, SERVER-SIDE REPRICING, SSE REPLAY",
                      chips=["NESTJS", "POSTGRES", "SSE", "PRISMA"], schematic=schematic_sync),
}

def build(spec, dark):
    c = palette(dark)
    idx_d, _ = t(spec["index"], 12, 4)
    title_d, _ = t(spec["title"], 30, 2.5)
    tag_d, _ = t(spec["tagline"], 12, 2)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{spec["title"]}">
  <title>{spec["title"]}</title>
  <rect width="{W}" height="{H}" fill="{c["bg"]}"/>
  {grid(c["accent"])}
  {brackets(c["accent"])}
  <g transform="translate({M + 20} {M + 52})" fill="{c["accent"]}" opacity="0.85"><path d="{idx_d}"/></g>
  <g transform="translate({M + 20} {M + 110})" fill="{c["fg"]}"><path d="{title_d}"/></g>
  <g transform="translate({M + 20} {M + 148})" fill="{c["muted"]}" opacity="0.8"><path d="{tag_d}"/></g>
  <line x1="{M + 20}" y1="{M + 178}" x2="{W - M - 20}" y2="{M + 178}" stroke="{c["accent"]}" stroke-opacity="0.2"/>
  {chips(spec["chips"], M + 20, M + 216, c)}
  {spec["schematic"](c)}
</svg>
'''

if __name__ == "__main__":
    import pathlib, sys
    out = pathlib.Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
    for name, spec in CARDS.items():
        (out / f"{name}-dark.svg").write_text(build(spec, True))
        (out / f"{name}-light.svg").write_text(build(spec, False))
    print("cards written")
