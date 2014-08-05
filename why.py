#/usr/bin/env python



l = [
	['0','32'],
	['1','11'],
	['2','78'],
	['3','111'],
	['4','783']
]

def get_min(l, i):
	data =[]
	for row in l:
		data.append(row[i])
	return {
		"min": data[0],
		"max": data[-1]
	}

print get_min(l, 0)

print get_min(l, 1)