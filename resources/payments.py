from flask_restful import reqparse, Resource
# from common.parsers import seller_parser, seller_card_parser
# from common.validators import validate_seller, validate_card
# from common.token import TokenValidator
from common.parsers import payment_parser

import requests, datetime

class Payments(Resource):
    def __init__(self, **kwargs):
        self.mongo = kwargs['mongo'].db

    def post(self):
        args = payment_parser.parse_args()
        beacon = self.mongo.Beacons.find_one_or_404({'beacon_token': args['beacon_token']})
        seller = self.mongo.Sellers.find_one({'_id': beacon['seller']})
        payload = {
            'cardNumber': args['cardNumber'],
            'sellerCard': seller['cards'][0]['cardNumber'],
            'value': beacon['value'],
        }
        resp = requests.post('http://localhost:3000/payment', data=payload) #NOT SURE IT WORKS !!!!
        history_dict = resp.json()
        history_dict['cardNumber'] = args['cardNumber']
        history_dict['value'] = beacon['value']
        self.mongo.Sellers.update({'_id': beacon['seller']}, {'$push': {'history': history_dict}})
        card_history = {
            'timestamp': datetime.datetime.now(),
            'value': beacon['value']
        }
        self.mongo.Cards.update({'cardNumber': args['cardNumber']}, {'$push': {'history': card_history}})
        self.mongo.Beacons.update({'beacon_token': args['beacon_token']}, {'value': 0.0, 'beacon_token': args['beacon_token']})
        return 200




