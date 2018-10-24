
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import json


app = Flask(__name__)
HIFA = Api(app)


class APP_(Resource):
	pass

class RASA_(Resource):
	pass
	
class GOOGLE_(Resource):
	pass

class AMZN_(Resource):
	pass


HIFA.add_Resource(APP_, "hifa/android/")
HIFA.add_Resource(RASA_, "hifa/rasa/")
HIFA.add_Resource(GOOGLE_, "hifa/googleassistant/")
HIFA.add_Resource(AMZN_, "hifa/amazonalexa/")



if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 8080)
