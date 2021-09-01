import flask
from flask import request, jsonify
app = flask.Flask(__name__)
app.config["DEBUG"] = True
@app.route('/', methods=['POST'])
def api_home():
     return "paths '/api/v1/changeUserSettings'"

@app.route('/api/v1/changeUserSettings', methods=['POST'])
def api_cards():
    if 'username' in request.args:
        name = request.args['name']
    else:
        return "Error: No username field provided. Please specify an accountType,name,firstname and adress."
    if 'name' in request.args:
        name = request.args['name']
    else:
        return "Error: No name field provided. Please specify an accountType,name,firstname and adress."
    if 'firstname' in request.args:
        name = request.args['name']
    else:
        return "Error: No firstname field provided. Please specify an accountType,name,firstname and adress."
    if 'adress' in request.args:
        name = request.args['name']
    else:
        return "Error: No adress field provided. Please specify an accountType,name,firstname and adress."
    if 'accountType' in request.args:
        type = request.args['accountType']
    else:
        return "Error: No type field provided. Please specify an accountType,name,firstname and adress. The type can be either user or reader"
    if type == 'admin':
        return "Good job!! Welcome to admin portal, Yo The BOSS!!!"
    else:
        return "account settings saved"
app.run(host="0.0.0.0",port="5008")