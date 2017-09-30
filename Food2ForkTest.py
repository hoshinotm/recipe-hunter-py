####
# Given keywords on the command line, searches the Food2Forks
# recipe databaase and prints out recipes with the keywords.
#
# - Prints recipe data in Json dump format; Handles only 1st keyword
#

import sys
from enum import Enum
import json
import requests
from recipe_hunter.RecipeHeaderResponse import RecipeHeaderResponse
from recipe_hunter.RecipeHeader import RecipeHeader


DEFAULT_URL = 'http://food2fork.com/api/search'
DEFAULT_KEYWORD = "sushi"

#################
# Enum Args
# Defines optional command line argument positions
#
class Args(Enum):
    API_KEY_POS = 1
    KEYWORD1_POS = 2

# class CmdLineArgs(object):
#
#     def num_of_params(self):
#         return len(sys.argv)-1
#
#     def script_name(self):
#         return sys.argv[0]
#
#     def param_list(self):
#         if len(sys.argv) > 1:
#             return sys.argv[1:]

#################
# get_api_key()
# Returns a API key from command line arguments
#
def get_api_key() :
    if len(sys.argv) < 2 :
        print( "Error: No API key is provided through command line argument.")
        exit( 100 )
    else :
        return sys.argv[Args.API_KEY_POS.value]

#################
# get_keywords()
# Returns keywords from the command line, or
# a default keyword if none is specified in the command line
#
def get_keywords():
    keywords = list()
    if len(sys.argv) < 3:
        keywords.append( DEFAULT_KEYWORD )
    else:
        keywords = sys.argv[Args.KEYWORD1_POS.value]
    return keywords


###################
# get_recipe_header_list()
# Returns a Json string containing recipe header count and
# recipe header list
def get_recipe_header_list():
    payload = {'key': get_api_key(), 'q': get_keywords()}
    return requests.get(DEFAULT_URL, params=payload)

###################
# create_header_list()
# Create a list of recipe header objects loaded from
# the a response to HTTP get request for recipe headers
# containing a specified keyword
def create_header_list(recipe_header_reponse):
    header_object_list = list()
    for header_info in recipe_header_response.recipe_header_list:
        header_object_list.append(RecipeHeader(header_info))
    return header_object_list

###################
#
#  Main
#
# payload = {'key': get_api_key(), 'q': get_keywords()[0]}
# r = requests.get(DEFAULT_URL, params=payload)
resp_content = get_recipe_header_list().content
dict = json.loads(resp_content)
# print(dict)
recipe_header_response = RecipeHeaderResponse(dict)
# print( "Count: ", recipe_header_response.num_recipes, "Recipes: ", recipe_header_response.recipe_header_list)
header_object_list = list()
header_object_list = create_header_list(recipe_header_response)
print(header_object_list)
# for header in recipe_header_response.recipe_header_list:
#     header_object_list.append( RecipeHeader(header))

# print(json.dumps(r.json(), sort_keys=True, indent=4))




