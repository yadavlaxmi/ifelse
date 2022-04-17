ex_date=int(input('enter a ex date'))
ex_month=int(input('enter a ex month'))
ex_year=int(input('enter a ex year'))
re_date=int(input('enter a re date'))
re_month=int(input('enter a re month'))
re_year=int(input('enter a re year'))
if ex_date>=re_date:
	if ex_month<=re_month:
		if ex_year==re_year:
			print('no charge')
else:
	if ex_date<=re_date:
		if ex_month<=re_month:
			if ex_year<=re_year:
				day=re_date-ex_date
				charge=day*5
				month=re_month-ex_month
				char=month*500
				year=re_year-ex_year
				cha=year*1000
				print('Charge:',charge, 'no of day:',day)
				print('Charge:',char,'no of month:',month)
				print('Charge:',cha,'no of year:',year)