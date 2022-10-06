import math
from expected_results import test_function

test_mode = True

def test_functions():
	print('################################################################################')
	'''
	function = ''
	test_function(function,  , )
	'''
	
	if test_mode:
		function = 'sum_of_multiples_below_borne'
		test_function(function, 23.0 , list=[3, 5], borne=10)
		test_function(function, 78.0 , list=[3, 5, 15], borne=20)
		
		function = 'sum_of_a_multiple_below_borne'
		test_function(function, 18.0 , n=3, borne=10)

		function = 'view_result_sum_of_multiples_below_borne'
		test_function(function , "The sum of multiples of 3, 5 below 10 is :\n23", list=[3, 5], borne=10)
		test_function(function , "Some inputs are invalids", list=[], borne=10)
		test_function(function , "Some inputs are invalids", list=[3, 5], borne=1)
		test_function(function , "Some inputs are invalids", list=[-1, 5], borne=10)

def sum_of_multiples_below_borne(list, borne):
	borne -= 1
	
	result = 0
	
	# Delete numbers which is multiple of others
	i = 0
	while i < len(list):
		x = list[i]
		j = i + 1
		while j < len(list):
			y = list[j]
			if y % x == 0:
				list.remove(y)
			j += 1
		i += 1
	
	# Add multiples of numbers
	for multiple in list:
		result += sum_of_a_multiple_below_borne(multiple, borne)

	# Substract one of multiples of multiples of the list
	# Which has been added two times
	i = 0
	while i < len(list):
		x = list[i]
		j = i + 1
		while j < len(list):
			y = list[j]
			z = x * y
			result -= sum_of_a_multiple_below_borne(z, borne)
			j += 1
		i += 1
		
	return result

def sum_of_a_multiple_below_borne(n, borne):
	number_of_n_below_borne = math.trunc(borne / n)
	number_of_brick_n_below_borne = \
		(number_of_n_below_borne / 2) * (number_of_n_below_borne + 1)
	return number_of_brick_n_below_borne * n

def check_input_of_sum_of_multiples_below_borne(list, borne):
	
	if len(list) == 0:
		print("Input error : List is empty")
		return False
	if borne < 2:
		print("Input error : Borne < 2")
		return False
	
	list.sort()
	
	if list[0] < 1:
		print("Input error : Multiples must be positive numbers")
		return False

	return True

def view_result_sum_of_multiples_below_borne(list, borne):
	result = ""
	if check_input_of_sum_of_multiples_below_borne(list, borne):
		view_list = ", ".join(map(str, list))
		result += "The sum of multiples of " + view_list + \
			  " below " + str(borne) + " is :\n"
		result += str(int(sum_of_multiples_below_borne(list, borne)))
		return result
	else:
		return "Some inputs are invalids"

def main():
	list = [3, 5, 7, 15, 45]
	borne = 1000
	print(view_result_sum_of_multiples_below_borne(list, borne))
	'''
	266341
	'''

main()

test_functions()
