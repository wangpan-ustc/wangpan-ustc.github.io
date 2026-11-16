import json
import os
import time
from datetime import datetime

import jsonpickle  # noqa: F401  (kept for compatibility with the original template)
from scholarly import scholarly, ProxyGenerator

SCHOLAR_ID = os.environ['GOOGLE_SCHOLAR_ID']
SECTIONS = ['basics', 'indices', 'counts']  # per-paper data is not used by the homepage


def use_proxy():
    """Google Scholar often blocks GitHub Actions IPs, so route through a proxy when available."""
    key = os.environ.get('SCRAPER_API_KEY')
    if key:
        pg = ProxyGenerator()
        if pg.ScraperAPI(key):
            scholarly.use_proxy(pg)
            print('Using ScraperAPI proxy')
            return 'scraperapi'
    return None


def fetch():
    author = scholarly.search_author_id(SCHOLAR_ID)
    scholarly.fill(author, sections=SECTIONS)
    return author


def fetch_with_fallback():
    mode = use_proxy()
    attempts = 3 if mode else 2
    for i in range(attempts):
        try:
            return fetch()
        except Exception as e:  # MaxTriesExceededException etc.
            print(f'Attempt {i + 1} failed: {e!r}')
            time.sleep(30)
    if mode is None:
        print('Direct access failed, trying free proxies')
        pg = ProxyGenerator()
        if pg.FreeProxies():
            scholarly.use_proxy(pg)
            return fetch()
    raise RuntimeError('Cannot fetch Google Scholar data. Set the SCRAPER_API_KEY secret for reliable access.')


author = fetch_with_fallback()
author['updated'] = str(datetime.now())
author.pop('publications', None)
print(json.dumps(author, indent=2, ensure_ascii=False))

os.makedirs('results', exist_ok=True)
with open('results/gs_data.json', 'w') as f:
    json.dump(author, f, ensure_ascii=False)

with open('results/gs_data_shieldsio.json', 'w') as f:
    json.dump({"schemaVersion": 1, "label": "citations", "message": f"{author['citedby']}"}, f, ensure_ascii=False)
