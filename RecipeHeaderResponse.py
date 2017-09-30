import sys

class RecipeHeaderResponse(object):
    # num_recipes = -1
    # recipe_header_list = []
    def __init__(self, response):
        self.num_recipes = response.get("count")
        self.recipe_header_list = response.get("recipes")
    def get_num_recipes(self):
        return self.num_recipes
    def get_recipe_header_list(self):
        return self.recipe_header_list

