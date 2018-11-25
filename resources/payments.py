from flask_restful import reqparse, Resource
# from common.parsers import seller_parser, seller_card_parser
# from common.validators import validate_seller, validate_card
# from common.token import TokenValidator
from common.parsers import payment_parser
import requests


class Payments(Resource):
    def __init__(self, **kwargs):
        self.mongo = kwargs['mongo'].db

    def post(self):
        args = payment_parser.parse_args()
        beacon = self.mongo.Beacons.find_one_or_404({'beacon_token': args['beacon_token']})
        del args['beacon_token']
        seller = self.mongo.Sellers.find_one({'_id': beacon['seller']})
        payload = {
            'cardNumber': args['cardNumber'],
            'sellerCard': seller['cards'][0]['cardNumber'],
            'value': beacon['value'],
        }
        resp = requests.post('localhost:3000', data=payload)
        return resp.json(), 200




