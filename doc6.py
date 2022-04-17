unit =int(input('enter'))
if unit<=100:
	print('no charge')
else:
	if unit>=100 and unit<=200:
		bill=unit*5
		print('bill per unit:',bill)
	else:
		if unit>=200 and unit<350:
		    bill=unit*10
		    print('bill per unit:',bill)
		else:
		    if unit==350:
		    	bill=2000
		    	print('total bill:',bill)
		    else:
		    	print('nothing')