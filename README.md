
# Twilio page tracker

Page trackers are valuable tools with various use cases such as price or item-restock monitoring, news notifications, or seeing when a competitor's website has changed. However, current trackers such as [visualping](https://visualping.io/) run in browser with great ping frequency (ceiling of 1s) but eats up valuable compute resources, assumes that your PC is constantly on, and also assumes that you're nearby to receive the notification. Visualping also offers a remote solution but the ping frequency is low (sampling frequency ceiling of 5 minutes, 65 checks/month) and increasing checks/month will incur fees. 

Twilio page tracker overcomes these limitations by creating a free easily hostable application with a simple config file. The application is Heroku hostable ready and can run 24/7 on a free tier (overcoming challenges of checks/month), sample at a frequency of 1 second (matching visualping's ceiling rate), and provide SMS notifications when any change is detected. 

## Setup and deployment

There are a couple steps for set up and deployment: 

#### 1) Clone this github repo

#### 2) config.yml 
this file lives within the repo and will determine what is tracked, what number to send the notification to, and where/what is sent as a notification

**website**: website you'd like to track (enclose in apostrophes)  
**text_message**: message you'd like to be sent from text (enclose in apostrophes)  
**twilio_phone_number**: from twilio you can request a number. Input that here (enclose in apostrophes)  
**recipient_phone_number**: where you'd like your text_message/notification sent to (enclose in apostrophes)  
**ping_frequency_seconds**: sampling frequency in seconds (integer value i.e. a whole number)  


#### 3) Twilio - this API will allow you to receive SMS notifications
- create a twilio account  

##### **Recommended: Running on Heroku.**  

This method allows for you the page tracker to run automatically within draining your own computational resources. Heroku's free tier provides 550 hours plus another 450 hours per month (plenty as one month as 744 hours TOPS). The below details will allow your app in Heroku to connect to Twilio and send SMS notifications.  

- sign up for [heroku](https://www.heroku.com/)  
- create a new app and name it whatever you'd like  
- go to 'Settings' > 'Config Vars' > 'Reveal Config Vars'  
- populate **TWILIO_ACCOUNT_SID** and **TWILIO_AUTH_TOKEN** from your newly minted Twilio account  

![](/_pictures/heroku_config_vars_example.png)  
*populate Heroku Config Vars with the above two keys.*


##### **IF YOU'D LIKE TO RUN THIS CODE LOCALLY** 
- in a text editor of your choice, create a file named ".env" and populate with two parameters from your newly set up Twilio account:  
**TWILIO_ACCOUNT_SID**=*fillwithyouraccountid*  
**TWILIO_AUTH_TOKEN**=*fillwithyourauthtoken*  

![](/_pictures/env_file_example.PNG)  
*obviously not my actual account and token. Make sure to replace with your own.*


##### 4) Heroku hosting - this service will allow your app to run 24/7
If running locally, you can just skip this step and run in your IDE of choice. I use PyCharm when I run locally. If running in Heroku...    

- under your app in Heroku > 'Deploy' > 'Deployment method' > 'Github'  
- login to your GitHub account where you've pushed your cloned and edited repo (i.e. config.yml) of twilio-page-tracker  
- after connecting, Heroku should build and deploy your application   
- > 'Activity' to see if your build was successful  

- if *SUCCESS*: > 'Resources' > edit dyno formation > switch to 'ON'/ turns blue.  
- You should receive a text saying "Tracker for your website is now live!"    

- if *FAILURE*: you'll need to [install Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)  
- launch command prompt/terminal > cd to heroku in your directories (mine is under Program_files/heroku/bin) > heroku login > heroku logs --tail --app *YOURAPPNAME* and diagnose messages

![](/_pictures/track_main_heroku_cli.PNG)  
*my app is running successfully and when accessed from Heroku CLI should look like this. *

## Close
If you like this app and want to contribute to it, make a pull request! Feel free to reach out if you have any questions. Happy to help!

