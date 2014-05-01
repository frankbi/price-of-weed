#!/usr/bin/env python

import csv
import json

FILE = "../data/weedprices31122013.csv";


# returns a dictionary
def process_file(data):
	for each_state in csv.reader(data, delimiter = ',', quotechar = '"')


'''
	for each_state in csv.reader(data, delimiter = ',', quotechar = '"'):
		print each_state
'''

with open(FILE, "r") as data:
	process_file(data)
