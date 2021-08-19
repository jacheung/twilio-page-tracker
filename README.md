
# Twilio page tracker

Page trackers are valuable tools with various use cases such as price or item-restock monitoring, news notifications, or seeing when a competitor's website has changed. However, current trackers such as [visualping](https://visualping.io/) run in browser with great ping frequency (ceiling of 1s) but eats up valuable compute resources, assumes your PC is constantly on, and that you're nearby to receive the notification. Visualping also offers a remote solution but the ping frequency is low (sampling frequency ceiling of 5 minutes, 65 checks/month) and increasing checks/month will incur fees. 

Twilio page tracker overcomes these limitations by creating a free easily hostable application with a simple config file. The application is Heroku hostable ready and can run 24/7 on a free tier (overcoming challenges of checks/month), sample at a frequency of 1 second (matching visualping's ceiling rate), and provide SMS notifications when any change is detected. 

## Setup

