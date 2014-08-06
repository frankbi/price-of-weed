#/usr/bin/python


# THE MISSION
#
# 1. The first 200+ days, the numbers were
# scraped with dollars signs
#
# 2. The filename convention is horrendous. It's currently
# day/month/year, which doesn't sort well
#
# 3. CSVs should be sorted into a folder, by year and month.

###########################
# python scripts/clean.py #
###########################


import csv
import os


def init():
	# rename_files()
	to_float()

def rename_files():
	files = os.listdir("try/")
	for filename in files:
		if filename.startswith("weedprices"):
			full_str = filename[10:]
			day = full_str[:2]
			month = full_str[2:4]
			year = full_str[4:]
			seq = (month, day, year)
			final_str = "-".join(seq)
			os.rename("try/" + filename, "try/prices" + final_str + ".csv")
			return True
		else:
			return False

def to_float():
	files = os.listdir("try/")
	for filename in files:
		if filename.startswith("weedprices"):
			csvfile = open("try/" + filename, "r")
			reader = csv.reader(csvfile, delimiter=",")
			csvfile_copy = []
			for row in reader:
				data_list = []
				for index in row:
					data_list.append(index)
				csvfile_copy.append(data_list)
			# print csvfile_copy
			# write_row(csvfile_copy)
			print csvfile_copy[0]

def write_row(data):
	csvfile = open("wtf_dang.csv", "wb")
	writer = csv.writer(csvfile, delimiter=",")
	writer.writerow(data)


if __name__ == "__main__":
	init()