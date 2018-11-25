from flask_restful import reqparse, Resource


card_parser = reqparse.RequestParser()
card_parser.add_argument('cardNumber', required=True)
card_parser.add_argument('expirationYear',  required=True)
card_parser.add_argument('expirationMonth',  required=True)
card_parser.add_argument('cvc', required=True)

seller_card_parser = card_parser.copy()
seller_card_parser.add_argument('token', location='headers')

seller_parser = reqparse.RequestParser()
seller_parser.add_argument('email', required=True)
seller_parser.add_argument('password', required=True)

beacon_parser = reqparse.RequestParser()
beacon_parser.add_argument('beacon_id')
beacon_parser.add_argument('beacon_token')

beacon_parser_seller = beacon_parser.copy()
beacon_parser_seller.add_argument('token', location='headers')

checkout_parser = reqparse.RequestParser()
checkout_parser.add_argument('value', type=float)

checkout_parser_seller = checkout_parser.copy()
checkout_parser_seller.add_argument('token', location='headers')

