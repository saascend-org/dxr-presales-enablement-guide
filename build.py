#!/usr/bin/env python3
"""Builds build/index.plain.html for the Pre-Sales enablement guide (XYP-PRESALES-001).

Source of truth is the artifact page: ../build/presales/guide/pre-sales-guide.html with its
images in ../build/presales/guide/pub/img/. This wraps it as a full document, inlines every image
as a data URI (so the screenshots only ever exist inside the encrypted payload), drops lazy loading
(images written by document.write never trigger it) and adds Mermaid for the process diagram,
which the artifact viewer rendered natively but GitHub Pages does not.

NEVER commit build/index.plain.html: it is the readable guide. publish.sh encrypts it into index.html.
"""
import base64, pathlib, re

HERE = pathlib.Path(__file__).parent
SRC = HERE.parent / 'build' / 'presales' / 'guide' / 'pre-sales-guide.html'
IMG = HERE.parent / 'build' / 'presales' / 'guide' / 'pub' / 'img'
OUT = HERE / 'build' / 'index.plain.html'

body = SRC.read_text()

def inline(m):
    f = IMG / pathlib.Path(m.group(1)).name
    mime = 'image/png' if f.suffix == '.png' else 'image/jpeg'
    return 'src="data:%s;base64,%s"' % (mime, base64.b64encode(f.read_bytes()).decode())

body, n = re.subn(r'src="img/([^"]+)"', inline, body)
body = body.replace(' loading="lazy"', '')
mermaid = ('<script src="https://cdn.jsdelivr.net/npm/mermaid@10.9.1/dist/mermaid.min.js"></script>\n'
           '<script>mermaid.initialize({startOnLoad:true,theme:window.matchMedia("(prefers-color-scheme: dark)").matches?"dark":"neutral"});</script>')
doc = ('<!doctype html>\n<html lang="en-GB">\n<head>\n<meta charset="utf-8">\n'
       '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
       '<meta name="robots" content="noindex,nofollow,noarchive,nosnippet">\n'
       + body.replace('</style>', '</style>\n</head>\n<body>', 1)
       + '\n' + mermaid + '\n</body>\n</html>\n')
OUT.parent.mkdir(exist_ok=True)
OUT.write_text(doc)
print(f'inlined {n} images -> {OUT} ({OUT.stat().st_size // 1024} KB)')
