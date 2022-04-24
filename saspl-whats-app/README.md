Twilio for WhatsApp

Points Covered
- Twilio Environment
- One-Way Message
- Two-Way Message
- Number Onboarding
- Call-Backs & Data Xchanged
- Monitoring Messages
- Interfaces with AWS-Lex, GCP-DialogFlow
- Pricing

Pre-requisites / Usage
- Account on Twilio
- Python 3.7+, Flask and associated components
- Deploy to a public server

Twilio Environment
- Sandbox provided for testing (needs to be refreshed daily)
- Identifiers are provisioned (AccountSid, AuthToken) and must be used to interface in all programs
- Native TwiML (the Twilio Markup Language, which is just to say that it's an XML document with special tags defined by Twilio to help you build 
your messaging and voice applications)
- TwiML expertise not mandatory for basic application but helpful for larger ones
- Sandbox provides a master demo-number and a code to identify our sand-box
- To use own phone number and brand name with WhatsApp, the account must be approved by WhatsApp. 
- This approval is provided only for brands that the company owns

Twilio Application Panel
- Use to setup the sandbox
- Use to authorize whats-app number
- Use to send one-way message (can be done via panel itself)
- For 2-way, use web-hook concept to provide call-backs to our application urls
- Configure web-hooks for 2-way application routing
- Monitor Logs

To Consider
- the on-boarding and authorization of WhatsApp numbers
- de-authorize or change the WhatsApp numbers
- a full-flow consists of many states <send, deliver, read, not-deliver>
- the flows are monitored via the status-webhook / callback
- auth-tokens may be refreshed periodically, and the latest to be taken in program
- credit-balance to be monitored and auto-modified based on traffic

First complete the following video to get sense of the basic approach
WhatsApp Bot using Twilio and Python (Part-1) | Setting up Twilio Sandbox for WhatsApp
<https://www.youtube.com/watch?v=BKK5NMDC0fk>

Message Dumps
- User messages are received with the following "request.data" formats
    Fields are SmsMessageSid, NumMedia, ProfileName, SmsSid, WaId, SmsStatus, Body, To, NumSegments, ReferralNumMedia, MessageSid, AccountSid, From, ApiVersion

- Status messages are received with the following "request.data" formats
    Fields are SmsSid, SmsStatus, MessageStatus, ChannelToAddress, To, ChannelPrefix, MessageSid, AccountSid, StructuredMessage, From, ApiVersion, ChannelInstallSid

EXAMPLE OF USER MESSAGE RCVD (FROM CALLBACK)
b'SmsMessageSid=SM45e9b726c0314a5524cXXXX&NumMedia=0&ProfileName=Ranjit+Sankar&SmsSid=SM45e9b726c0314a5524c3f3cbYYYYY&WaId=91990000000&SmsStatus=received&Body=hey&To=whatsapp%3A%2B14155238886&NumSegments=1&ReferralNumMedia=0&MessageSid=SM45e9b726c0314a5524c3f3cb4ZZZZZ&AccountSid=AC8e904faad99a05efe123e12DDDDDD&From=whatsapp%3A%2B919900000000&ApiVersion=2010-04-01'

EXAMPLE OF STATUS MESSAGE RCVD (FROM CALLBACK)
b'SmsSid=SMc4c96554c26604013c6b7f1b4bXXXXX&SmsStatus=sent&MessageStatus=sent&ChannelToAddress=%2B91994541XXXX&To=whatsapp%3A%2B919900000000&ChannelPrefix=whatsapp&MessageSid=SMc4c96554c26604013c6b7f1b4b6DDDDD&AccountSid=AC8e904faad99a05efe123e12515ZZZZZ&StructuredMessage=false&From=whatsapp%3A%2B14155238886&ApiVersion=2010-04-01&ChannelInstallSid=XEcc20d939f803ee381f2442185EEEEE'

INDICATIVE PRICING
Considers Conversation Price + Per Msg Price + No.Users
https://support.twilio.com/hc/en-us/articles/360037672734-How-Much-Does-it-Cost-to-Send-and-Receive-WhatsApp-Messages-with-Twilio-


THIS REPO HAS FOLL. FILES
- wa-cli-send.py which is a simple program to send a msg (text, image) to a number
- wa-send-recv.py which is a program that awaits an image from a number, and replies with an image to the same numer
- wa-reminder.py which is a program that schedules reminders via whatsapp

In both wa-send-recv and wa-reminder,
- the message call-back is at route /wa
- the status call-back is at route /sts

ADDITIONAL INFO
Instead of writing our native python/similar code, Twilio can also be integrated with AWS-Lex and GCP-DialogFlow

Create Your Own Amazon Lex Chatbot - Full tutorial (AWS-Lex not available in Mumbai as on Apr-2022)
<https://www.youtube.com/watch?v=Gy0C9g16DW0>
