
import urllib.request
def get_page(first_url):
    page = urllib.request.urlopen(first_url).read()
    page = page.decode('utf-8')
    return page

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return (None, 0)
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return (url, end_quote)

def get_all_links(page_text):
    links =[]
    while True:
        (url, end_pos) = get_next_target(page_text)
        if url:
            page_text = page_text[end_pos:]
            if url[0:4] == "http":
                links.append(url)
        else:
            break
    return links


def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    while tocrawl:
        pageUrl = tocrawl.pop()
        if pageUrl not in crawled:
            for e in get_all_links(get_page(pageUrl)):
                if e not in tocrawl:
                    tocrawl.append(e)
            crawled.append(pageUrl)
    return crawled

print(crawl_web("https:/boun.edu.tr"))
#print(get_all_links(get_page("https://haberler.boun.edu.tr/tr/haber/ogretim-uyemiz-dr-alper-yagciya-tuba-ustun-basari-odulu")))