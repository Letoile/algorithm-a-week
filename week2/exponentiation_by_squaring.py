def fast_exp(number, exp):
	if exp == 0:
		return 1
	if exp == 1:
		return number
	if (number % 2 == 1):
		return fast_exp(number, exp-1) * number
	else:
		temp = fast_exp(number, exp/2)
		return temp * temp			