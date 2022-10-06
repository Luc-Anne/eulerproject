import sys
import math

################################################################################
def sum_of_even_fibonacci_borne(borne):
	#Create fibonacci serie towards the borne
	fibo = [1,1]
	i = 2
	while fibo[i-1] < borne:
		fibo.append(fibo[i-1] + fibo[i-2])
		i += 1
	fibo.pop()
	
	#Sum of even numbers
	result = 0
	i = 2
	while i < len(fibo):
		result += fibo[i]
		i += 3
	
	return result

################################################################################
def fibonacci_serie_generator():
	previous_previous = 0
	previous = 1
	while True:
		current = previous_previous + previous
		previous_previous = previous
		previous = current
		
		yield current

gen = fibonacci_serie_generator()

def sum_of_even_fibonacci_borne2(borne):
	result = 0
	for last in gen:
		if last < borne:
			if last % 2 == 0:
				result += last
		else:
			return result

################################################################################
def fibonacci_serie_even_generator():
	previous_previous = 0
	previous = 1
	while True:
		current = previous_previous + previous
		previous_previous = previous
		previous = current
		
		if current % 2 == 0:
			yield current

gen2 = fibonacci_serie_even_generator()

def sum_of_even_fibonacci_borne3(borne):
	result = 0
	for i in gen2:
		if i < borne:
			result += i
		else:
			break
	return result

def main():
    borne = 4000000
    print(sum_of_even_fibonacci_borne3(borne))
    '''
    4613732
    '''

if __name__ == '__main__':
    main()
