# Just as SMTP is the protocol for sending email,
# IMAP (Internet Message Access Protocol)specifies how to communicate with an email provider’s server to retrieve emails sent to your email address

# Python comes with an imaplib module, but in fact the third party imapclient module is easier to use.

# The imapclient module downloads emails from an IMAP server in a rather complicated format.
# you’ll want to convert them from this format into simple string values.
# The pyzmail module does the hard job of parsing these email messages for you.


import imapclient
import pyzmail

# here’s a full steps of logging in to an IMAP server, searching for emails, fetching them, and then extracting the text of the email messages from them.
imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapObj.login(' my_email_address@gmail.com ', ' MY_SECRET_PASSWORD ')
# 'my_email_address@gmail.com Jane Doe authenticated (Success)'
imapObj.select_folder('INBOX', readonly=True)
UIDs = imapObj.search(['SINCE 05-Jul-2014'])
UIDs
# [40032, 40033, 40034, 40035, 40036, 40037, 40038, 40039, 40040, 40041]
rawMessages = imapObj.fetch([40041], ['BODY[]', 'FLAGS'])
message = pyzmail.PyzMessage.factory(rawMessages[40041]['BODY[]'])
message.get_subject()
# 'Hello!'
message.get_addresses('from')
# [('Edward Snowden', 'esnowden@nsa.gov')]
message.get_addresses('to')
# [(Jane Doe', 'jdoe@example.com')]
message.get_addresses('cc')
# []
message.get_addresses('bcc')
# []
message.text_part != None
# True
message.text_part.get_payload().decode(message.text_part.charset)
# 'Follow the money.\r\n\r\n-Ed\r\n'
message.html_part != None
# True
message.html_part.get_payload().decode(message.html_part.charset)
# '<div dir="ltr"><div>So long, and thanks for all the fish!<br><br></div>-Al<br></div>\r\n'
imapObj.logout()

















