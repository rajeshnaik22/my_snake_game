def basic_input_output():
    print("Enter you name")
    my_name = input()
    my_age = input("Enter your age please: ")

    print("Your name and age:", my_name, my_age)
    print(f"Hello {my_name}! You're {my_age} years old")


import datetime as dt
from urllib import response

def date_functions():
    now = dt.datetime.now()
    print(now)
    print(now.year)
    print(now.weekday())

    birth_date = dt.datetime(year=2002,month=1,day=23)
    print(birth_date)

import requests
def api():
    url="http://api.open-notify.org/iss-now.json"
    response = requests.get(url=url)
    response.raise_for_status()
    print(response.json())

    params = {
        "lat":15.388806,
        "lng":74.008884 
    }

    response = requests.get("https://api.sunrise-sunset.org/json",params=params)
    print(response.json())

api()
