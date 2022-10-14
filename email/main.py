from random import random
import smtplib
# DOESN'T work with gmail as less secure app access removed by google

def get_quotes():
    with open("email/quotes.txt") as file:
        content = file.readlines()
        return content


QUOTES = get_quotes()

import datetime as dt
import random

today = dt.datetime.now().weekday

if today != 0:
    quote = random.choice(QUOTES)
    print(quote)








