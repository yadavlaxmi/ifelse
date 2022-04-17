user=int(input('enter'))
if user>=18:
	print('eligible for voting')
if user>=18 and user<=20:
	print('eligible for study')
if user>=20 and user<=30:
	print('eligible for married')
else:
		print('nothing')