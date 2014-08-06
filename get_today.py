#/usr/bin/env python

import csv
import json
import time
import sys
import operator

def init():
	filename = "data/weedprices" + time.strftime("%d%m%Y") + ".csv"
	csvfile = open(filename, "r")
	csvreader = csv.reader(csvfile, delimiter=",")
	data = []
	data.append({
		"info": {
			"dateAbbrev": time.strftime("%m-%d-%Y"),
			"date": time.strftime("%B %d, %Y")
		},
		"summary": {
			"high": get_summ(filename, 1),
			"medium": get_summ(filename, 3),
			"low": get_summ(filename, 5)
		},
		"data": get_row(csvreader)[1:]
	})
	print json.dumps(data, indent=2)

def get_summ(filename, index):
	arr = []
	f = open(filename, "r")
	reader = csv.reader(f, delimiter=",")
	for row in reader:
		try:
			arr.append(float(row[index]))
		except ValueError:
			pass
	return {
		"min": min(arr),
		"max": max(arr),
		"avg": avg(arr)
	}

def avg(arr):
	summation = 0
	for i in arr:
		summation += i
	return "%.2f" % (summation / len(arr))

def get_row(csv):
	arr = []
	for row in csv:
		obj = {
			"state": row[0],
			"highQ": row[1],
			"highQN": row[2],
			"medQ": row[3],
			"medQN": row[4],
			"lowQ": row[5],
			"lowQN": row[6]
		}
		arr.append(obj)
	return arr

if __name__ == "__main__":
	init()