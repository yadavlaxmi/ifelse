A=input('enter any number')
B=input('enter any number')
C=input('enter any number')
D=input('enter any number')
if A>B and C>D:
	print('A is greater than B,C and D')
elif C>D>B>A:
	print('C is greater than D,A and E')
elif D>B>C>A:
	print('D is greater than A,B and C')
elif B>C>A>D:
	print('B is greater A,C and D')
else:
	print('Nothing')