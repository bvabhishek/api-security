import flask
from flask import request, jsonify
 
app = flask.Flask(__name__)
app.config["DEBUG"] = True
 
CreditCards = [
{'id': 0,
     'creditCard': '1234567901234',
     'user': 'yuvan',
     'CVV': '677',
     'validUntil': '1992'},
{'id': 1,
     'creditCard': '1234567901235',
     'user': 'Vittal',
     'CVV': '677',
     'validUntil': '2022'},
{'id': 2,
     'creditCard': '1234567901239',
     'user': 'Janesh',
     'CVV': '677',
     'validUntil': '2023'}
]
 
# A route to return all of the available entries in our catalog.
@app.route('/api/v1/shop/cc/all', methods=['GET'])
def api_all():
    return jsonify(CreditCards)
 
app.run(host="0.0.0.0",port="5005")