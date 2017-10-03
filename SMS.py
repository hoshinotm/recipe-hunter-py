from twilio.rest import Client
from recipe_hunter.Twilio import TwilioAccess

class SMS(TwilioAccess):

    def send(self, to_number, text):
        TwilioAccess.send_sms(to_number,text)


