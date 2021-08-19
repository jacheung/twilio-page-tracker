import os
import time
import hashlib
from urllib.request import urlopen, Request
from twilio.rest import Client
from dotenv import load_dotenv
import yaml


load_dotenv('.env')
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)
track_config = yaml.safe_load(open(os.getcwd() + "\\config.yml"))


def track(website, text_message, to_number, ping_frequency):
    # create initial hash
    url = Request(website,
                  headers={'User-Agent': 'Mozilla/5.0'})
    response = urlopen(url).read()
    current_hash = hashlib.sha224(response).hexdigest()
    print("Starting monitoring...")
    while True:
        try:
            # wait for 5 seconds
            time.sleep(ping_frequency)

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
                    from_='+17472479302',
                    to=to_number
                )

                # again read the website and update the hash
                response = urlopen(url).read()
                current_hash = hashlib.sha224(response).hexdigest()

                # wait before pinging
                time.sleep(ping_frequency)
                continue

        # To handle exceptions
        except Exception:
            client.messages.create(
                body="Code has broken. :'(",
                from_='+17472479302',
                to=to_number
            )
            break


if __name__ == '__main__':
    website = track_config['website']
    text_message = track_config['text_message']
    phone_number = track_config['recipient_phone_number']
    ping_frequency_seconds = track_config['ping_frequency_seconds']
    track(website, text_message, phone_number, ping_frequency_seconds)

