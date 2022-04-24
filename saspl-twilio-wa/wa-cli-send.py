from twilio.rest import Client 
 
account_sid = '<>' 
auth_token = '<>' 
client = Client(account_sid, auth_token) 
 
"""
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Hello! This is an editable text message. You are free to change it and write whatever you like.',      
                              to='whatsapp:+919900000000' 
                          ) 
 
print(message.sid)
"""

"""
message = client.messages.create(
         media_url=['https://images.unsplash.com/photo-1545093149-618ce3bcf49d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=668&q=80'],
         from_='whatsapp:+14155238886',
         to='whatsapp:+919900000000'
     )

print(message.sid)
print(message)
"""

message = client.messages.create( 
                              from_='whatsapp:+919900000000',
                              body='Hello! This is an editable text message. You are free to change it and write whatever you like.',      
                              to='whatsapp:+14155238886'
                          ) 
 
print(message.sid)