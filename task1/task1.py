import requests as rqst
from bs4 import BeautifulSoup

content = str(rqst.get("https://www.lipsum.com/").content)

soup = BeautifulSoup(content, 'html.parser')

headerList = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

completeString = ""
for h in headerList:
    completeString += str(h) + "\n"

with open("task1/headers.txt", "w") as f:
    f.write(completeString)
