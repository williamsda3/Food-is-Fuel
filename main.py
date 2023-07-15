# Importing the request module
import requests

API_KEY = '33edc764ecf341ef9b75704f6297816e'

# Creating a function to return recipe suggestions based on ingredients passed
def get_recipe_suggestions(ingredients):
    endpoint = 'https://api.spoonacular.com/recipes/complexSearch'
    params = {
        'apiKey': API_KEY,
        'includeIngredients': ','.join(ingredients),
        'number': number  # Number of recipe suggestions to retrieve
    }

    response = requests.get(endpoint, params=params)
    if response.status_code == 200:
        recipe_suggestions = response.json()
        for recipe in recipe_suggestions['results']:
            recipe_title = recipe['title']
            recipe_id = recipe['id']
            print(f"Recipe: {recipe_title} (ID: {recipe_id})")
    else:
        print('Failed to retrieve recipe suggestions.')


# Example usage
number = input('Number of recipe suggestions \n>> ')

# Creating an array to hold the ingredients
ingredients = []


recipe1 = input('Enter a desired ingredient: \n>> ')
recipe2 = input('Enter a desired ingredient: \n>> ')

ingredients.append(recipe1)
ingredients.append(recipe2)

get_recipe_suggestions(ingredients)
