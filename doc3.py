months=input('enter any months')
if months in 'April,june,september,november':
	print('30 days')
elif months in 'January,March,May,july,August,October,December':
	print('31days')
elif months== 'February':
	print('28 or 29 days')
else:
	print('nothing')