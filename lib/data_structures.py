spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    the_names = []
    for food in spicy_foods:
        the_names.append(food["name"])
    return the_names    

#Define a function get_spiciest_foods() that takes a list of spicy_foods and returns a list of dictionaries where the heat level of the food is greater than 5.

def get_spiciest_foods(spicy_foods):
    hot_foods = []
    for food in spicy_foods:
        if food["heat_level"] > 5:
            hot_foods.append(food)
    return hot_foods

#Define a function print_spicy_foods() that takes a list of spicy_foods and output to the terminal each spicy food in the following format using print(): Buffalo Wings (American) | Heat Level: 🌶🌶🌶.

#HINT: you can use times (*) with a stringLinks to an external site. to produce the correct number of "🌶" emojis.

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        spice_level = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {spice_level}")

#Define a function get_spicy_food_by_cuisine() that takes a list of spicy_foods and a string representing a cuisine, and returns a single dictionary for the spicy food whose cuisine matches the cuisine being passed to the method.

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if cuisine == food['cuisine']:
            return food

#Define a function print_spiciest_foods() that takes a list of spicy_foods and outputs to the terminal ONLY the spicy foods that have a heat level greater than 5, in the following format:

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        spice_level = "🌶" * food["heat_level"]
        if food['heat_level'] > 5:
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {spice_level}")

#Define a function average_heat_level() that takes a list of spicy_foods and returns an integer representing the average heat level of all the spicy foods in the array. Recall that to derive the average of a collection, you need to calculate the total and divide number of elements in the collection.


def get_average_heat_level(spicy_foods):
    list_length = len(spicy_foods)
    total_spice = 0
    for food in spicy_foods:
        total_spice += food['heat_level']    
    return total_spice / list_length

#Define a function create_spicy_food() that takes a list of spicy_foods and a new spicy_food and returns the original list with the new spicy_food added.


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
