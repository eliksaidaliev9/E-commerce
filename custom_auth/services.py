import random
import requests
from django.core.cache import cache
from django.conf import settings


SMS_KEY = settings.SMS_KEY


def generate_verification_code():
    return str(random.randint(100000, 999999))

def send_verification_sms(phone_number):
    code = generate_verification_code()

    url = "https://gateway.seven.io/api/sms"
    payload = {
        "to": [phone_number],
        "from": "elixya",
        "text": f"Your verification code is {code}"
    }
    headers = {
        "X-Api-Key": SMS_KEY,
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    print("STATUS:", response.status_code)
    print("RESPONSE:", response.text)

    if response.status_code == 200:
        cache.set(phone_number, code, 300)
        print(f"[FAKE SMS] To: {phone_number}, Code: {code}")
        return True
    return False
