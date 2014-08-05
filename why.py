#/usr/bin/env python

l1 = [1, 3, 5, 7, 9, 11]
l2 = [2, 4, 6, 8, 10, 12]

def get_min(l):
	l.sort()
	return l[0]

print get_min(l1)

print get_min(l2)