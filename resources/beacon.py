from flask_restful import reqparse, Resource
from common.parsers import beacon_parser_seller
# from python_shared.validators import beacon
from common.token import TokenValidator
from bson.json_util import dumps

class Beacon(Resource):
    def __init__(self, **kwargs):
        self.mongo = kwargs['mongo'].db

    def post(self):
        args = beacon_parser_seller.parse_args()
        token = TokenValidator(args['token'], self.mongo)
        if token.is_valid():
            del args['token']
            args['seller'] = token.user['_id']
            args['value'] = 0.0
            self.mongo.Beacons.insert_one(args)
            return 200
        else:
            return 403

    def get(self):
        args = beacon_parser_seller.parse_args()
        token = TokenValidator(args['token'], self.mongo)
        if token.is_valid():
            del args['token']
            beacons = self.mongo.Beacons.find({'seller': token.user['_id']}, {'_id': 0, 'seller': 0})
            return [b for b in beacons], 200
        return 403
















