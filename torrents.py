import os
import psutil

def isDownloadRunning(pid):
    notRunningStatus = [psutil.STATUS_ZOMBIE, psutil.STATUS_DEAD]
    try:
        p = psutil.Process(pid)
        if p.status() in notRunningStatus:
            return False
    except (psutil.NoSuchProcess, psutil.ZombieProcess):
        return False
    
    return True

class Transmission:

    def __init__(self, magnet):
        self.magnet = magnet
    
    def startDownload(self):
        pid = os.spawnlp(os.P_NOWAIT, "transmission-cli", "transmission-cli", "-f", "/home/paulo/Documents/python/TorrentService/killtransmission.sh", self.magnet)
        return {"magnet":self.magnet, "pid":pid}

