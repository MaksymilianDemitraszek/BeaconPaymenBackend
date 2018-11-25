from flask_restful import reqparse, Resource
from Visa.common.parsers import seller_parser
import random, string
# from python_shared.validators import beacon


class Login(Resource):
    def __init__(self, **kwargs):
        self.mongo = kwargs['mongo'].db

    def post(self):
        args = seller_parser.parse_args()
        user = self.mongo.Sellers.find_one({'email': args['email'],
                                'password': args['password']})
        if user:
            token_string = ''.join([random.choice(string.ascii_letters + string.digits) for x in range(72)])
            token_object = self.mongo.Tokens.find_one({'user': user})
            if not token_object:
                self.mongo.Tokens.insert_one({'user': user, 'token': token_string})
                return {'token': token_string}, 200
            return {'token': token_object['token']}, 200
        else: return 403





