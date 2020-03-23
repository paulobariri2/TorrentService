import os
import psutil
import requests
from bs4 import BeautifulSoup
import json

TORRENTSITE = "https://1337x.to%s"
SEARCHURL = "https://1337x.to/search/%s/%d/"
KILL_SCRIPT = os.environ['KILL_SCRIPT']
DOWNLOAD_FOLDER = os.environ['DOWNLOAD_FOLDER']

headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"
}

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

def getInfoFromHtmlTableRow(row):
    info = {}
    for td in row.find_all('td'):
        if not td.get('class'):
            continue
        if 'name' in td['class']:
            for a in td.find_all('a'):
                if a.get('class'):
                    continue

                if a.get('href'):
                    info['url'] = TORRENTSITE % a['href']
                    info['name'] = a.text

        if 'seeds' in td['class']:
            info['seeds'] = td.text
        if 'coll-date' in td['class']:
            info['date'] = td.text
        if 'size' in td['class']:
            info['size'] = td.text
        if 'uploader' in td['class']:
            info['uploader'] = td.text
    return info

def getJsonFromHtmlTable(table):
    body = table.find('tbody')
    if not body:
        raise Exception("Table has no tbody tag!")

    data = []
    for row in body.find_all('tr'):
        torrentInfo = getInfoFromHtmlTableRow(row)
        if torrentInfo:
            data.append(torrentInfo)
    return data

def searchTorrents(searchString, page):
    resp = requests.get(SEARCHURL % (searchString, page), headers=headers)
    soup = BeautifulSoup(resp.content, 'html.parser')
    table = soup.find('table')
    if not table:
        raise Exception("No result found for %s, page %d." % (searchString, page))

    return getJsonFromHtmlTable(table)

def searchTorrentsPages(searchString, pages=[1,2,3]):
    data = []
    for i in pages:
        data += searchTorrents(searchString, i)
    return data

class Transmission:

    def __init__(self, magnet):
        self.magnet = magnet
    
    def startDownload(self):
        pid = os.spawnlp(os.P_NOWAIT, "transmission-cli", "transmission-cli", "-f", os.path.join(KILL_SCRIPT, "killtransmission.sh"), self.magnet)
        return {"magnet":self.magnet, "pid":pid}
