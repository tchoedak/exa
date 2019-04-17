import os


from_ = 'USD'
to = 'CNY'
threshold = 0.68
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
RECEIVER_NUMBER = os.environ.get('RECEIVER_NUMBER')
TWILIO_NUMBER = os.environ.get('TWILIO_NUMBER')


class URL(object):

    def __init__(self, from_, to):
        self.from_ = from_
        self.to = to
        self.url = f'https://www.x-rates.com/calculator/?from={from_}&to={to}&amount=1'
