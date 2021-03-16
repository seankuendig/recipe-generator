import json
from dataclasses import dataclass

import requests
from decouple import config

API_KEY: str = config('KEY')

URL = "https://api.spoonacular.com/mealplanner/generate"


@dataclass(frozen=True)
class RecipeConfiguration:
    diet: str
    exclude: str = ""
    target_calories: int = 2000
    time_frame: str = "day"


def send_request(recipe_configuration):
    # uncomment this part for live demos, else use example data below

    PARAMS = {
        'apiKey': API_KEY,
        'timeFrame': recipe_configuration.time_frame,
        'targetCalories': recipe_configuration.target_calories,
        'exclude': recipe_configuration.exclude,
        'diet': recipe_configuration.diet
    }
    r = requests.get(url=URL, params=PARAMS)
    data = r.json()

    # data = '{"meals": [{"id": 849685, "imageType": "jpg", "title": "Healthy Strawberry Smoothie (Vegan+Dairy Free) + VIDEO", "readyInMinutes": 5, "servings": 2, "sourceUrl": "https://www.platingsandpairings.com/healthy-strawberry-shortcake-smoothie/"}, {"id": 402871, "imageType": "jpg", "title": "Fiesta Loaf", "readyInMinutes": 15, "servings": 6, "sourceUrl": "http://www.tasteofhome.com/Recipes/fiesta-loaf"}, {"id": 572905, "imageType": "jpg", "title": "Banana Pudding : A Little Southern Comfort", "readyInMinutes": 20, "servings": 10, "sourceUrl": "http://www.restlesschipotle.com/2010/12/banana-pudding-recipe-a-little-southern-comfort/"}], "nutrients": {"calories": 1999.89, "protein": 57.11, "fat": 124.47, "carbohydrates": 177.44}}'
    # json_data = json.loads(data)
    return data
