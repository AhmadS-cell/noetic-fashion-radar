"""Keep published radar data, approved layout, order and noindex intact."""
import pathlib,re,json,hashlib,html
root=pathlib.Path(__file__).parent
BASELINE_IDS = ['DercOXfKWDG', 'DexXn0rRDsP', '7696965067044080928', 'DegX2mTpV79', '7697010851466857746', 'DepH3P0KGjQ', '7698422243881127186', 'Demlf58iAxl', 'DenFmDGxClU', 'DerOfNgT0XQ', 'DesFblBz1l8', 'DeoO0TSTFc4', 'DehWZhnI9nq', 'DemzzUTiKev', 'Depg1RrqBd6', 'DevVxCkHLEE', 'Dewkn8bDNfN', 'DdO5Po0MQu7', 'DePff2jxou8', 'DeVe3n-JbbN', 'DeXX4uujSFa', 'DdG4upPsyqR', 'Demdhx0tIF-', 'DeuJHsLIalo', 'Dehi7Lusqum', '7699076619893214484', 'DemE3GfzqrH', 'Dev9qPAsY5c', 'DewYDguTFy1', 'DYpJ4S-NRc2', 'DeZOCeSs-AB', 'Dee6fCdR52a', 'DeZ0AsrxDug', 'DePjXYAMPQQ', 'DecRj_SMkd2', 'DeZKS0pKvQg', 'DeZjuhnMUJq', 'Dd8zh6bsZXR', 'Dd1rDpiN0-i', 'DeQVR8TJnlt', 'DeXCUp8v0Jj', '7696850780610891016', '7698085974114372885', '7697259771950304532', '7699205183909235988', '7696915975639141653', 'DekX6COqTSL', 'Deq7KyqRV5a', '7698118468998302996', 'Derv6l0K6Og', 'DenMKCiql80', 'DerrOIBxwGz', 'Der7RyixLX-', 'DewyRdNNd6k', 'DetpHYVq9eP', 'DenKJi9Kbl9', 'DetkPCctwGN', 'Dewv-KfK-5a', 'DeuiyJKROKl', 'Dev8v0-R0oZ', '7697513773837470984', 'DeuTVt7xAk-', '7698408167146917126', '7698426769564601608', '7697736969564032257', '7698309537907985665', '7698688374848130305', '7698788288655658292', '7698450269876653364', '7698804785524264212', '7696965372230012180', '7698812244653509909', '7696890441085488406', '7696800468428688662', 'DelxMTzzoxt', '7697414859515890966', '7697399954863656205', '7698871969298566422', '7698281874640162068', '7698278704803269908', '7699097074234608918', '7698839523651865889', '7698027931955711254', 'Dexzo4UJMjr', '7698032236070800672', '7698361662243376416', '7698671822421724468', '7698860890770230559', '7697744187889929504', '7697592446707830048', '7697619003665059080', '7697730815173725472', '7698877276800208141', '7699203136312855829', '7698086971666713857', 'DehDUxHN61b', 'DepCi-AtcRV', 'DXmh76-jY9f', 'DYsg-4nRRH3', 'DXlwCqJjVPa', 'DeW1Tc3KDqy', 'Dec6dNMKCFg', 'DebXPrEzhog', 'Def5pOozgTo', 'DecN8PJNHHf', '7697229322251259157', '7697718939979173121', '7697019417078598930', '7697200544888147216', '7696877762975436050', '7697935679262657810', '7699111608206773525', '7696885821978316040', '7696990665988836629', '7697939609413635336', '7698154811228704007', '7697717567795809556', '7697981896608861460', '7697561351090228532', '7697707550556294407', '7699059180849712405', '7698712700255243541', '7698526947713764621', '7699090608467578130', '7696959054266027285', '7698423341828279573', '7698795884582161695', '7698127193511120135', '7698824251507363124', '7698451239058623796', '7697690130198400276', '7697630839273819412', '7697524454833818897', '7699087506477681928', '7699117436116798741', 'Dek7tLhJpUt', 'DepBdpFxrbC', '7697377681511402770', '7697558449420242192', '7698154913540361494', '7696914645398899975', '7696914921484766482', '7698231766892547359', 'Ddl3toUoLPp', 'DecSymliD8d', 'DUWR8yggvDB', 'C20FoqHMxte', 'DOLXOnyiE5m', 'DaCnvfJtUMI', 'DSRziKODQyf', 'DcgVQnfjJys', 'DdMsqzFsXOb', 'DZ-qzASq_r-', 'DUtN8-4jDle', 'DFdkUL6Ou8E', 'Db2iPflAT0w', 'DWa07rSDE0p', '7700276024960879879', 'De7FDRtI5rt', 'DeyqHyusQFi', '7699314116334226706', 'DeypocoR7dp', 'De6rPA2RbgV', 'De6_1UvJgD0', 'De2C3xbisU8', 'De4rkJAxzuA', 'De7WX4lRnh7']
BASELINE_RECOMMENDATIONS = ['DerOfNgT0XQ', 'DesFblBz1l8', 'DeXX4uujSFa', 'DeVe3n-JbbN', 'DercOXfKWDG', '7696965067044080928', 'DegX2mTpV79', 'DexXn0rRDsP', '7700276024960879879', 'De7FDRtI5rt']
BASELINE_TRIAL_HASHES = ['62e302a53ef4319897145a9b70d9e7156e41750e07bcee08aad1e8f7bd8fd10a', '48eef57ea333540b90827be3c8568eb89527f2cc6a8bf6477a93382faa5caeec', '037145a9275b6749f672b5f292f38ce371799a4634fc9dd937baea64515d3506', 'd656ce950858e36bb423dabd786619a256e11158ecc20520365d8dd5d0d22692']
APPROVED_CSS_HASH = '9be76a5fdc645eb0e9324ea6886c65b3c97749b6ed4e30fc0750f8687e96df3b'
pages=list(root.rglob('*.html'))
assert pages,'No served HTML'
for path in pages:
    content=path.read_text(encoding='utf-8')
    assert re.search(r'<meta[^>]+name=["\x27]robots["\x27][^>]+content=["\x27][^"\x27]*noindex',content,re.I),f'Missing noindex: {path}'
    assert not re.search(r'src=["\x27](?:media/|[^"\x27]+\.mp4)',content,re.I),f'Hosted video: {path}'
