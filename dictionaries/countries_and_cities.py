"""
Given a list of countries and cities of each country, then given
the names of the cities. For each city print the country in
which it is located.
"""

# get num of countries
country_num = int(input())
# create dictionary
# country_and_cities[country] = list_of_cities
country_and_cities = {}

for i in range(country_num):
    country, cities = input().split(" ", 1)
    cities = cities.split()
    country_and_cities[country] = cities

# get number of cities
city_num = int(input())
# get city names
for i in range(city_num):
    user_city = input()

    for country, city in country_and_cities.items():
        if user_city in city:
            print(country)
            break