import flask
from flask import request, jsonify
 
app = flask.Flask(__name__)
app.config["DEBUG"] = True
 
# Create some test data for our catalog in the form of a list of dictionaries.
optType = [
    {'id': 0,
     'title': 'Operation  Rocket',
     'place': 'Bangladesh',
     'description': 'Successfull Navy operation ',
     'year': '1992'},
{'id': 1,
     'title': 'Operation Jackpot',
     'place': 'Sri Lanka',
     'description': 'secret Army operation ',
     'year': '1990'},
{'id': 2,
     'title': ' black box',
     'place': 'China',
     'description': 'Conqured wihout any arms and ammunations',
     'year': '2019'}
]
 
# Create some test data with an extra record for extra info for chief.
optType_detail = [
    {'id': 0,
     'title': 'CID-999',
     'author': 'Navy Operation',
     'description': 'Andaman Nicobar',
     'year': '1992'},
{'id': 1,
     'title': 'Casino ',
     'place': 'NIA',
     'description': 'Drug Mafia',
     'year': '2018'},
{'id': 2,
     'title': 'Quantom',
     'place': 'Lakshadweep',
     'description': 'Safety rescue operation.',
     'year': '2016'},
{'id': 3,
     'title': 'Operation Cocoon',
     'place': 'TN',
     'description': 'Assasination',
     'year': '2006'}
]
 
# A route to return all of the available entries in army.
@app.route('/api/v1/resources/opt/all', methods=['GET'])
def api_all():
    return jsonify(optType)
 
@app.route('/api/v2/resources/opt', methods=['GET'])
def api_id():
    
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
 
    #empty list
    results = []
 
    # For Loop haku through the data and match results that fit the requested unique ID
    for opt in optType_detail:
        if  opt['id'] == id:
            results.append(opt)

    return jsonify(results)
 
app.run(host="0.0.0.0",port="5001")