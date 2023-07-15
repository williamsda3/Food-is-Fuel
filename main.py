import requests

API_KEY = '33edc764ecf341ef9b75704f6297816e'

def get_recipe_suggestions(ingredients):
    endpoint = 'https://api.spoonacular.com/recipes/complexSearch'
    params = {
        'apiKey': API_KEY,
        'includeIngredients': ','.join(ingredients),
        'number': 1  # Number of recipe suggestions to retrieve
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
ingredients_list = [ 'bread', 'chocolate']
get_recipe_suggestions(ingredients_list)
