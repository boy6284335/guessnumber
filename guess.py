import random
r = random.randint(1, 100)
while True:
	num = int(input('請猜數字: '))
	if num == r:
		print('終於猜對了!')
		break
	elif num > r: 
		print('再猜小一點')
	elif num < r:
		print('再猜大一點')
	elif num > 100 :
		print('請輸入比1到100')
