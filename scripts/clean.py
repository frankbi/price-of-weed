#/usr/bin/python

'''
MISSION
Why we need to clean the data:

1. The first 200+ days of scraping, numbers were
scraped as strings, with dollars signs

2. The filename convention is horrendous. It's currently
day/month/year, which doesn't sort very well

3. CSVs should be sorted into a folder, by year and month.

'''

import csv
import os


def init():
	files = os.listdir("../data/")
	for row in files:
		print row



if __name__ == "__main__":
	init()