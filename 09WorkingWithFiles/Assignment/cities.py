import json
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

f = open("../data/1000-largest-us-cities.json", "r")
cities = json.load(f)
f.close()

list_of_cities = ""
for city in cities:
    if city["state"] == "Kansas":
        list_of_cities = list_of_cities + city["city"]

#print("All large cities in Kansas:", list_of_cities)

f = open("../data/1000-largest-us-cities.json", "r")
cities = json.load(f)
f.close()



longest_city_name = ""
letter_amount = len(city["city"])
max_letters = 0
for city in cities:
    if letter_amount > max_letters:
        max_letters = letter_amount
longest_city_name = (city["city"])

print("The city with the longest name is:", longest_city_name, letter_amount)