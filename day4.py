print("Gcd of two numbers:")
def my_gcd(a,b):
	while a > 0 and b > 0:
		if a > b:
			a = a % b
		else:
			b = b % a
	if a == 0:
		return b
	else:
		return a
