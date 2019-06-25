def fibo(n):
	
	if (n==0):
		return c
	if (n==1):
		return [0]
	if (n==2):
		return [0,1]
	c=[0,1]
	b=1
	f=0
	for i in range(n-2):
		f=f+b
		c.append(f)
		b=c[i+1]
	return c


