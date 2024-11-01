import HolidayClass as hld
import requests
import json

country = input("Enter country (us, ua): ")
contetnt = requests.get("https://date.nager.at/api/v3/publicholidays/2024/" + country).content
holidaysJson = json.loads(contetnt)

holidayList = []
for holiday in holidaysJson:
    holidayList.append(hld.Holiday(holiday['date'], holiday['name']))

with open("task2/holidays.txt", "w", encoding='utf-8') as file:
    finalString = ""
    for h in holidayList:
        finalString += str(h) + "\n"
    file.write(finalString)
