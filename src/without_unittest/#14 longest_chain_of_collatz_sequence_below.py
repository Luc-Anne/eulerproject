#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import copy

def generator_lenght_collatz_sequence_with_length():
	n = 0
	while True:
		n += 1
		length = 1
		i = copy.copy(n)
		while i != 1:
			length += 1
			if i % 2 == 0:
				i = i / 2
			else:
				i = 3 * i + 1
		yield [n, length]
			
gen = generator_lenght_collatz_sequence_with_length()

def longest_chain_of_collatz_sequence_below(borne):
	data_result = []
	length = 0
	for i in range(borne):
		# Display for long calcul
		if i % 1000 == 0:
			print("Current number checked :" + str(i))
		data = next(gen)
		if data[1] > length:
			length = data[1]
			data_result = data
	return data_result

# TEST
print(longest_chain_of_collatz_sequence_below(1000000))
'''
[837799, 525]
'''
