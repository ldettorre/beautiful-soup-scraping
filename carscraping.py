import requests, os
from bs4 import BeautifulSoup
from csv import writer


# Important note: If registration does not exist, code will break and throw this error "IndexError: list index out of range"
for i in range(5):
    response = requests.get("https://www.cartell.ie/ssl/servlet/beginStarLookup?registration=181C"+str(i))
    soup = BeautifulSoup(response.text, "html.parser")
    
    file_exists = os.path.isfile("car_data.csv")
    with open("car_data.csv", "a") as csv_file:
        csv_writer = writer(csv_file)
        headers = ["Registration","Make","Model","Description","Engine Capacity"]
        if not file_exists:
            csv_writer.writerow(headers)

        
        try:
            registration = soup.select("td")[0].get_text()
            make = soup.select("td")[1].get_text()
            model = soup.select("td")[2].get_text()
            desc = soup.select("td")[3].get_text()
            engine_cc = soup.select("td")[4].get_text()
            csv_writer.writerow([registration, make, model, desc, engine_cc])
        except IndexError:
            registration = "N/A"
            make = "N/A"
            model = "N/A"
            desc = "N/A"
            engine_cc = "N/A"
            csv_writer.writerow([registration, make, model, desc, engine_cc])

