from twilio.rest import Client
from recipe_hunter.Twilio import TWILIO_IDENTIFIER

class Texting(object):
    account_sid = TWILIO_IDENTIFIER.ACCOUNT_SID
    auth_token = TWILIO_IDENTIFIER.AUTH_TOKEN
    client = Client(account_sid, auth_token)
    from_number = TWILIO_IDENTIFIER.FROM_NUMBER

    def send(self, to_number, text):

        self.client.api.account.messages.create( \
                to = to_number, \
                from_= self.from_number, \
                body = text)
