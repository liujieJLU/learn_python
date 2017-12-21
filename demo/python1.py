# -*- coding:utf-8 -*-

def is_odd(n):
	return n %2 ==1


def creatGenerator():
	mylist = range(3)	
	for i in mylist:
		yield i * i

# 构造基数序列
def odd_iter():
	n = 1
	while True:
		n = n + 2
		yield n

def not_divisible(n):
	return lambda x: x % n >0

def prime():
	yield 2
	it = odd_iter()
	while True:
		n = next(it)
		yield n 
		it = filter(not_divisible(n), it)

# print(prime())

for n in prime():
	print("----------:"+ str(n))
	if n < 1000:
		print(n)
	else :
		break



a = list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

# print(a)

mygenerator = creatGenerator()
# print (mygenerator)

# for i in mygenerator:
# 	print(i)


# fs = [(lambda n: i + n) for i in range(10)]
# print (fs[3](4))
