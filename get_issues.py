import requests, csv
from bs4 import BeautifulSoup

V8_URL = "https://bugs.chromium.org/p/v8/issues/list"
BASE = "https://bugs.chromium.org"
V8_wasm = "https://bugs.chromium.org/p/v8/issues/list?can=1&q=wasm&colspec=ID+Type+Status+Priority+Owner+Summary+HW+OS+Component+Stars&x=priority&y=owner&num=10000&cells=ids"
V8_WASM_COMPONENT = "https://bugs.chromium.org/p/v8/issues/list?q=component:WebAssembly"

def get_all_issues_by_engine(engine, url):
    if engine not in ['v8', 'jsc', 'sm', 'ch']:
        raise Exception('Error: invalid engine <{}>'.format(engine))  
    
    soup = to_soup(url)
    data = []
    if (engine == 'v8'):
        issue_links = soup.find_all('a')
        c = 1
        for issue in issue_links:
            print('{} of {}'.format(c, len(issue_links)))
            if 'detail?id=' in issue.get('href'):
                issue_link = BASE + issue.get('href')
                title = to_soup(issue_link).find_all('h1')[-1].span.string
                row = {"issue_name": title, "issue_url": issue_link}
                data.append(row)
            c+=1
    elif (engine == 'ch'):
        
    return data

def to_soup(url):
    req = requests.get(url)
    html_text = req.text
    soup = BeautifulSoup(html_text, "html.parser")
    return soup

def save_csv(data, csv_name):
    field_names = ['issue_name', 'issue_url']
    with open('{}.csv'.format(csv_name), 'w') as doc:
        doc = csv.DictWriter(doc, fieldnames=field_names)
        doc.writeheader()
        for line in data:
            row = {"issue_name": line["issue_name"], "issue_url": line["issue_url"]}
            doc.writerow(row)

data = get_all_issues_by_engine('v8', V8_wasm)
save_csv(data, '{}'.format('v8_wasm'))