from flask_restful import reqparse, Resource
from common.parsers import seller_parser, seller_card_parser, token_parser
from common.validators import validate_seller, validate_card
from common.token import TokenValidator

class Seller(Resource):
    def __init__(self, **kwargs):
        self.mongo = kwargs['mongo'].db

    def post(self):
        args = seller_parser.parse_args()
        errors = validate_seller(args)
        if errors:
            return {'error': errors}, 406
        self.mongo.Sellers.insert_one(args)
        return 203


class SellerCard(Resource):
    def __init__(self, **kwargs):
        self.mongo = kwargs['mongo'].db

    def post(self):
        args = seller_card_parser.parse_args()
        tok_val = TokenValidator(args['token'], self.mongo)
        if tok_val.is_valid():
            errors = validate_card(args)
            if errors:
                return {'error': errors}, 406
            del args['token']
            self.mongo.Sellers.update({'_id': tok_val.user['_id']}, {'$push': {'cards': args}})
            return 200
        else:
            return 403

class History(Resource):
    def __init__(self, **kwargs):
        self.mongo = kwargs['mongo'].db

    def get(self):
        args = token_parser.parse_args()
        tok_val = TokenValidator(args['token'], self.mongo)
        if tok_val.is_valid():
            return tok_val.user['history'], 200
