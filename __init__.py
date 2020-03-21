from flask import Flask
from flask_restful import Resource, Api, reqparse
from .torrents import Transmission
from .torrents import isDownloadRunning
from .torrents import getMagnetLinkFromPage

app = Flask(__name__)

api = Api(app)

class Download(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('url', required=True)
        args = parser.parse_args()
        
        url = args['url']
        magnetLink = getMagnetLinkFromPage(url)
        transm = Transmission(magnetLink)
        downloadInfo = transm.startDownload()
        downloadInfo['url'] = url
        return , 201

class DownloadStatus(Resource):
    def get(self, pid):
        status = {}
        status['pid'] = pid
        status['status'] = "Running" if isDownloadRunning(int(pid)) else "Stopped"
        return status

api.add_resource(Download, '/download')
api.add_resource(DownloadStatus, '/download/<string:pid>')