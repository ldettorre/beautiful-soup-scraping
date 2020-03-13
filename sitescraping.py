import requests
from bs4 import BeautifulSoup
from csv import writer

# We specify the site we want to scrape below. 
response = requests.get("https://ldettorre.github.io/portfolio/")

soup = BeautifulSoup(response.text, "html.parser")

# Each skill section in the site is seperated via col-sm-4 so that's what we'll use to select them by.
skills = soup.select(".col-sm-4")

# Below creates a file with our chosen name and declares the headers we want to use.
with open("data.csv", "w") as csv_file:
    csv_writer = writer(csv_file)
    headers = ["Title", "Description", "Skill Name"]
    csv_writer.writerow(headers)

# It then iterates over each skill and writes the data to a row.
    for skill in skills:
        title = skill.find(class_="skill-title").get_text() 
        desc = skill.find(class_="skill-description").get_text()
        skill_name = skill.select(".skill-name")[0].get_text()
        csv_writer.writerow([title, desc, skill_name])
    