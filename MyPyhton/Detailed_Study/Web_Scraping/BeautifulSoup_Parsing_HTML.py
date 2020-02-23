# f12 to open the chrome developer tool
# right click on browser and click "view page source
# right-click any part of the web page and select Inspect Element from the context menu to bring up the HTML responsible for that part of the page.
# This will be helpful when you begin to parse HTML for your web scraping programs

"""
Beautiful Soup is a module for extracting information from an HTML page (and is much better for this purpose than regular expressions).
The BeautifulSoup module’s name is bs4 (for Beautiful Soup, version 4).
To install it, you will need to run pip install beautifulsoup4
While beautifulsoup4 is the name used for installation, to import Beautiful use import bs4 in program.
"""

""" SAVE THE FOLLOWING CODES I EXERCISE.HTML
<html><head><title>The Website Title</title></head>
<body>
<p>Download my <strong>Python</strong> book from <a href="http://inventwithpython.com">my website</a>.</p>
<p class="slogan">Learn Python the easy way!</p>
<p>By <span id="author">Al Sweigart</span></p>
</body></html>
"""

import bs4, requests

# bs4.BeautifulSoup() function needs to be called with a string containing the HTML
# it will parse. The bs4.BeautifulSoup() function returns is a BeautifulSoup object

res = requests.get('http://nostarch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text)  # text attribute of teh response is passed tp bs4.beautifulsoup
type(noStarchSoup)   # <class 'bs4.BeautifulSoup'>


# HTML file can also be loaded from the hard drive
examplefile = open('example.html')
exampleSoup = bs4.beautifulSoup(examplefile)
type(exampleSoup) # <class 'bs4.BeautifulSoup'>

# select() method can be used find the element of interest
# select method with CSS selector of the element
# these selectors are like regex, they specify an HTML pattern to look for in HTML pages
# ex:soup.select('#author') The element with an id attribute of author
# The select() method will return a list of HTML Tag objects.
# The list will contain one Tag object for every match in the BeautifulSoup object’s HTML.
# Tag values can be passed to the str() function to show the HTML TAGs they represent.
# Tag values also have an attrs attribute that shows all the HTML attributes of the TAG as a dictionary
# getText() can be used with the tag object to check teh text value they represent
# The get() method for Tag objects makes it simple to access attribute values of a TAG element.
# The method is passed an attribute name and returns that attribute’s # value.

examplefile = open('example.html')
exampleSoup = bs4.beautifulSoup(examplefile.read())
elems = exampleSoup.select('#author')
type(elems) # <class 'list'>

print(len(elems)) # 1
print(type(elems[0]))  #<class 'bs4.element.Tag'>
print(elems[0].getText())   # Al Sweigart
print(str(elems[0]))   # <span id="author">Al Sweigart</span>
print(elems[0].attrs)   # {'id': 'author'}

##################################################
pElems = exampleSoup.select('p')
str(pElems[0]) #'<p>Download my <strong>Python</strong> book from <a href="http://inventwithpython.com">my website</a>.</p>'
pElems[0].getText() #'Download my Python book from my website.'
str(pElems[1]) #'<p class="slogan">Learn Python the easy way!</p>'
pElems[1].getText() #'Learn Python the easy way!'
str(pElems[2]) #'<p>By <span id="author">Al Sweigart</span></p>'
pElems[2].getText() #'By Al Sweigart'
##################################################

import bs4
soup = bs4.BeautifulSoup(open('example.html'))
spanElem = soup.select('span')[0]
str(spanElem) # '<span id="author">Al Sweigart</span>'
spanElem.get('id') # 'author'
spanElem.get('some_nonexistent_addr') == None #True
spanElem.attrs #{'id': 'author'}