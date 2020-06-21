from torrent_download import TorrentManager 
import sys

tm = TorrentManager()
tm.updateTorrentAsDone(sys.argv[1])
print(tm.resp)