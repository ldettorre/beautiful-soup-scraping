import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get("https://www.motorcheck.ie/free-car-check/?vrm=07D54140")

soup = BeautifulSoup(response.text, "html.parser")

car_summary = soup.select(".report-summary")
# print(car_summary)

# The function below takes a url address as a string and limit as an integer.
# The loop will run upto the set limit -1 as it's a range. 
# Each iteration will print the url with that iterations number concatenated to the end.

def incrmenting_url(url, limit):
    for i in range(limit):
        print(url + str(i))

incrmenting_url("https://www.motorcheck.ie/free-car-check/?vrm=07D",5)