unit= int(input('enter any unit'))
if unit < 100:
	print('no charge')
elif unit < 200:
	print('5 per unit')
elif unit >200:
	print('10 per unit')
else:
	print('nothing')