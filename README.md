
# Twilio page tracker

Page trackers are valuable tools with various use cases such as price or item-restock monitoring, news notifications, or seeing when a competitor's website has changed. However, current trackers such as [visualping](https://visualping.io/) run in browser with great ping frequency (ceiling of 1s) but eats up valuable compute resources, assumes that your PC is constantly on, and also assumes that you're nearby to receive the notification. Visualping also offers a remote solution but the ping frequency is low (sampling frequency ceiling of 5 minutes, 65 checks/month) and increasing checks/month will incur fees. 

Twilio page tracker overcomes these limitations by creating a free easily hostable application with a simple config file. The application is Heroku hostable ready and can run 24/7 on a free tier (overcoming challenges of checks/month), sample at a frequency of 1 second (matching visualping's ceiling rate), and provide SMS notifications when any change is detected. 

## Setup

There are a couple steps to set up: 

1) Clone this github repo locally

2) Twilio - this will allow you to receive SMS notifications
- create a twilio account  
- in a text editor of your choice, create a file named ".env" and populate with two parameters that can be got from your newly set up Twilio account:
== TWILIO_ACCOUNT_SID=fillwithyouraccountid
== TWILIO_AUTH_TOKEN=fillwithyourauthtoken

![]('\_pictures\env_file_example')
*obviously not my actual account and token. Make sure to replace with your own.*

3) config.yml
- this file will determine what is tracked, your phone number, and where/what is sent as a notification  
= website: website you'd like to track (enclose in apostrophes)  
= text_message: message you'd like to be sent from text (enclose in apostrophes)  
= twilio_phone_number: from twilio you can request a number. Input that here (enclose in apostrophes)  
= recipient_phone_number: where you'd like your text_message/notification sent to (enclose in apostrophes)  
= ping_frequency_seconds: sampling frequency in seconds (integer value i.e. a whole number)  


4) Heroku hosting
