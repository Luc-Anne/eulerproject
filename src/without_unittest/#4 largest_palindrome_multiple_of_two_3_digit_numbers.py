import math

def check_palindrome_6_digits(number):
	
	i = 6
	digits = []
	while i >= 1:
		digit = math.trunc(number/pow(10, i-1))
		digits.append(digit)
		number = number - digit*pow(10, i-1)
		i -= 1

	if digits[0] == digits[5]:
		if digits[1] == digits[4]:
			if digits[2] == digits[3]:
				return True

	return False

def check_palindrome(number):
	
	digits = [int(i) for i in str(number)]

	number_of_check = math.ceil(len(digits) / 2)
	i = 0
	while i < number_of_check:
		if digits[i] == digits[i * (-1) - 1]:
			i += 1
		else:
			return False

	return True

#TEST
number = 567897
print(check_palindrome_6_digits(number))
number = 202202
print(check_palindrome_6_digits(number))
number = 2024202 # not a 6 digit number
print(check_palindrome_6_digits(number))
number = 567897
print(check_palindrome(number))
number = 202202
print(check_palindrome(number))
number = 2024202
print(check_palindrome(number))
'''
False
True
False
False
True
True
'''

def largest_palindrome_multiple_of_two_3_digit_numbers():
	'''
	Première hypothèse : Il est supérieur à 900000
	
	On a alors :
	- les deux nombres sont supérieur à 900 car 900000 / 999 > 900
	- le chiffre des unités est 9 car c'est un palindrome :
	pour obtenir 9 à l'unité en multipliant deux nombres,
	il y a 3 possibilités pour le chiffre de l'unité, soient :
	1 * 9 | 3 * 3 | 7 * 7
	
	On cherche donc deux nombres justifiant de :
	- former un palindrome par leur multiplication
	- ayant une combinaison de chiffre unitaire particulière
	- tous deux supérieurs à 900
	'''
	
	largest_palindrome_found = 0
	number1 = 0
	number2 = 0
	
	# List of possibilities
	# first method
	'''
	list_number_above_900_last_digit_1 = []
	i = 901
	while i < 1000:
		list_number_above_900_last_digit_1.append(i)
		i += 10
		
	list_number_above_900_last_digit_3 = []
	i = 903
	while i < 1000:
		list_number_above_900_last_digit_3.append(i)
		i += 10

	list_number_above_900_last_digit_7 = []
	i = 907
	while i < 1000:
		list_number_above_900_last_digit_7.append(i)
		i += 10

	list_number_above_900_last_digit_9 = []
	i = 909
	while i < 1000:
		list_number_above_900_last_digit_9.append(i)
		i += 10
	'''
	# second method
	list_number_above_900_last_digit_1 = []
	list_number_above_900_last_digit_3 = []
	list_number_above_900_last_digit_7 = []
	list_number_above_900_last_digit_9 = []
	for i in range(900,1000):
		if   str(i)[-1] == "1": list_number_above_900_last_digit_1.append(i)
		elif str(i)[-1] == "3": list_number_above_900_last_digit_3.append(i)
		elif str(i)[-1] == "7": list_number_above_900_last_digit_7.append(i)
		elif str(i)[-1] == "9": list_number_above_900_last_digit_9.append(i)
	
	# Check for every possibilities
	# ##3 * ##3
	for i in list_number_above_900_last_digit_3:
		for j in list_number_above_900_last_digit_3:
			k = i * j
			if check_palindrome(k) and k > largest_palindrome_found:
				largest_palindrome_found = k
				number1 = i
				number2 = j
	
	# ##7 * ##7
	i = 0
	while i < len(list_number_above_900_last_digit_7):
		x = list_number_above_900_last_digit_7[i]
		j = i
		while j < len(list_number_above_900_last_digit_7):
			y = list_number_above_900_last_digit_7[j]
			if check_palindrome_6_digits(x * y):
				if x * y > largest_palindrome_found:
					largest_palindrome_found = x * y
					number1 = x
					number2 = y
			j = j + 1
		i = i + 1
	
	# ##1 * ##9
	i = 0
	while i < len(list_number_above_900_last_digit_1):
		x = list_number_above_900_last_digit_1[i]
		j = 0
		while j < len(list_number_above_900_last_digit_9):
			y = list_number_above_900_last_digit_9[j]
			if check_palindrome_6_digits(x * y):
				if x * y > largest_palindrome_found:
					largest_palindrome_found = x * y
					number1 = x
					number2 = y
			j = j + 1
		i = i + 1

	if largest_palindrome_found != 0:
		return [largest_palindrome_found, number1, number2]
	else:
		return "Les hypothèses n'étaient pas bonnes."

#TEST
print(largest_palindrome_multiple_of_two_3_digit_numbers())
'''
[906609, 913, 993]
'''
