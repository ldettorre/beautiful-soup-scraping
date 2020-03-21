import random
from csv import writer
reg_years = ["00","01","02","03","04","05","06","07","08","09","10","11","12","131","132","141","142","151","152","161","162","171","172","181","182","191","192","201"]
counties = ["CE","CN","C","CW","D","DL","G","KE","KK","KY","L","LD","LH","LM","LS","MH","MN","MO","OY","RN","SO","T","WH","W","WX","WW"]

# Random Car Registration Generator
for i in range(2000):
    random_reg_year = str(random.choice(reg_years))
    random_county = str(random.choice(counties))
    random_num = str(random.randrange(1, 94865, 1))
    print( random_reg_year + random_county + random_num)

