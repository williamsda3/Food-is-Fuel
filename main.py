# anything dealing with API has requests library
# importing the request module
import requests

# used to access the API (through Davids account)
# Creating a function to return recipe suggestions based on ingredients passed
API_KEY = '33edc764ecf341ef9b75704f6297816e'

# takes in param of ingredients
def get_recipe_suggestions(ingredients):
    # not an actual website, just an API call
    endpoint = 'https://api.spoonacular.com/recipes/complexSearch'
    params = {
        'apiKey': API_KEY,
        'includeIngredients': ','.join(ingredients),
        'number': 3  # Number of recipe suggestions to retrieve
    }

    #get request is when youre trying to get information from an API, and needs an endpoint and parameters
    #first parameter is the API call, second paramater is what is required for the API
    #call (varies based on what you're trying to do)
    response = requests.get(endpoint, params=params)
    #status code 200 means success
    if response.status_code == 200:
        #this is what the API gives us back
        recipe_suggestions = response.json()
        #then we manipulate the json file to get the information we actually care about
        for recipe in recipe_suggestions['results']:
            recipe_title = recipe['title']
            recipe_id = recipe['id']
            print(f"Recipe: {recipe_title} (ID: {recipe_id})")
    else:
        print('Failed to retrieve recipe suggestions.')

# pass this array into recipe suggestions. 
# it is making a recipe suggestion based on the parameter you give
ingredients = []
recipe1 = input('Enter desired ingredients: ')
recipe2 = input('Enter desired ingredients: ')

ingredients.append(recipe1)
ingredients.append(recipe2)

get_recipe_suggestions(ingredients)
