#python3!- Write a program that runs just before you wake up in the morning
#and checks whether it’s raining that day and get a reminder text.

import requests
import bs4
from twilio.rest import TwilioRestClient

def rain_check():
    """Check weather.gov to see if it is likely to rain today."""
    url = 'https://weather.com/en-GB/'
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautfulSoup(res.text, 'lxml')
    weather_elem = soup.select('#styles-xz0ANuUJ_nowBlurb_17gst')
    weather = weather_elem[0].getText()

    if 'rain' in weather.lower():
        return True

account_sid = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
auth_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
my_number = '+44 75xxxxxxxxxxx'
twilo_number = '+xxxxxxxxxxxxxxxxxx' #use this link for more info https://www.youtube.com/watch?v=knxlmCVFAZI&ab_channel=Twilio

def text_myself(message):
    """ Use Twilo to text the message argument to your phone"""
    twilo_cli = TwilioRestClient(account_sid, auth_token)
    twilo_cli.messages.create(body=message, from_=twilo_number, to=my_number)

if rain_check():
    text_myself('Remember to take an umbrella.')
