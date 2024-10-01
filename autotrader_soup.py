import requests
from bs4 import BeautifulSoup

URL = "https://www.autotrader.com/cars-for-sale/port-st-lucie-fl"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="srp-listings")
cars = results.find_all("div", class_="col-xs-12 col-sm-4 display-flex")

for car in cars:
    car_title = car.find("h3", class_="text-bold text-size-400 link-unstyled")
    car_price = car.find("div", class_="text-size-600 text-ultra-bold first-price")
    #car_mileage =
    
    #print(car, end="\n"*2)
    print(car_title)
    print(car_price)
    print()
#print(results.prettify)