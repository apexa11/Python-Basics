from twilio import rest

# Your Account SID from twilio.com/console
account_sid = "AC8bea92c256a3f96debec4fa1314cace2"
# Your Auth Token from twilio.com/console
auth_token  = "620c65e471b40cb7006c1e3e98e9b404"

client = rest.TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(
 
    to="+14435313817", 
    from_="+14437762069",
    body="Hello from Python!")

print(message.sid)
