from flask_restful import reqparse, Resource
from Visa.common.parsers import card_parser
from Visa.common.validators import validate_card

class Card(Resource):
    def __init__(self, **kwargs):
        self.mongo = kwargs['mongo'].db

    def post(self):
        args = card_parser.parse_args()
        errors = validate_card(args)
        if errors:
            return {'error': errors}, 406
        if self.mongo.Cards.find_one(args):
            return {'error': 'card already exists'}
        self.mongo.Cards.insert_one(args)
        return 203