assert not list(root.rglob('*.mp4')),'Do not publish MP4 downloads'
assert not (root/'robots.txt').exists(),'Keep noindex documents crawlable'
for folder in [root,root/'docs']:
    page=(folder/'index.html').read_text(encoding='utf-8')
    assert all(x not in page for x in ['نواتك','نوايتك','نوتك']),'Incorrect Arabic brand spelling'
    rows=json.loads(re.search(r'const REELS = (\[.*?\]);\n',page,re.S)[1])
    ids=[x['id'] for x in rows]
    assert len(ids)==len(set(ids)) and len(ids)>=len(BASELINE_IDS)
    assert ids[:len(BASELINE_IDS)]==BASELINE_IDS,'Saved library IDs or order changed'
    assert all(x['displayOrder']==i for i,x in enumerate(rows)),'Default display order changed'
    assert 'a.displayOrder-b.displayOrder' in page,'Default sort must preserve card order'
    css=re.search(r'<style>(.*?)</style>',page,re.S)[1]
    assert hashlib.sha256(css.encode()).hexdigest()==APPROVED_CSS_HASH,'Approved Noetic design changed'
    recs=re.findall(r'class="recommended-card" id="recommended-([^"]+)"',page)
    assert recs[:len(BASELINE_RECOMMENDATIONS)]==BASELINE_RECOMMENDATIONS,'Recommendations removed/reordered'
    trials=re.findall(r'<article class="trial-card".*?</article>',page,re.S)
    assert [hashlib.sha256(x.encode()).hexdigest() for x in trials[:len(BASELINE_TRIAL_HASHES)]]==BASELINE_TRIAL_HASHES,'Saved experiments changed'
    lookup={x['id']:x for x in rows}
    for markup in re.findall(r'<article class="recommended-card".*?</article>',page,re.S):
        ident=re.search(r'id="recommended-([^"]+)"',markup)[1]
        values=re.findall(r'<div class="metric"><b>(.*?)</b>',markup)
        row=lookup[ident]
        assert html.unescape(values[0])==str(row['viewsDisplay']),f'Stale recommendation views: {ident}'
        assert html.unescape(values[1])==str(row['comments'] if row['comments'] is not None else 'غير متاح'),f'Stale recommendation comments: {ident}'
    assert re.search(r'<section[^>]*id="decisions"[^>]*>.*?TESTING / PENDING APPROVAL',page,re.S),'Experiment status lost'
    assert not re.search(r'https://[^" ]*(?:tiktokcdn|fbcdn|cdninstagram)',page),'Temporary signed media URL published'
    assert '@media(max-width:1199px){.video-grid{grid-template-columns:repeat(2,minmax(0,1fr))}}' in page
    assert all('id="'+x+'"' in page for x in ['platform','collection','review','market'])
assert (root/'index.html').read_bytes()==(root/'docs'/'index.html').read_bytes(),'Published copies differ'
print(f'PASS: {len(pages)} noindex routes, {len(rows)} retained/unique references, saved order/design/trials and current recommendation metrics.')
