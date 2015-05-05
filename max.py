a = int(input('enter first value: '))
b = int(input('enter second value: '))

def max(a, b):
	if a > b:
		print('the largest value is ' + str(a))
	elif b > a:
		print('the largest value is ' + str(b))
	else:
		print('nubmers are the same')

max(a, b)

