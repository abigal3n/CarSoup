#Only works with the website autotrader.com

import requests
from bs4 import BeautifulSoup

URL = "https://www.autotrader.com/cars-for-sale/port-st-lucie-fl"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="srp-listings")
#cars = results.find_all(class_="col-xs-12 col-sm-4 display-flex")
#car_elements = [div_element.parent.parent.parent for div_element in cars]
#print(len(cars))
repeat = True
#maybe have it iterate until specified number of cars meeting the criteria have been added to a list

while(repeat):
    URL = "https://www.autotrader.com/cars-for-sale/port-st-lucie-fl"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="srp-listings")
    cars = results.find_all(class_="col-xs-12 col-sm-4 display-flex")
    more = input("Would you like more cars? Type more or m for more options")
    if more == "more" or  more == "m":
        for car in cars:
            car_title = car.find("h3", class_="text-bold text-size-400 link-unstyled")
            car_price = car.find("div", class_="text-size-600 text-ultra-bold first-price")
            car_mileage = car.find("div", class_="text-bold text-subdued-lighter margin-top-3")
            comma = ","
            cpt = car_price.text.replace(comma, "")
            print(cpt)
            #if int(cpt) < 3000:
            #print(car, end="\n"*2)
            print("Car: " + car_title.text.strip())
            print("Price: $" + cpt.strip())
            print("Mileage: " + car_mileage.text.strip())
            print()
            #else:
                #print("no cars under 3000")
    else:
        print("Have a nice day")
        break
#print(results.prettify)