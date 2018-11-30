import requests, csv
from bs4 import BeautifulSoup

V8_URL = "https://bugs.chromium.org/p/v8/issues/list"
BASE = "https://bugs.chromium.org/"
all_issues = "https://bugs.chromium.org/p/v8/issues/list?can=1&q=wasm&colspec=ID+Type+Status+Priority+Owner+Summary+HW+OS+Component+Stars&x=priority&y=owner&cells=ids&start={}"
V8_WASM_COMPONENT = "https://bugs.chromium.org/p/v8/issues/list?q=component:WebAssembly"

def get_all_issues_by_engine(engine, url):
    if engine not in ['v8', 'jsc', 'sm', 'ch']:
        raise Exception('Error: invalid engine <{}>'.format(engine))
    
    req = requests.get(url)
    html_text = req.text

    soup = BeautifulSoup(html_text, "html.parser")

    return soup

def save_csv(data, csv_name):
    field_names = ['bug_tracker', 'issue name', 'issue_url']
    with open('{}.csv'.format(csv_name), 'w') as doc:
        doc = csv.DictWriter(doc, fieldnames=field_names)
        for line in data:
            row = {"bug_tracker": line["bug_tracker"], "issue_name": line["issue_name"], "bug_tracker": line["issue_url"]}
            doc.writerow(row)
