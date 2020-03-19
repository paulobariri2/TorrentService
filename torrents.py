import os

class Transmission:

    def __init__(self, magnet):
        self.magnet = magnet
    
    def startDownload(self):
        pid = os.spawnlp(os.P_NOWAIT, "transmission-cli", "transmission-cli", "-f", "/home/paulo/Documents/python/TorrentService/killtransmission.sh", self.magnet)
        return {"magnet":self.magnet, "pid":pid}

