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