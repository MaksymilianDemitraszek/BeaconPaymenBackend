from resources.account import Seller, SellerCard
from resources.login import Login
from resources.card import Card
from resources.beacon import Beacon
from resources.checkout import Checkout


from flask import Flask
from flask_pymongo import PyMongo
from flask_restful import Api



app = Flask(__name__)
api = Api(app)
# app.config["MONGO_URI"] = "mongodb://localhost:27017/Visa"
# app.config["MONGO_URI"] = "mongodb://mo1243_test:7QwnNzA84Pz3DySAI4XW@91.185.184.123:27017/?authSource=mo1243_test&authMechanism=SCRAM-SHA-1"
app.config["MONGO_URI"] = "mongodb://mo1243_test:7QwnNzA84Pz3DySAI4XW@91.185.184.123:27017/mo1243_test"
mongo = PyMongo(app)


api.add_resource(Seller, '/seller/register', resource_class_kwargs={'mongo': mongo})
api.add_resource(SellerCard, '/seller/add_card', resource_class_kwargs={'mongo': mongo}) #requires token header
api.add_resource(Login, '/seller/login',  resource_class_kwargs={'mongo': mongo})

api.add_resource(Card, '/cards/add_card', resource_class_kwargs={'mongo': mongo})


api.add_resource(Beacon, '/beacon', resource_class_kwargs={'mongo': mongo})
api.add_resource(Checkout, '/checkout/<ObjectId:beacon_id>',
                 resource_class_kwargs={'mongo': mongo})



if __name__ == "__main__":
    app.run()