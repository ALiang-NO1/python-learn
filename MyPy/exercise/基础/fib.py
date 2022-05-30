def fib(m):
	a, b = 0, 1
	n = 1
	s = [1]
	while n < m:
		a, b = b, a+b
		n += 1
		s.append(b)
	print(s)
fib(3)