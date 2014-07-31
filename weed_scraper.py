#/usr/bin/python

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

	c.writerow([
		state,
		clean(cell[4]),
		clean(cell[5]),
		clean(cell[7]),
		clean(cell[8]),
		clean(cell[10]),
		clean(cell[11])
	])

def clean(num):
	return str(num.get_text()).replace("$", "")

with open('states.csv', 'r') as states:
	states_read = csv.reader(states, delimiter=',', quotechar='"')
	for row in states_read:
		scrape(row[0])
