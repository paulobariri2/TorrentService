import os

class Transmission:

    def __init__(self, magnet):
        self.magnet = magnet
    
    def startDownload(self):
        os.system("transmission-cli " + self.magnet)
        return {"magnet":self.magnet}


