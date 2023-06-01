import bs4 as bs
from bs4 import BeautifulSoup, CData
import urllib.request
import csv
import lxml
from lxml import *

def getEvents():
    events = urllib.request.urlopen('https://www.robotevents.com/robot-competitions/vex-robotics-competition').read()
    new_hash = hashlib.md5(str(vf).encode('utf-8')).hexdigest()
    events_html = BeautifulSoup(requests.get(
        'https://www.vexforum.com').text, 'html5lib')
    events_xml = BeautifulSoup(vf, 'lxml')