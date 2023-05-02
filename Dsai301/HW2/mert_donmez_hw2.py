# Mert Dönmez
# 2016203039

# Question1:
def getPage(url):
    try:
        import urllib.request
        page = urllib.request.urlopen(url).read()
        page = page.decode('utf-8') #I used this because converting it to str not sense i think. Converting to string includes "//n" etc. commands into page and causes a lot of confusion .
        return page
    except:
        return ""

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
            links.append(url)
        else:
            break
    return links

def no_some_commands(word):    #To filter some commands in html code. We dont want to index them.
    html_codes = ["<html>","<body>","<p>","</p>","<a","</body>","</html>"]
    if word in html_codes:
        word = ""
    if word[0:4] == "href":
        word = ""
    if word.endswith("</b>") or word.endswith("</a>"):
        word = word[:-4]
    if word.startswith("<b>") or word.startswith("<a>") :
        word = word[3:]
    #Can be added other commands

    return word

def add_to_index(index, keyword, url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword, [url]])

def addPageToIndex(index, url, content):
    words = content.split()
    for word in words:
        word = word.lower() #Otherwise procedure acts like "the" and "The" are different words and indexes
        word = no_some_commands(word)
        if word:
            add_to_index(index, word, url)

def crawl_web(seed): #This crawl_web just adding links to do list and crawled these. However it doesnt index them.
    tocrawl = [seed]
    crawled = []
    while tocrawl:
        pageUrl = tocrawl.pop()
        if pageUrl not in crawled:
            content = getPage(pageUrl)
            for e in get_all_links(content):
                if e not in tocrawl:
                    tocrawl.append(e)
            crawled.append(pageUrl)

    return crawled
# print(get_all_links(getPage("https://udacity.github.io/cs101x/index.html")))
# print(crawl_web("https://udacity.github.io/cs101x/index.html"))


def crawl_web(seed): #Updateted version of crawl_web. 
    tocrawl = [seed]
    crawled = []
    index = []
    while tocrawl:
        pageUrl = tocrawl.pop()
        if pageUrl not in crawled:
            content = getPage(pageUrl)
            addPageToIndex(index, pageUrl, content)
            for e in get_all_links(content):
                if e not in tocrawl:
                    tocrawl.append(e)
            crawled.append(pageUrl)

    return index

# print(crawl_web("https://udacity.github.io/cs101x/index.html"))

# Question2: Update indexing to exclude a, an ,the,at,to etc..

def addPageToIndex(index, url, content):
    words = content.split()
    conjunctions = ["a","the","an","at","to","is","are","or","am","not","but","for"]
    for word in words:
        word = word.lower() #Otherwise procedure acts like "the" and "The" are different words and indexes
        word = no_some_commands(word)
        if word not in conjunctions and word:
                add_to_index(index, word, url)

# print(crawl_web("https://udacity.github.io/cs101x/index.html"))

# Question3:

def noPunct(word):
    punctuations = ["!", ",", ".", "(", ")", "?","’"]
    while len(word) > 0 and word[0] in punctuations:
        word = word[1:]
    while len(word) > 0 and word[-1] in punctuations:
        word = word[:-1]
    if word.endswith("’re") or word.endswith("’ve"):
        word = word[:-3]
    if word.endswith("’s"):
        word = word[:-2]

    return word



def addPageToIndex(index, url, content):
    words = content.split()
    
    conjunctions = ["a","the","an","at","to","is","are","or","am","not","but","for"]
    for word in words:
        word = word.lower() #Otherwise procedure acts like "the" and "The" are different words and indexes
        word = no_some_commands(word)
        word = noPunct(word)
        if word not in conjunctions and word: #To not add these words and links as index
                add_to_index(index, word, url)

# print(crawl_web("https://udacity.github.io/cs101x/index.html"))