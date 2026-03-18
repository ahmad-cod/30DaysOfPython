# Exercises: Level 3
from countries import COUNTRY_LIST
countries_with_land = []
for country in COUNTRY_LIST:
  if 'land' in country:
    countries_with_land.append(country)
print(countries_with_land)
#     Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
#     This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits = ['banana', 'orange', 'mango', 'lemon']
# reverse_fruits = []
# for i in range(len(fruits) - 1, -1, -1):
#   reverse_fruits.append(fruits[i])
# print(reverse_fruits)

#     Go to the data folder and use the countries_data.py file.

#         What are the total number of languages in the data
#         Find the ten most spoken languages from the data
#         Find the 10 most populated countries in the world
from countries_data import COUNTRIES_DATA
languages = []
for country in COUNTRIES_DATA:
  for language in country['languages']:
    if language not in languages:
      languages.append(language)
print(f'Total number of languages: {len(languages)}')
