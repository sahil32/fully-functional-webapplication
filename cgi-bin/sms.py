
# coding: utf-8

# In[3]:


from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACd9c39949157e732edacd7b85106be671'
auth_token = '70c4fa6d1608cb06095d6f40c934fb32'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hi chhotu',
                              from_='+13345641870',
                              to='+917877443404'
                          )

print(message.sid)
#OUTPUT
#{
#  "account_sid": "ACc6987f223e725c9be88214b64efcb348",
#  "api_version": "2010-04-01",
#  "body": "Hi there!",
#  "date_created": "Thu, 30 Jul 2015 20:12:31 +0000",
#  "date_sent": "Thu, 30 Jul 2015 20:12:33 +0000",
#  "date_updated": "Thu, 30 Jul 2015 20:12:33 +0000",
#  "direction": "outbound-api",
#  "error_code": null,
 # "error_message": null,
 # "from": "+919887860854",
 # "messaging_service_sid": "MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
 # "num_media": "0",
 # "num_segments": "1",
 # "price": "-0.00750",
 # "price_unit": "USD",
 # "sid": "MMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
 # "status": "sent",
 # "subresource_uris": {
 #   "media": "/2010-04-01/Accounts/AC/Messages/SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Media.json"
 # },
 # "to": "+14155552345",
 # "uri": "/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Messages/SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.json"
#}

