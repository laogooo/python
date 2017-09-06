# -*-conding uft-8-*-
def my_abs(x):
	if x>=0:
		return x
	else:
		return -x
	pass


L = []
for x in range(1,11):
	L.append(x*x)
print(L)

y=[y*y for y in range(1,11)]
print(y)


print([z*z for z in range(1,11) if z%2==0])


print([m+n for m in 'ABC' for n in 'XYZ'])


L=['Hello','World',18,'Apple',None]
L2=[s.lower() for s in L if isinstance(s,str)]
print(L2)