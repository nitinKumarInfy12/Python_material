#! pythonn3

import webbrowser, bs4, requests, sys

print("Googling...")  # prints googling meanwhile web is loaded

res = requests.get('https://www.google.com/search?q='+ ' '.join(sys.argv[1:]))
res.raise_for_status()  # res.status_code == requests.codes.ok

googleSoup = bs4.beautifulSoup(res.text)
linkElems = googleSoup.select('.r a')

tabnums = min(5, len(linkElems))  # returns teh minimum number from both

for i in range(tabnums)
    webbrowser.open('http:google.com'+linkElems[i].get('href'))





