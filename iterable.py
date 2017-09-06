from collections import Iterable
print("\"abc\" can iterable?:",isinstance('abc',Iterable))

print('\"[1,2,3]\" can iterable?:',isinstance([1,2,3],Iterable))

print('\"123\" can iterable?:',isinstance(123,Iterable))


for ch in 'ABC':
	print(ch)

for x,y in[(1,1),(2,4),(3,9)]:
	print(x,y)