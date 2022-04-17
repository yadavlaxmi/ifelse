quantity=int(input('enter any quantity'))
cost=input('quantity*100')
if quantity>1000:
	discount=('10/100* cost')
	total=(cost)
	print('total:',total)
else:
	print('nothing')