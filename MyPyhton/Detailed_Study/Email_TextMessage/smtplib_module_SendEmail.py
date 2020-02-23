# SMTP (SIMPLE MAIL TRANSFER PROTOCOL) is the protocol for sending email over the internet
# smtplib module is used to send email in python

import smtplib
smtpObj = smtplib.SMTP('smtp.example.com', 587)  # domain name with smtp. prefixed. ex smtp.gmail.com and the port number
smtpObj.ehlo()  # pings/connects/texts to teh smtp server
# (250, b'mx.example.com at your service, [216.172.148.131]\nSIZE 35882577\n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nCHUNKING')
smtpObj.starttls()
# (220, b'2.0.0 Ready to start TLS')
smtpObj.login('bob@example.com', ' MY_SECRET_PASSWORD')
# (235, b'2.7.0 Accepted')
smtpObj.sendmail('bob@example.com', 'alice@example.com', 'Subject: So long.\nDear Alice, so long and thanks for all the fish. Sincerely, Bob')
# {}
smtpObj.quit()
# (221, b'2.0.0 closing connection ko10sm23097611pbd.52 - gsmtp')


#======= Connecting to an SMTP Server
# web search for <your provider> smtp settings should turn up the server and port to use
# smtp object for gmail :
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
# if teh above command dosent work, you will need to create an SMTP object using smtplib.SMTP_SSL() and port 465 instead
smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)


# ====================== Sending the SMTP “Hello” Message
# once the smtp object is created, need to call teh ehlo() method to ping/text smtp server
smtpObj.ehlo()
# (250, b'mx.google.com at your service, [216.172.148.131]\nSIZE 35882577\n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nCHUNKING')
# in return tuple, first value 250 (the code for “success” in SMTP), then the greeting succeeded.


# ======================= Starting TLS Encryption
# If you are connecting to port 587 on the SMTP server (that is, you’re using TLS encryption), you’ll need to call the starttls() method next.
# This required step enables encryption for your connection.
# If you are connecting to port 465 (using SSL), then encryption is already set up, and you should skip this step.
# Here’s an example of the starttls() method call:
smtpObj.starttls()
# (220, b'2.0.0 Ready to start TLS')
# starttls() puts your SMTP connection in TLS mode. The 220 in the return value tells you that the server is ready

# ============================ Logging in to the SMTP Server
# Once your encrypted connection to the SMTP server is set up,
# you can log in with your username (usually your email address) and email password by calling the login() method.
smtpObj.login(' my_email_address@gmail.com ', ' MY_SECRET_PASSWORD ')
# (235, b'2.7.0 Accepted')
# The 235 in the return value means authentication was successful.
# Python will raise an smtplib.SMTPAuthenticationError exception for incorrect passwords


# =========================Sending an Email
# call the sendmail() method to actually send the email. The sendmail() method call looks like this:
smtpObj.sendmail(' my_email_address@gmail.com ', ' recipient@example.com ', 'Subject: So long.\nDear Alice, so long and thanks for all the fish. Sincerely, Bob')
# {}
# The sendmail() method requires three arguments.
# 1. Your email address as a string (for the email’s “from” address)
# 2. The recipient’s email address as a string or a list of strings for multiple recipients (for the “to” address)
# 3. The email body as a string.
# The start of the email body string must begin with 'Subject: \n' for the subject line of the email.
# The '\n' newline character separates the subject line from the main body of the email.
# The return value from sendmail() is a dictionary.
# There will be one key-value pair in the dictionary for each recipient for whom email delivery failed.
# An empty dictionary means all recipients were successfully sent the email.


# =========================Disconnecting from the SMTP Server
# Be sure to call the quit() method when you are done sending emails. This will disconnect your program from the SMTP server.
smtpObj.quit()
# (221, b'2.0.0 closing connection ko10sm23097611pbd.52 - gsmtp')
# The 221 in the return value means the session is ending.