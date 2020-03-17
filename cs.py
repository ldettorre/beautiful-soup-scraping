import requests, os
from bs4 import BeautifulSoup
from csv import writer

response = requests.get("https://www.cartell.ie/ssl/servlet/beginStarLookup?registration=191D194")

soup = BeautifulSoup(response.text, "html.parser")


with open("car_data.csv", "a") as csv_file:
    csv_writer = writer(csv_file)
    headers = ["Registration","Make","Model","Description","Engine Capacity"]
    csv_writer.writerow(headers)

    registration = soup.select("td")[0].get_text()
    make = soup.select("td")[1].get_text()
    model = soup.select("td")[2].get_text()
    desc = soup.select("td")[3].get_text()
    engine_cc = soup.select("td")[4].get_text()
    csv_writer.writerow([registration, make, model, desc, engine_cc])


# The function below takes a url address as a string and limit as an integer.
# The loop will run upto the set limit -1 as it's a range. 
# Each iteration will print the url with that iterations number concatenated to the end.

def incrmenting_url(url, limit):
    for i in range(limit):
        print(url + str(i))

# incrmenting_url("https://www.cartell.ie/ssl/servlet/beginStarLookup?registration=191D",5)