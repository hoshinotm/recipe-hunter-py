import sys

class RecipeHeader(object):
    def __init__(self, header_block):
        self.publisher = header_block.get("publisher")
        self.f2f_url = header_block.get("f2f_url")
        self.title = header_block.get("title")
        self.source_url = header_block.get("source_url")
        self.recipe_id = header_block.get("recipe_id")
        self.image_url = header_block.get("image_url")
        self.social_rank = float(header_block.get("social_rank"))
        self.publisher_url = header_block.get("publisher_url")