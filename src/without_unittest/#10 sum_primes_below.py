#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import math

def prime_below(number):
	list_primes = [2]
	for i in range(3, number+1):
		# Display some informations for long calculs
		if i % 1000 == 0:
			print("Current number checked : " + str(i))

		racine_carre = math.trunc(math.sqrt(i))
		is_prime = True
		for prime in list_primes:
			if prime <= racine_carre and i % prime == 0:
				is_prime = False
				break
		if not(is_prime):
			continue
		list_primes.append(i)
	return list_primes

def sum_primes_below(number):
	result = sum(i for i in prime_below(number))
	return result

# TEST
print(sum_primes_below(2000000))
'''
print(sum_primes_below(2000000))
142913828922
'''
