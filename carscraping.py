import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get("https://www.motorcheck.ie/free-car-check/?vrm=07D54140")

soup = BeautifulSoup(response.text, "html.parser")

car_summary = soup.select(".report-summary")

print(car_summary)


