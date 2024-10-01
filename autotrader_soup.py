#Only works with the website autotrader.com

import requests
from bs4 import BeautifulSoup

URL = "https://www.autotrader.com/cars-for-sale/port-st-lucie-fl"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="srp-listings")
cars = results.find_all(class_="col-xs-12 col-sm-4 display-flex", limit=10)
print(len(cars))

for car in cars:
    car_title = car.find("h3", class_="text-bold text-size-400 link-unstyled")
    car_price = car.find("div", class_="text-size-600 text-ultra-bold first-price")
    car_mileage = car.find("div", class_="text-bold text-subdued-lighter margin-top-3")
    
    #print(car, end="\n"*2)
    print("Car: " + car_title.text.strip())
    print("Price: $" + car_price.text.strip())
    print("Mileage: " + car_mileage.text.strip())
    print()
#print(results.prettify)