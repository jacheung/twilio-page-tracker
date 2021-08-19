import time
import hashlib
from urllib.request import urlopen, Request
from twilio.rest import Client
from dotenv import load_dotenv
import os


load_dotenv('.env')
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

website = 'https://space-invaders.com/spaceshop/product/99108775083900940'
# website = 'https://hypebeast.com/'
text_message = 'Website change! https://space-invaders.com/spaceshop'
to_number = '+14155192029'
ping_frequency = 5  # in seconds


def track(website, text_message, to_number):
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
    track(website, text_message, to_number)