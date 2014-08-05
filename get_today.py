#/usr/bin/env python

import csv
import json
import time

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
			"high": get_summ(csvreader, 1)
		},
		"data": get_row(csvreader)[1:]
	})
	print json.dumps(data, indent=2)


def getSumm(csv, index):
	print csv
'''
	array = []
	for row in csv:
		try:
			array.append(float(row[index]))
		except ValueError:
			pass
	array.sort()

	print array

	return {
		"min": array[0],
		"max": array[-1],
		"avg": getAvg(array)
	}
'''

def getAvg(arr):
	summation = 0
	for i in arr:
		summation += i
	return summation / len(arr)

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