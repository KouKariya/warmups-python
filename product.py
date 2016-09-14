#product.py
#Written by Jesse Gallarzo
#Written in Python3
ans = 1
arr=[]
N = int(input())
#TODO fix 'int not iterable' issue
for num in N:
	arr.append(int(input()))

for val in N:
	ans = (ans*arr[val])%(10**9 + 7)
	
print (ans)
