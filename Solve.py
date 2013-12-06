test = u'3 + 1'
output = []
stack = []
final = ''
for x in test:
	if(x.isnumeric()):
		output.append(x)
	else:
		stack.push(x)
	print 

