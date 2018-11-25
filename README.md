POST /seller/register  <br />
email  <br />
password  <br />

POST /seller/add_card   #requires token header <br />
cardNumber  <br />
expirationYear  <br />
expirationMonth  <br />
cvc  <br />

POST /seller/login #returns token<br /> 
email <br />
password <br />

POST /cards/add_card
cardNumber  <br />
expirationYear  <br />
expirationMonth  <br />
cvc  <br />


GET /beacon #returns all seller beacons requires token header

POST /beacon # requires token header <br />
beacon_id <br />
beacon_token <br />

GET /checkout/<ObjectId:beacon_id> <br />
 returns data about single beacon and checkout assigned to id\t<br />

POST /checkout/<ObjectId:beacon_id> #requires token header <br />
value <br />
updates checkout to this value



api.add_resource(Beacon, '/beacon', resource_class_kwargs={'mongo': mongo})
api.add_resource(Checkout, '/checkout/<ObjectId:beacon_id>',
                 resource_class_kwargs={'mongo': mongo})