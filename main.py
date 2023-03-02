import os

import requests
from twilio.rest import Client
#SMS API credentials
account_sid = "AC36cb5adb80820193a48fa1f09687efc5"
auth_token="1d81140c895c58b9703fac0be45dcac2"
#my Location
MY_LAT=23.7796515
MY_LNG=90.4266307

#weather Data from weather API
url="https://api.openweathermap.org/data/2.5/onecall"
APIparameter={
    "lat": MY_LAT,
    "lon":MY_LNG,
    "appid":"69f04e4613056b159c2761a9d9e664d2",
    "exclude":"current,daily,minutely,daily"

}
response=requests.get(url=url,params=APIparameter)
#print(response.json())

allData=response.json()
hourlyData=allData["hourly"][:12]
rain = False
for singleData in hourlyData:
    weatherID=singleData["weather"][0]["id"]
    if weatherID<700:
        rain=True
# listID=[ for weather in hourlyData]

#Sent SMS by if weather have possiblity of rain
if rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="আজ বৃষ্টি হতে পারে। নিশ্চিত আপনার ছাতা আপনার সাথে আছে নাকি?",
        from_="+13155992828",
        to="+8801767213613"#8801580377643
    )
    print(message.status)
    print("rain")
else:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="আজ বৃষ্টি হবে না । নিশ্চিতে যেতে পারেন  আপনার ছাতা ছাড়া!",
        from_="+13155992828",
        to="+8801767213613"  # 8801580377643
    )
    print(message.status)
    print("Sunny day")


response.raise_for_status()
