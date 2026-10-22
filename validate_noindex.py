import pathlib,re,hashlib
root=pathlib.Path(__file__).parent
pages=list(root.rglob('*.html'))
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
    assert len(rows)==157 and len({r['id'] for r in rows})==157
    assert len({r['brand'] for r in rows})>=10
    assert sum(r['collection']=='new' for r in rows)==69
    assert sum(r['collection']=='saved' for r in rows)==88
    saved_ids='\n'.join(sorted(r['id'] for r in rows if r['collection']=='saved'))
    assert hashlib.sha256(saved_ids.encode()).hexdigest()=='c5a0bf9436128bfa7021f729d1f60cf184744236240cfb0896e152f8316908b8', 'Saved references changed'
    original_css=re.search(r'<style>(.*?)</style>',page,re.S).group(1)[:16832]
    assert hashlib.sha256(original_css.encode()).hexdigest()=='5c988b27fef6b2d2e5d822be4f853a854ba66a32ff91da7b806480afc91e5c1a', 'Approved Noetic design changed'
    assert {r['platform'] for r in rows}=={'instagram','tiktok'}
    assert page.count('class="recommended-card"')==8 and page.count('class="trial-card"')==4
    for code in ['DerOfNgT0XQ','DesFblBz1l8','DeXX4uujSFa','DeVe3n-JbbN']:assert 'id="recommended-'+code+'"' in page
    for p in folder.glob('*.html'):
        text=p.read_text(encoding='utf-8')
        assert '\u0646\u0648\u0627\u062a\u0643' not in text and '\u0646\u0648\u062a\u0643' not in text
    assert not re.search(r'https://[^" ]*(?:tiktokcdn|fbcdn|cdninstagram)',page), 'Transient CDN URL published'
    assert all('id="'+field+'"' in page for field in ['platform','collection','review','market'])
    assert '@media(max-width:1199px){.video-grid{grid-template-columns:repeat(2,minmax(0,1fr))}}' in page, 'Tablet library must have two columns'
print('PASS: 157 references, 88 saved + 69 discoveries, original four recommendations + four candidates, four experiments and Arabic spelling.')


BASELINE_IDS = ['DYpJ4S-NRc2', 'Dd1rDpiN0-i', 'Dd8zh6bsZXR', 'DdO5Po0MQu7', 'Ddl3toUoLPp', 'DePff2jxou8', 'DePjXYAMPQQ', 'DeQVR8TJnlt', 'DeVe3n-JbbN', 'DeXCUp8v0Jj', 'DeXX4uujSFa', 'DeZ0AsrxDug', 'DeZOCeSs-AB', 'DeZjuhnMUJq', 'DecRj_SMkd2', 'Dee6fCdR52a', 'Dehi7Lusqum', 'Dek7tLhJpUt', 'DemE3GfzqrH', 'Demdhx0tIF-', 'Demlf58iAxl', 'DemzzUTiKev', 'DeoO0TSTFc4', 'DepBdpFxrbC', 'Depg1RrqBd6', 'DerOfNgT0XQ', 'DesFblBz1l8', 'DeuJHsLIalo', 'Dev9qPAsY5c', 'DevVxCkHLEE', 'DewYDguTFy1', 'Dewkn8bDNfN']
assert set(BASELINE_IDS)<=set(r["id"] for r in rows), "Previously published references were removed"
