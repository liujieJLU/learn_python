# -*-coding:utf-8 -*-
from math import sqrt
# d = {}
# d['name'] = 'Gumby'
# d['age'] ='42'
# d.clear()
# print(d)



# x = {'username': 'admin', 'machine':['foo', 'bar', 'baz'], 'password':['food', 'ba', 'z']
# y = x.copy()
# y['username'] = 'liujie'
# y['machine'] = 'car'
# y['password'].remove('food')
# print(x)
# print(y)
# print(x.items())


# x = [1, 2, 3]
# y = [2, 4]

# print(x is not y)
# del x[2]
# y[1] = 1
# y.reverse()
# y = 1
# assert y > 1

# d = {'x' : 1, 'y' : 2, 'z' : 3}
# for key, value in d.items():
# 	print(key + "======:" + str(value))
# print(y)


# exec("print('hello, world')")
scope = {}
exec('qrt = 1')
print(scope['qrt'])
print(sqrt(4))