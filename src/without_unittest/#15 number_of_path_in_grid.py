#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import copy

def number_of_path_in_grid(dimension):
	current_grid_dimension = 1
	description_path = [1]
	while current_grid_dimension < dimension:
		i = 0
		new_description_path = []
		while i < len(description_path):
			j = 0
			sum = 0
			while j < i + 1:
				sum += description_path[j]
				j += 1
			new_description_path.append(sum)
			i += 1
		double = new_description_path[-1] * 2
		new_description_path.append(double)
		current_grid_dimension += 1
		description_path = copy.copy(new_description_path)

	# Count path for grid at dimension dimension
	result = 0
	for i in new_description_path:
		result += i
	# Description path is half of the total path
	result *= 2
	
	return result

# TEST
print(number_of_path_in_grid(20))
'''
137846528820
'''
