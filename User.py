from recipe_hunter import Digest

class User(object):

    def generate_password_digest(self, password):
        return Digest.generate(password)

    def __init__(self, name, password):
        self.name = name.lowercase()
        self.pasword_digest = self.generate_password_digest(password)

    def is_authentic(self, User):
        self.name = User.name
        self.pasword_digest = User.pasword_digest

