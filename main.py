import requests
import smtplib
import os

API_KEY = os.environ['API_KEY']
EXCLUDE = "daily,current,minutely"
MY_EMAIL = os.environ['MY_EMAIL']
PASSWORD = os.environ['PASSWORD']

LAT = 13.072090
LNG = 80.201859

response = requests.get(url=f"https://api.openweathermap.org/data/2.5/onecall?lat={LAT}&lon={LNG}&exclude={EXCLUDE}&appid={API_KEY}")
response.raise_for_status()

data = response.json()["hourly"][:12]
# print(data)

will_rain = False

for hour in data:
    data1 = int(hour["weather"][0]["id"])
    if data1 < 700:
        will_rain = True

if will_rain:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"It will rain today, Bring your umbrella.")
else:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Today it will not rain, it will be sunny or cloudy today.")
