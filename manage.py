from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify
import os
from app import create_app
from flask.ext.script import Manager
import sys
sys.path.append("/home/zack/Desktop/HLTH/app/default/keywords")
import speech


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
api = Api(app)

CORS(app)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

