import requests
from bs4 import BeautifulSoup
from csv import writer

# We specify the site we want to scrape below. 
response = requests.get("https://ldettorre.github.io/portfolio/")

soup = BeautifulSoup(response.text, "html.parser")

first_scrape = soup.body.contents

print(first_scrape)