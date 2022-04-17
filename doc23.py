days= int(input('enter any number'))
if days<5:
	charges=days*2
	print ('charges')
else:
	if days>10 and days<10:
		charges=days*3
		print('charges')
	else:
		 		if days<15 and days>10:
		 			charges=days*4
		 			print('charges')
		 		else:
		 		  		if days>15:
		 		  		   charges=days*5
		 		  		   print('charges')
		 		  		else:
		 		  			print('nothing')