#/usr/bin/env python2.5

from bs4 import BeautifulSoup
import requests
import re
import csv
import time

c = csv.writer(open('data/weedprices' + time.strftime("%d%m%Y") + '.csv', 'wb'), quoting = csv.QUOTE_ALL)
c.writerow(['State','HighQ','HighQN','MedQ','MedQN','LowQ','LowQN'])
base_url = 'http://www.priceofweed.com/prices/United-States/'


def scrape(state):

	r = requests.post(base_url + state + '.html')
	soup = BeautifulSoup(r.text)

	title = soup.findAll("title")
	state = re.sub(r' Weed Prices - PriceOfWeed.com', '', title[0].get_text())

	content = soup.findAll("table", {"class":"avg_box"})
	cell = content[0].findAll("td")

	d = {
		'state' : state,
		'highq' : cell[4].get_text(),
		'highq_n' : cell[5].get_text(),
		'mediumq' : cell[7].get_text(),
		'mediumq_n' : cell[8].get_text(),
		'lowq' : cell[10].get_text(),
		'lowq_n' : cell[11].get_text()
	}
	c.writerow([d['state'],d['highq'],d['highq_n'],d['mediumq'],d['mediumq_n'],d['lowq'],d['lowq_n']])

with open('states.csv', 'r') as states:
	states_read = csv.reader(states, delimiter=',', quotechar='"')
	for row in states_read:
		scrape(row[0])
