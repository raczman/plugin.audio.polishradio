import xbmcplugin, xbmcgui, xbmcaddon
import urllib2, random, re

resources = xbmc.translatePath(os.path.join(xbmcaddon.Addon('plugins.audio.polishradio').getAddonInfo('path'), 'resources', 'lib' ))
sys.path.append(resources)

from bs4 import *

handle = int(sys.argv[1])
url = "http://sask1-%s.radio.pionier.net.pl:8000" % (random.choice(range(1,5)))

soup = BeautifulSoup(urllib2.urlopen(url).read())

for el in soup.find_all(class_="newscontent"):
    title = unicode(el.find(class_='streamdata').string)
    stream = el.find('a').get('href')
    li = xbmcgui.ListItem(label=title)
    xbmcplugin.addDirectoryItem(handle, url+stream, li, False)
    
xbmcplugin.endOfDirectory(handle)