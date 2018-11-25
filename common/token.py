class TokenValidator():

    def __init__(self, token, mongo):
        self.token = token
        self.mongo = mongo
        self.user = None

    def is_valid(self):
        token_obj = self.mongo.Tokens.find_one({'token': self.token})
        if token_obj:
            self.user = self.mongo.Sellers.find_one({'_id': token_obj['user']['_id']})
            return True
        else:
            return False
