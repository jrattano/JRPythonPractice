"""
Task:
Write a Python function named get_city_population that takes two parameters.

populations - a dictionary representing city populations.

city - a string representing the name of the city.

The function should:

Return the population of the specified city if it's found in the dictionary.

Raise a KeyError with a clear error message if the city is not found.

Use a try-except block inside the function to handle the KeyError with a custom error message.

Tips:
Use raise KeyError() to explicitly raise the exception with your custom error message.

Do not use any type hints when declaring the function.

Example 1:
city_populations = {"New York": 8336817, "Los Angeles": 3979576, "Chicago": 2679044}

city_name = "Tampa"

This should yield a KeyError stating 'City "Tampa" not found in population data.'

Example 2:
city_populations = {"New York": 8336817, "Los Angeles": 3979576, "Chicago": 2679044}

city_name = "New York"

This should yield the population of New York, which is 8336817 in this dictionary.
"""

city_populations = {"New York": 8336817, "Los Angeles": 3979576, "Chicago": 2679044}

def get_city_population(populations, city):
    if city not in populations:
        raise KeyError(f'City "{city}" not found in population data.')
    return populations[city]
try:
    print(get_city_population(city_populations, "New York"))
except KeyError as e:
    print(e)  # This will print: City "Tampa" not found in population data.

try:
    print(get_city_population(city_populations, "Tampa"))
except KeyError as e:
    print(e)  # This will print: City "Tampa" not found in population data.