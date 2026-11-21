"""Create one page per highlight in highlights/ from _data/highlights.yml.

Run after adding or renaming a highlight:  python3 scripts/make_highlight_pages.py
Each page is a short stub; the content comes from _data/highlights.yml.
Needs PyYAML if available; falls back to Ruby's YAML otherwise.
"""
import json, os, re, subprocess, unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load():
    path = os.path.join(ROOT, "_data", "highlights.yml")
    try:
        import yaml
        return yaml.safe_load(open(path))
    except ImportError:
        out = subprocess.check_output(["ruby", "-ryaml", "-rjson", "-e",
                                       "puts JSON.dump(YAML.load_file(ARGV[0]))", path])
        return json.loads(out)

def slugify(s):  # matches Jekyll's default slugify
    s = unicodedata.normalize("NFKD", s).lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")

def strip_html(s):
    s = re.sub(r"<[^>]+>", "", s or "")
    return s.replace("&amp;", "&").strip()

made = []
for b in load():
    slug = slugify(b["title"])
    hid = f'{b["date"]}-{slug}' if b.get("date") else slug
    first = (b.get("cards") or [{}])[0]
    image = first.get("poster") if first.get("kind") == "video" else first.get("src")
    desc = strip_html(b.get("lead")) or strip_html(first.get("caption"))
    lines = ["---", "layout: highlight", f'title: {json.dumps(b["title"])}']
    if b.get("date"):
        lines.append(f'date: {b["date"]}')
    if desc:
        lines.append(f"description: {json.dumps(desc)}")
    if image and "://" not in image:
        lines.append(f"share_image: {image}")
    lines.append("---")
    path = os.path.join(ROOT, "highlights", hid + ".html")
    open(path, "w").write("\n".join(lines) + "\n")
    made.append(os.path.relpath(path, ROOT))
print("\n".join(made))
