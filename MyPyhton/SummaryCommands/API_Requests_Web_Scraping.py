# webbrowser :Comes with Python and opens a browser to a specific url.
# Requests :Downloads files and web pages from the Internet.
# Beautiful Soup : Parses HTML, the format that web pages are written in.
# Selenium: Launches and controls a web browser. Selenium is able to fill in forms and simulate mouse clicks in this browser



#! python3
# mapIt.py - Launches a map in the browser using an address from the command line or clipboard.
import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard.
    address = pyperclip.paste()
    webbrowser.open('https://www.google.com/maps/place/' + address)
    
    
    ==================================== requests =====================================================
    
import requests

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
type(res)    #<class 'requests.models.Response'>
if res.status_code == requests.codes.ok:   # as per HTTP protocol statu_code for OK is 200. Alternativly this line can also be res.status_code == 200
    len(res.text)
        # 178981
    print(res.text[:250])
"""The Project Gutenberg EBook of Romeo and Juliet, by William Shakespeare
This eBook is for the use of anyone anywhere at no cost and with
almost no restrictions whatsoever. You may copy it, give it away or
re-use it under the terms of the Projet"""


# Checking for Errors

# error can be checked by using teh status_code or code.ok . Asimpler way is to use the raise_for_status()
# call raise_for_status() on response object after the requests.get() to make sure website was downloaded correctly.
# if there was any error found downloading the site, this will raise exception and fail the program.
# if dont want to fail the program, the command can be wrapped in try - except block to catch teh exception

# without try-except block
res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
res.raise_for_status()
"""Traceback (most recent call last):
File "<pyshell#138>", line 1, in <module>
res.raise_for_status()
File "C:\Python34\lib\site-packages\requests\models.py", line 773, in raise_for_status
raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 404 Client Error: Not Found """

# with try - except block
res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))
# This raise_for_status() method call causes the program to output the following:
#There was a problem: 404 Client Error: Not Found



# ========Saving the downloaded files to hard drive==================
# with standard open() and write() functions. but the mode must be 'wb' :write binary
# iter_content(chunk_size in bytes) can be used to pull teh downloaded data in chunks


res= requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
res.raise_for_status()

with open('RomeoAndJuliet.txt', 'wb') as playfile:
    for chunk in iter_contet(100000):  # dowloding 100k bytes of data in each chunk
        playfile.write(chunk)    # write() method returns the number of bytes written to the file

"""
To review, here’s the complete process for downloading and saving a file:
1. Call requests.get() to download the file.
2. Call open() with 'wb' to create a new file in write binary mode.
3. Loop over the Response object’s iter_content() method.
4. Call write() on each iteration to write the content to the file.
"""


===========================================HTML========================================================
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
# select method with CSS selector if the element
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

================================================selenium====================================================

# >>> from selenium import webdriver
# >>> browser = webdriver.Firefox()
# >>> type(browser) : # <class 'selenium.webdriver.firefox.webdriver.WebDriver'>
# >>> browser.get('http://inventwithpython.com')
# use find_element_by_<Tag_attribute>* and find_elements_by_<Tag_attribute>* methods to find teh matched elements
# if no match found, it raises NoSuchElement exception
# If you do not want this exception to crash your program, add try and except statements to your code


