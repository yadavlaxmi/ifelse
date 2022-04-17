Number= int(input('enter any number'))
if Number%5==1:
	print('remainder1')
elif Number%5==0:
	print('remainder0')
elif Number=='00':
	print('error')
else:
	print('special character')