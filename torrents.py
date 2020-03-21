import os
import psutil
import requests
from bs4 import BeautifulSoup

TORRENTSITE = "https://1337x.to/"

def isDownloadRunning(pid):
    notRunningStatus = [psutil.STATUS_ZOMBIE, psutil.STATUS_DEAD]
    try:
        p = psutil.Process(pid)
        if p.status() in notRunningStatus:
            return False
    except (psutil.NoSuchProcess, psutil.ZombieProcess):
        return False
    
    return True

def isMagnetLinkTag(tag):
    return tag.name == 'a' and "Magnet Download" in tag.text

def getMagnetLinkFromPage(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, 'html.parser')
    a = soup.find(isMagnetLinkTag)
    if a and a.get('href'):
        return a['href']
    else:
        raise Exception("Magnet link not found!")

class Transmission:

    def __init__(self, magnet):
        self.magnet = magnet
    
    def startDownload(self):
        pid = os.spawnlp(os.P_NOWAIT, "transmission-cli", "transmission-cli", "-f", "/home/paulo/Documents/python/TorrentService/killtransmission.sh", self.magnet)
        return {"magnet":self.magnet, "pid":pid}
