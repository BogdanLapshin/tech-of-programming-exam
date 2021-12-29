def P(n):
	if n < 0:
		return None
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return P(n - 1) + (1 + (1 + 8*P(n - 1)) ** .5) // 2