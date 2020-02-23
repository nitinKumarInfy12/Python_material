#! python3

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



# Saving the downloaded files to hard drive
# with standard open() and write() functions. but the mode must be 'wb' :write binary
# iter_content(chunk_size in bytes) can be used to pull teh downloaded data in chunks


res= requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
res.raise_for_status()

with open('RomeoAndJuliet.txt', 'wb') as playfile:
    for chunk in res.iter_contet(100000):  # dowloding 100k bytes of data in each chunk
        playfile.write(chunk)    # write() method returns the number of bytes written to the file

"""
To review, here’s the complete process for downloading and saving a file:
1. Call requests.get() to download the file.
2. Call open() with 'wb' to create a new file in write binary mode.
3. Loop over the Response object’s iter_content() method.
4. Call write() on each iteration to write the content to the file.
"""





