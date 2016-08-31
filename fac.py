#fac.py writen by Jesse Gallarzo

N = int(input())
ans = 1
for num in range(1,N+1):
	print "ans " + str(ans)
	ans *= num
	print "num " +  str(num)
	print "answer after operation" +  str(ans)
print ans
