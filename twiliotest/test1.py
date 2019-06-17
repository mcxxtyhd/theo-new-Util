from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACbcasdasdasdasdc1c0e2b'
auth_token = 'a67123123124124wrwerwerwerwere17e'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+13345186523',
                     to='+1asdasda1231558'
                 )

print(message.sid)