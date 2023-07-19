
# Mert Dönmez - 2016203039

# Question 1:


exampleWeb = {
   'http://udacity.com/cs101x/urank/index.html': """<html>
<body>
<h1>Dave's Cooking Algorithms</h1>
<p>
Here are my favorite recipes:
<ul>
<li> <a href="http://udacity.com/cs101x/urank/hummus.html">Hummus Recipe</a>
<li> <a href="http://udacity.com/cs101x/urank/arsenic.html">World's Best Hummus</a>
<li> <a href="http://udacity.com/cs101x/urank/kathleen.html">Kathleen's Hummus Recipe</a>
</ul>
For more expert opinions, check out the 
<a href="http://udacity.com/cs101x/urank/nickel.html">Nickel Chef</a> 
and <a href="http://udacity.com/cs101x/urank/zinc.html">Zinc Chef</a>.
</body>
</html>
""", 
   'http://udacity.com/cs101x/urank/zinc.html': """<html>
<body>
<h1>The Zinc Chef</h1>
<p>
I learned everything I know from 
<a href="http://udacity.com/cs101x/urank/nickel.html">the Nickel Chef</a>.
</p>
<p>
For great hummus, try 
<a href="http://udacity.com/cs101x/urank/arsenic.html">this recipe</a>.
</body>
</html>
""", 
   'http://udacity.com/cs101x/urank/nickel.html': """<html>
<body>
<h1>The Nickel Chef</h1>
<p>
This is the
<a href="http://udacity.com/cs101x/urank/kathleen.html">
best Hummus recipe!
</a>
</body>
</html>
""", 
   'http://udacity.com/cs101x/urank/kathleen.html': """<html>
<body>
<h1>
Kathleen's Hummus Recipe
</h1>
<p>
<ol>
<li> Open a can of garbanzo beans.
<li> Crush them in a blender.
<li> Add 3 tablespoons of tahini sauce.
<li> Squeeze in one lemon.
<li> Add salt, pepper, and buttercream frosting to taste.
</ol>
</body>
</html>
""", 
   'http://udacity.com/cs101x/urank/arsenic.html': """<html>
<body>
<h1>
The Arsenic Chef's World Famous Hummus Recipe
</h1>
<p>
<ol>
<li> Kidnap the <a href="http://udacity.com/cs101x/urank/nickel.html">Nickel Chef</a>.
<li> Force her to make hummus for you.
</ol>
</body>
</html>
""", 
   'http://udacity.com/cs101x/urank/hummus.html': """<html>
<body>
<h1>
Hummus Recipe
</h1>
<p>
<ol>
<li> Go to the store and buy a container of hummus.
<li> Open it.
</ol>
</body>
</html>
""", 
}


def getPage(url):
    if url in exampleWeb:
        return exampleWeb[url]
    else:
        return None
    


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

def union(p,q):
    for e in q: 
        if e not in p: 
            p.append(e)

def no_some_commands(word):    #To filter some commands in html code. We dont want to index them.
    html_codes = ["<html>","<body>","<p>","</p>","<a","</body>","</html>","<li>","<ul>","</ul>","<ol>","</ol>"]
    if word in html_codes:
        word = ""
    if word[0:4] == "href":
        word = ""
    if word.endswith("</b>") or word.endswith("</a>") or word.endswith("<h1>"):
        word = word[:-4]
    if word.endswith("</h1>"):
        word = word[:-5]
    if word.startswith("<b>") or word.startswith("<a>") :
        word = word[3:]
    if word.startswith("<h1>")  :
        word = word[4:]
    #Can be added other commands

    return word

def noPunct(word):
    punctuations = ["!", ",", ".", "(", ")", "?","’"]
    while len(word) > 0 and word[0] in punctuations:
        word = word[1:]
    while len(word) > 0 and word[-1] in punctuations:
        word = word[:-1]
    if word.endswith("’re") or word.endswith("’ve"):
        word = word[:-3]
    if word.endswith("'s"):
        word = word[:-2]

    return word

def add_to_index(index, keyword, url): #Now index is a dictionary
    if keyword in index:
        if url not in index[keyword]:
            index[keyword].append((url))
    else:
        index[keyword] = [(url)]


def addPageToIndex(index, url, content):
    words = content.split()
    
    conjunctions = ["a","the","an","at","to","is","are","or","am","not","but","for","and","from","in","of"]
    for word in words:
        word = word.lower() #Otherwise procedure acts like "the" and "The" are different words and indexes
        word = no_some_commands(word)
        word = noPunct(word)
        word = no_some_commands(word)
        if word not in conjunctions and word: #To not add these words and links as index
                add_to_index(index, word, url)


def pageRank(graph):

    d = 0.8
    nLoops= 10
    ranks = {}
    nPages= len(graph)

    for page in graph:
        ranks[page] = 1.0 / nPages


    for i in range(0,nLoops):
        newranks = {}
        for page in graph:
            newrank = (1 - d) / nPages
            for node in graph:
                if page in graph[node]:
                    newrank = newrank + (d * (ranks[node] / len(graph[node])))
            newranks[page] = newrank
        ranks = newranks
    return ranks


def crawlWeb(seed):  #just add a parameter for date
    tocrawl = [seed]
    crawled = []

    index = {} #Now index is a dictionary
    graph = {} #The Dictionary that holds links in the page
    while tocrawl: 
        page = tocrawl.pop()
        if page not in crawled: 
            content = getPage(page)
            outlinks = get_all_links(content)
            graph[page] = outlinks
            addPageToIndex(index, page, content)
            union(tocrawl, outlinks)
            crawled.append(page)


    return index, graph


my_index, graph = crawlWeb("http://udacity.com/cs101x/urank/index.html")
my_ranks = pageRank(graph)

#In order for the PageRank function to work properly, the "graph" dictionary must be completed.
#But since we already added the url and keyword to the "index" when filling in the "graph" in the crawlWeb function,
#it was difficult to add the rank part to the "index" dictionary later. 
#Instead, I will keep the dictionary created by the RankPage function separately and make a search ranking using this dictionary in the lookUp function.

# print(my_index)
# print(graph)
# print(my_ranks)

# Question 2:

def lookup(index, keyword, ranks): 
    keyword = keyword.lower() #Because I converted keywords in index to lower case in the addPageToIndex function. So searching keywords also must be lower case.

    if keyword in index:
        pages = index[keyword]
    else:
        pages = None
    
    return pageSorting(pages, ranks)

def pageSorting(pages, ranks): #Recursive sorting algorithm
    if not pages or len(pages) <= 1:
        return pages
    else:
        pivot = ranks[pages[0]]
        worse = []
        better = []
        for page in pages[1:]:
            if ranks[page] <= pivot:
                worse.append(page)
            else:
                better.append(page)
    return pageSorting(better, ranks) + [pages[0]] + pageSorting(worse, ranks)


def search(keyword): # Unlike lookup, it searches with a single word input and prints the results
    print("KEYWORD:", keyword)
    results = lookup(my_index, keyword, my_ranks)
    if results:
        for url in results:
            print("URL:", url, "RANK", my_ranks[url])
    else:
        print("""Did you mean "Hummus"? :)""")
    print()


search("Hummus")
search("chef")
search("mert")
search("Lemon")
search("storE")