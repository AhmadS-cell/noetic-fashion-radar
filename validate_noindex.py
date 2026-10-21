import pathlib,re
root=pathlib.Path(__file__).parent
pages=list(root.glob('*.html'))
assert pages, 'No served HTML documents'
for p in pages:
    text=p.read_text(encoding='utf-8')
    assert re.search(r'<meta[^>]+name=["\']robots["\'][^>]+content=["\'][^"\']*noindex', text, re.I), f'Missing noindex: {p}'
    assert not re.search(r'src=["\'](?:media/|[^"\']+\.mp4)',text,re.I), f'Unexpected hosted video: {p}'
assert not list(root.rglob('*.mp4')), 'Do not publish MP4 downloads on GitHub Pages'
assert not (root/'robots.txt').exists(), 'Keep noindex documents crawlable'
print(f'PASS: noindex on all {len(pages)} served HTML documents; no hosted MP4 downloads.')
import json
for folder in [root,root/'docs']:
    if not (folder/'index.html').exists():continue
    page=(folder/'index.html').read_text(encoding='utf-8')
    assert '\u0646\u0648\u0627\u062a\u0643' not in page and '\u0646\u0648\u062a\u0643' not in page, 'Incorrect Arabic brand spelling'
    rows=json.loads(re.search(r'const REELS = (\[.*?\]);\n',page,re.S).group(1))
    assert len(rows)==32 and len({r['id'] for r in rows})==32
    assert len({r['brand'] for r in rows})==8
    assert page.count('class="recommended-card"')==4 and page.count('class="trial-card"')==4
    for code in ['DerOfNgT0XQ','DesFblBz1l8','DeXX4uujSFa','DeVe3n-JbbN']:assert 'id="recommended-'+code+'"' in page
    for p in folder.glob('*.html'):
        text=p.read_text(encoding='utf-8')
        assert '\u0646\u0648\u0627\u062a\u0643' not in text and '\u0646\u0648\u062a\u0643' not in text
print('PASS: 32 videos, 8 brands, original three plus fourth recommendation, four experiments and Arabic spelling.')
