#!/usr/bin/python -tt
NoErr = False

while True:
	try:
		upper_lim = raw_input('\n\nInput upper limit, or 0 for standard limit of 100\n\n> ')
		upper_lim = int(upper_lim)
		break
	except:
		print 'Non numeric input'
print type(upper_lim)
if (upper_lim == 0 or upper_lim == 100):
	upper_lim = 101
else:
	upper_lim += 1


output = []
for arg in range(1,upper_lim):
	# print arg,

	if not (arg%3 or arg%5):
		pa = 'Fizz Buzz'
	elif not arg%3:
		pa = 'Fizz'
	elif not arg%5:
		pa = 'Buzz'
	else:
		pa = repr(arg)
	output.append(pa)

print ' '.join(output)
