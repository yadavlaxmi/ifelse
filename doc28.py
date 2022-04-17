year= int (input('enter any year'))
if year% 4==0:
	print('leap year')
else:
	if year%400==0:
		print('it is leap year')
	else:
		print('not leap year')