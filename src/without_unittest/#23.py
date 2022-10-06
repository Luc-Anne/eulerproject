#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import math, copy

def list_of_abundant_numbers(borne):
	list = []
	n = 1
	while n < borne:
		print(n)
		# Sum of proper divisors
		sum_proper_divisors = 0
		i = copy.copy(n) / 2
		# Check others
		while i > 0:
			if n % i == 0:
				sum_proper_divisors += i
				# Add n to the list if n is an abundant number
				if sum_proper_divisors > n:
					list.append(n)
					break
			i -= 1
		n += 1

	return list

def list_not_double_an():
	borne = 28123
	list_an = list_of_abundant_numbers(borne)
	list_potential_double_an = set(int for int in range(1, borne + 1))

	# Remove double an in the list of potential double an
	i = 0
	while i < len(list_an):
		print(list_an[i])
		j = copy.copy(i)
		while j < len(list_an):
			k = list_an[i] + list_an[j]
			if k > (borne + 1):
				break
			list_potential_double_an.discard(k)
			j += 1
		i += 1
	
	print(list_potential_double_an)
	return list_potential_double_an

# TEST
print(sum(list_not_double_an()))
'''
4179871
'''
