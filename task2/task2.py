from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

class Holiday(object):
    date = ""
    name = ""
    
    def __init__(self, date, name):
        self.date = date
        self.name = name
    
    def __str__(self):
        s = ""
        s += str(self.name) + ", "
        s += str(self.date)
        return s

def getListOfholidays(country):
    holidayList = []
    
    chromeOptions = Options()
    chromeOptions.add_argument("--headless")
    driver = webdriver.Chrome(options=chromeOptions) 
    url = "https://date.nager.at/PublicHoliday/" + country
    driver.get(url)
    time.sleep(2)
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    holidayContainers = soup.find_all('div', class_=["d-flex", "flex-row publicHolidayList", "publicHolidayListPast"])
    holidayDatesList = holidayContainers[0].find_all_next('div', class_=["col-4"])
    holidayNamesList = holidayContainers[0].find_all_next('div', class_=["col-3"])
    for i in range(1, len(holidayDatesList)):
        holidayList.append(Holiday(holidayDatesList[i].text.strip(), holidayNamesList[i].text.strip()))
        
    driver.quit()
    
    return holidayList

country = input("Enter country (United-States, Ukraine): ")
listOfHolidays = getListOfholidays(country)

with open("task2/holidays.txt", "w", encoding='utf-8') as file:
    finalString = ""
    for h in listOfHolidays:
        finalString += str(h) + "\n"
    file.write(finalString)
    