#Mert Donmez
#2016203039


def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    while tocrawl:
        pageUrl = tocrawl.pop()
        if pageUrl not in crawled:
            for e in get_all_links(get_page(pageUrl)):
                if e not in tocrawl and e not in crawled:
                    tocrawl.append(e)
            crawled.append(pageUrl)
    return crawled