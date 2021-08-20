import os
import time
import hashlib
from urllib.request import urlopen, Request
from twilio.rest import Client
from dotenv import load_dotenv
import yaml


def track(website, text_message, twilio_phone_number, recipient_phone_number, ping_frequency_seconds):
    # create initial hash
    url = Request(website,
                  headers={'User-Agent': 'Mozilla/5.0'})
    response = urlopen(url).read()
    current_hash = hashlib.sha224(response).hexdigest()
    print("Starting monitor...")
    client.messages.create(
        body='Tracker for ' + website + ' is now live!',
        from_=twilio_phone_number,
        to=recipient_phone_number
    )
    while True:
        try:
            # wait for 5 seconds
            time.sleep(ping_frequency_seconds)

            response = urlopen(url).read()
            new_hash = hashlib.sha224(response).hexdigest()

            # check if new hash is same as the previous hash
            if new_hash == current_hash:
                print('no change')
                continue

            # if something changed in the hashes
            else:
                # notify via Twilio
                client.messages.create(
                    body=text_message,
                    from_=twilio_phone_number,
                    to=recipient_phone_number
                )

                # again read the website and update the hash
                response = urlopen(url).read()
                current_hash = hashlib.sha224(response).hexdigest()

                # wait before pinging
                time.sleep(ping_frequency_seconds)
                continue

        # To handle exceptions
        except Exception:
            client.messages.create(
                body="Code has broken. :'(",
                from_=twilio_phone_number,
                to=recipient_phone_number
            )
            break


if __name__ == '__main__':
    try:
        # FOR LOCAL:
        load_dotenv('.env')
        account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    except NameError:
        # FOR HEROKU:
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']

    client = Client(account_sid, auth_token)
    track_config = yaml.safe_load(open(os.getcwd() + "\\config.yml"))

    track(website=track_config['website'],
          text_message=track_config['text_message'],
          twilio_phone_number=track_config['twilio_phone_number'],
          recipient_phone_number=track_config['recipient_phone_number'],
          ping_frequency_seconds=track_config['ping_frequency_seconds'])

