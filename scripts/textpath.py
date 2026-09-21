from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.misc.transform import Transform

def text_to_path(font_path, text, size, tracking=0.0):
    """Return (svg_path_d, advance_width) with baseline at y=0, y-down coords."""
    f = TTFont(font_path)
    upem = f["head"].unitsPerEm
    scale = size / upem
    cmap = f.getBestCmap()
    gs = f.getGlyphSet()
    hmtx = f["hmtx"]
    pen = SVGPathPen(gs, ntos=lambda v: f"{v:.2f}")
    x = 0.0
    for ch in text:
        gname = cmap.get(ord(ch))
        if gname is None:
            x += size * 0.5 + tracking
            continue
        adv = hmtx[gname][0] * scale
        t = Transform(scale, 0, 0, -scale, x, 0)
        gs[gname].draw(TransformPen(pen, t))
        x += adv + tracking
    return pen.getCommands(), x

if __name__ == "__main__":
    import sys, json
    d, w = text_to_path(sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4]))
    print(json.dumps({"d": d, "w": round(w, 2)}))
