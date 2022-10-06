import copy

def prime_factor(num):
	num_tested = copy.copy(num)
	list_divisor = []
	divisor_tested = 2
	while True:
		if num_tested % divisor_tested == 0:
			list_divisor.append(divisor_tested)
			# Check if all prime divisors has been found
			product_of_divisors_found = 1
			for i in list_divisor:
				product_of_divisors_found *= i
			if num == product_of_divisors_found:
				return list_divisor
			else:
				num_tested /= divisor_tested
				divisor_tested = 1
		divisor_tested += 1

#TEST
num = 600851475143
print(prime_factor(num)[-1])
"""
6857
"""
