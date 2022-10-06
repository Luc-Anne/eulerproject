#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import math

def triangle_number():
	i = 0
	t = 0
	while True:
		i += 1
		t += i
		yield t

gen = triangle_number()

def number_of_divisors(number):
	result = 0
	sqrt = math.sqrt(number)
	sqrt_trunc = math.trunc(sqrt)
	# case : number is a square
	if sqrt == sqrt_trunc:
		result += 1
	# Test all number below square root
	for i in range(1, sqrt_trunc):
		if number % i == 0:
			result += 2

	return result

def first_triangle_number_over_five_hundred_divisors(borne):
	number_divisors = 0
	while number_divisors < borne:
		triangle_number = next(gen)
		number_divisors = number_of_divisors(triangle_number)
	return triangle_number


# TEST
print(first_triangle_number_over_five_hundred_divisors(500))
'''
76576500
'''
