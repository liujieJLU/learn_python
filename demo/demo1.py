# -*- coding:utf-8-*-

# 过滤出回数过滤器1
def filterR1(i):
	s = str(i)
	return s == ''.join(reversed(s))

# 过滤出回数过滤器2
def fileterR2(i):
	s = str(i)
	return s[:] == s[::-1]


print(filter(filterR1, range(2000)))