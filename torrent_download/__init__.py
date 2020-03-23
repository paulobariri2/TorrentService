from flask import Flask
from flask_restful import Resource, Api, reqparse
from .torrents import Transmission
from .torrents import isDownloadRunning
from .torrents import getMagnetLinkFromPage
from .torrents import searchTorrents
from .torrents import searchTorrentsPages

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
        return downloadInfo, 201

class DownloadStatus(Resource):
    def get(self, pid):
        status = {}
        status['pid'] = pid
        status['status'] = "Running" if isDownloadRunning(int(pid)) else "Stopped"
        return status

class SearchTorrents(Resource):
    def get(self, searchString, page=None):
        if page:
            return searchTorrents(searchString, int(page)), 200
        else:
            return searchTorrentsPages(searchString), 200

api.add_resource(Download, '/download')
api.add_resource(DownloadStatus, '/download/<string:pid>')
api.add_resource(SearchTorrents, '/search/<string:searchString>', '/search/<string:searchString>/page/<string:page>')