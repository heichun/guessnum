import random

r = random.randint(1,100)
count = 0
while True:
	count += 1 #count = count + 1
	num = input('no?')
	num = int(num)
	if num == r:
		print('you right!')
		print('你估左', count, '次')
		break
	elif num > r:
		print('細D')
	elif num < r:
		print('大D')
	print('你估左', count, '次')
