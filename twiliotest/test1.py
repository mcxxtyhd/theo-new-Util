from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACbc92982bc1b885f53ed32c1a6c1c0e2b'
auth_token = 'a67d6585a3b5fa51206e5542f4d9e17e'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+13345186523',
                     to='+18789563558'
                 )

print(message.sid)