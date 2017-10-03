
import string
from recipe_hunter import Digest

###################
# digest()
# Return a digest string for the given password string
# TODO; Implement
#
def digest(password_string):
    return password_string

class Password(object):
    def __init__(self, password_string):
        self.digest = Digest(password_string).generate()
    def digest(self):
        return self.digest
