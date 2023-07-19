# Mert Dönmez
# 2016203039

# Question1:

def get_day_name(day, month, year):
    # I didnt importing datetime so i used a different algorithm to determine weekday. 
    # Compute the number of days using Zeller's congruence. (https://en.wikipedia.org/wiki/Zeller%27s_congruence)
    y = year - (14 - month) // 12
    m = month + 12 * ((14 - month) // 12) - 2
    d = (day + y + y//4 - y//100 + y//400 + (31*m)//12) % 7
    
    weekdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    return weekdays[d]

def is_weekend(day, month, year):
    
    # Returns True if the given date is a weekend holiday, False otherwise.
    
    if year < 1935:  # before 1935, Friday was the weekend day
        if get_day_name(day,month,year) == "Friday":
            return True
    else:
        if get_day_name(day,month,year) == "Sunday":
            return True
    
    return False



def is_holiday(day, month, year):
    
    # Returns True if the given date is a holiday in Turkey, False otherwise.
  
    holidays = [
        (1, 1, 1935),   # New Year's Day
        (23, 4, 1921),  # Children's Day
        (1, 5, 2009),   # Labour Day
        (19, 5, 1935),  # Youth and Sports Day
        (15, 7, 2016),  # Democracy Day
        (30, 8, 1935),  # Victory Day 
        (29, 10, 1925), # Republic Day 
    ]
    
    for holiday in holidays:
        holiday_day, holiday_month, holiday_announcement_year = holiday
        if year >= holiday_announcement_year and (day, month) == (holiday_day, holiday_month):
            return True
        
    return False

def is_leap_year(year):
    
    # Returns True if the given year is a leap year, False otherwise.

    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False
    
def days_in_month(month, year):

    # Returns the number of days in the given month and year.
    
    if month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    elif month in {4, 6, 9, 11}:
        return 30
    else:
        return 31

def next_day(day, month, year):
    
    # Increment the day by 1
    day += 1
    
    # Check if the day exceeds the number of days in the month
    if day > days_in_month(month, year):
        day = 1
        month += 1
        if month > 12:
            month = 1
            year += 1
    
    return (day, month, year)

def invalid_dates(d1, m1, y1, d2, m2, y2):

    # Returns True if the given dates are invalid and gives an error message, False otherwise.

    if y1 < 1920 or y2 < 1920:
        print("Invalid input dates. Please enter a date between 1920-present")
        return True
    
    if d1 < 1 or m1 < 1 or m1 > 12 or d1 > days_in_month(m1, y1):
        print("Start date is invalid")
        return True
    
    if d2 < 1 or m2 < 1 or m2 > 12 or d2 > days_in_month(m2, y2):
        print("End date is invalid")
        return True
    
    if y2 < y1 or (y2 == y1 and (m2 < m1 or (m2 == m1 and d2 < d1))):  
        print("End date is before start date")
        return True
    
    return False


def vacations(d1, m1, y1, d2, m2, y2):
    
     # Calculates the total number of vacation days between two dates

    if invalid_dates(d1, m1, y1, d2, m2, y2):
        return None

    
    total_holidays = 0
    current_date = (d1, m1, y1)

    while current_date != next_day(d2, m2, y2):  # I add 1 to end day to include it in the range
        if is_weekend(*current_date):
            total_holidays += 1
        elif is_holiday(*current_date):
            total_holidays += 1

        current_date = next_day(*current_date)
    
    return total_holidays


# print(vacations(29,8,1930,29,8,1930)) # it counts 1 because it is friday


# Question2:

import datetime 

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

def union(p,q):
    for e in q: 
        if e not in p: 
            p.append(e)

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

def add_to_index(index, keyword, url, crawl_date):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append((url, crawl_date))
            return
    index.append([keyword, [(url, crawl_date)]])

def addPageToIndex(index, url, content, crawl_date):
    words = content.split()
    
    conjunctions = ["a","the","an","at","to","is","are","or","am","not","but","for"]
    for word in words:
        word = word.lower() #Otherwise procedure acts like "the" and "The" are different words and indexes
        word = no_some_commands(word)
        word = noPunct(word)
        if word not in conjunctions and word: #To not add these words and links as index
                add_to_index(index, word, url, crawl_date)



def crawlWeb(seed, date):  #just add a parameter for date
  tocrawl = [seed]
  crawled = []
  index = []
  while tocrawl: 
    page = tocrawl.pop()
    if page not in crawled: 
      content = getPage(page)

      addPageToIndex(index, page, content, date)

      union(tocrawl, get_all_links(getPage(page)))
      crawled.append(page)

  return index

my_index = crawlWeb("https://udacity.github.io/cs101x/index.html", [12, 1, 2021])



# print(crawlWeb("https://udacity.github.io/cs101x/index.html", [12, 1, 2021]))

