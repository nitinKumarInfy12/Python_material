# sign up for a Twilio account, verify your phone number, register a Twilio phone number, and obtained your account SID and auth token,
# install the twilio module :pip install twilio

from twilio.rest import TwilioRestClient
accountSID = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
authToken = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
twilioCli = TwilioRestClient(accountSID, authToken)
myTwilioNumber = '+14955551234'  # sender`s number
myCellPhone = '+14955558888'     # recipient`s number
message = twilioCli.messages.create(body='Mr. Watson - Come here - I want to see you.', from_=myTwilioNumber, to=myCellPhone)

# message Object has following attributes:
message.to          # '+14955558888'
message.from_   # '+14955551234'
message.body    # 'Mr. Watson - Come here - I want to see you.'

message.status  # 'queued'
message.date_created    #datetime.datetime(2015, 7, 8, 1, 36, 18)
message.date_sent == None  # True

# You will need to refetch the Message object in order to see its most up-to-date status and date_sent.
# Every Twilio message has a unique string ID (SID) that can be used to fetch the latestupdate of the Message object
message.sid     # 'SM09520de7639ba3af137c6fcb7c5f4b51'
updatedMessage = twilioCli.messages.get(message.sid)
updatedMessage.status       # 'delivered'
updatedMessage.date_sent    #datetime.datetime(2015, 7, 8, 1, 36, 18)


