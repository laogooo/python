names = ['Michael','Bob','Tracy']
for name in names:
	print(name)

L=list(range(5))
print(L)

sum=0
for x in range(101):
	sum= sum+x
print(sum)


sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)


# -*- coding: utf-8 -*-
L = ['Bart', 'Lisa', 'Adam']
for n in L:
	print('hello,%s'%n)


n=1
while n<=100:
	if n>10:   # 当n = 11时，条件满足，执行break语句
		break  # break语句会结束当前循环
	print(n)
	n=n+1
	pass

n=0
while n<10:
	n=n+1
	if n%2==0:    # 如果n是偶数，执行continue语句
		continue  # continue语句会直接继续下一轮循环，后续的print()语句不会执行
	print(n)

n =1
while n>0:
	n=n+1
	print(n)
	pass