#!/usr/bin/python3
i = 0
while i <= 99:
	if i != 99:
		print('{0:02d}'.format(i), end=', ')
	else:
		print(i)
	i += 1
