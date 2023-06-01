import bs4 as bs
from bs4 import BeautifulSoup, CData
import csv
import lxml
from lxml import *

def getEvents():
    mydb = mysql.connector.connect(
    host="sql.freedb.tech",
    user="freedb_josephine",
    passwd="amyC%zk5m&WsXjm",
    database="freedb_scraper"
)
mycursor = mydb.cursor()

vf = urllib.request.urlopen('https://www.vexforum.com/posts.rss').read()
new_hash = hashlib.md5(str(vf).encode('utf-8')).hexdigest()
vf_html = BeautifulSoup(requests.get(
    'https://www.vexforum.com').text, 'html5lib')
# vf_html = BeautifulSoup(vf, 'html.parser')
vf_xml = BeautifulSoup(vf, 'lxml')