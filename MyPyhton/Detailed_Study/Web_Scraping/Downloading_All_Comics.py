# Downloading All XKCD Comics
# XKCD is a popular geek webcomic

#! python3
# downloadXkcd.py - Downloads every single XKCD comic.
import requests, os, bs4

url = 'http://xkcd.com'                 # starting url
os.makedirs('xkcd', exist_ok=True)       # store comics in ./xkcd
while not url.endswith('#'):

    # TODO: Download the page.
    print('Downloading the page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.beautifulSoup(res.text)

    # TODO: Find the URL of the comic image.
    comicElement = soup.select('#comic img')
    if comicElement == []
        print("couldnot find any comic image")
    else:
        comicURL = comicElement[0].get('src')

    # TODO: Download the image.
    print('Downloading teh image %s ..' %(comicURL))
    res = requests.get(comicURL)
    res.raise_for_status()

    # TODO: Save the image to ./xkcd.
    with open(os.path.join('xkccd',os.path.basename(comicURL)), 'wb') as imageFile:
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)

    # TODO: Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0].get('href')
    url = 'http://xkcd.com' + prevLink

print('Done.')