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
