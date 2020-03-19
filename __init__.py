from flask import Flask
from flask_restful import Resource, Api, reqparse
from .torrents import Transmission

app = Flask(__name__)

api = Api(app)

class Download(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('magnet', required=True)
        args = parser.parse_args()
        
        transm = Transmission(args['magnet'])
        return transm.startDownload(), 201

api.add_resource(Download, '/download')