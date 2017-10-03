from twilio.rest import Client

class TwilioAccess(object):

    def __init__(self,account_sid,auth_token):
        self account_sid = account_sid
        self.auth_token = auth_token
        self.client = Client(account_sid, auth_token)

    # Return a randomly-selected number from a pool of possible texting origin
    # numbers
    # TODO: Implement
    def get_random_origin_number(self):
        return "XXXXXXXXXX"

    def send_sms(self,to_number,text):
        from_number = self.get_random_origin_number()
        self.client.api.account.messages.create( \
                to = to_number, \
                from_= from_number, \
                body = text)




