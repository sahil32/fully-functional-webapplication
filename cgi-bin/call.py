#!/usr/bin/python36
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACb94a02198a2bc277953116c463806c11'
auth_token = '60f1a628e3b29d923d5fe239dbdbbc10'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to='+919509103484',
                        from_='+919660235627'
                    )

print(call.sid)
