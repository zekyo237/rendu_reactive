from flask import Flask,Response,request
from flask_jwt_extended import JWTManager,get_jwt_identity,jwt_required
import json
from flask.json import jsonify
from resources.routes import initialize_routes
from flask_restful import Api
from flask_cors import CORS
import os 
app = Flask(__name__)
@app.route("/api/user",methods=["GET"])
@jwt_required()
def protected():
    current_user= get_jwt_identity()
    return jsonify(username=current_user),200
app.secret_key = 't1NP63m4wnBg6nyHYKfmc2TpCOGI4nss'
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api= Api(app)
jwt= JWTManager(app)


initialize_routes(api)



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5001)