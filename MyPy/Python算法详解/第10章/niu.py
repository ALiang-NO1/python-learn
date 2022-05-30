from math import sqrt

def sqrt_newton(num):
	x=sqrt(num)
	y=num/2.0
	count=1
	while abs(y-x)>0.00000001:
		print(count,y)
		count+=1
		y=((y*1.0)+(1.0*num)/y)/2.0000
	return y

print(sqrt_newton(5))
print(sqrt(5))