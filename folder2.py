from bs4 import BeautifulSoup
import requests, urllib, re, sys, os
import http

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3', 'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8', 'Connection': 'keep-alive'
}
url = input("URL: ")
fileName = url.strip("https://drive.google.com/drive/u/0/folders/") + ".txt"
regex = r'\[.*?\]'
sys.stdout = open(fileName, 'w', encoding="utf-8")
req = urllib.request.Request(url, headers = header)
html = urllib.request.urlopen(req).read()
bsoup = BeautifulSoup(html, "html.parser")
link = bsoup.findAll("c-wiz", {"class": "pmHCK"})
for i in link:
    title = i.find("div", {"class": "Q5txwe"}).text.strip(".mp3")
    title = re.sub(regex, '', title)
    while title.startswith(" "):
        title = title[1:]
    #fileType = i.find("div", {"class": 'a-c'}).find('img')['src']
    fileURL = "https://docs.google.com/uc?id=" + i.find("div", {"class": "WYuW0e"})['data-id']
    lineString = "{ \'icon\': iconImage, \'title\': \'%s\', \'file\': \'%s\' }," % (title, fileURL)
    print(lineString)
    #print(fileURL)
sys.stdout.close()
    #print(fileType)