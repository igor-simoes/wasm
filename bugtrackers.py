import requests, csv

class Trackers:
    def __init__(self, name, url, query, num_pages=1):
        self.name = name
        self.url = url
        self.query = query
        self.num_pages = num_pages
        self.html_text = ''
        self.num_pages = num_pages
        self.data = set({})

    def get_html_text(self, page):
        if self.num_pages > 1:
            pass

        req = requests.get(self.get_full_url())
        text = req.text.strip()
        
        return text

    def get_url(self):
        return self.url

    def get_query(self):
        return self.query

    def get_num_pages(self):
        return self.num_pages
    
    def get_full_url(self):
        # fix this later
        return self.url + self.query

    def save_to_csv(self):
        field_names = ['bug_tracker', 'issue name', 'issue_url']
        with open('issues_{}.csv'.format(self.name), 'w') as doc:
            doc = csv.DictWriter(doc, fieldnames=field_names)
            for line in self.data:
                row = {"bug_tracker": line["bug_tracker"], "issue_name": line["issue_name"], "bug_tracker": line["issue_url"]}
                doc.writerow(row)

class Chakra(Trackers):
    CHAKRA_URL = "https://github.com/Microsoft/ChakraCore/issues?q="
    
    def __init__(self, query):
        Trackers.__init__(self, "ch", CHAKRA_URL, query)

class V8(Trackers):
    V8_URL = "https://bugs.chromium.org/p/v8/issues/list"
    BASE = "https://bugs.chromium.org/"
    all_issues = "https://bugs.chromium.org/p/v8/issues/list?can=1&q=wasm&colspec=ID+Type+Status+Priority+Owner+Summary+HW+OS+Component+Stars&x=priority&y=owner&cells=ids&start={}"
    
    def __init__(self, query):
        Trackers.__init__(self, "v8", V8_URL, query)

class SpiderMonkey(Trackers):
    SPIDERMONKEY_URL = ""

    def __init__(self, query):
        Trackers.__init__(self, "sm", SPIDERMONKEY_URL, query)

class WebKit(Trackers):
    WEBKIT_URL = "https://bugs.webkit.org/buglist.cgi?bug_status=UNCONFIRMED&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED&bug_status=RESOLVED&bug_status=VERIFIED&bug_status=CLOSED&component=JavaScriptCore&list_id=4281411&longdesc=wasm%20WebAssembly%20webassembly&longdesc_type=anywordssubstr&product=WebKit&query_format=advanced"

    def __init__(self, query):
        Trackers.__init__(self, "jsc", WEBKIT_URL, query)


