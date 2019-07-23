# $ sudo -H pip install BeautifulSoup
# $ sudo -H pip install Requests
# uses python 2.7 soz

import requests
import re
import sys
import time
import Tkinter
import tkMessageBox
import os
from BeautifulSoup import BeautifulSoup

url = 'https://cookiefactorylofts.com/lofts/'
regex = "(data\.addRows)((.|\n)*)(('1',1,)|('2',1,))"
regex_escaped = re.escape(regex)

def scrape():
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html)
    stringo = soup.findAll('script')
    match = re.search(regex_escaped, stringo[6].prettify())
    if match:
        print "Match found!"
        tkMessageBox.showinfo("Found", "I found a 1br1b or 2br1b apartment available!!!!")
    print "Match not found, SAD!"
    tkMessageBox.showinfo("Not Found", "No 1br1b or 2br1b apartments available, SAD!")

if __name__ == '__main__':
    scrape()
