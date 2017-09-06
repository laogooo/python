# -*- coding: utf-8 -*-
age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')


birth = int(input('birth: '))
if birth < 2000:
    print('00前')
else:
    print('00后')

h=float(input('输入身高(单位米):'))
w=float(input('输入体重(单位千克):'))
b=w/(h*h)
print('你的BMI指数是:%.1f'%b)
if b > 32:
	print('严重肥胖')
elif b >= 28:
 	print('肥胖')
elif b >=25:
 	print('过重')
elif b >= 18.5:
    print('您的体形:正常')
else:
    print('您的体形:过轻')