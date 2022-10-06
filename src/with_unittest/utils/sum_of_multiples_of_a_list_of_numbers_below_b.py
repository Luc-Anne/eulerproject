import math
from utils.generic import copy_list

# Given a list of numbers, return the sum of their multiples below b
def sum_of_multiples_of_a_list_of_numbers_below_b(input_list, b):
    # input_list, not empty, with all numbers > 0 and no doublons
    # b >= 2
    check = check_sum_of_multiples_of_a_list_of_numbers_below_b(input_list, b)
    if not check[0]:
        return check
    
    # Make a new list to not modify input list
    list = copy_list(input_list)
    # Delete numbers which are multiple of others
    # to avoid adding several times the same multiple
    # from different numbers of the list
    list.sort()
    i = 0
    while i < len(list):
        j = i + 1
        while j < len(list):
            if list[j] % list[i] == 0:
                list.remove(list[j])
                # remove() automatically move to the next number of the list
            else:
                j += 1
        i += 1
    
    result = 0
    # Add multiples of numbers
    for n in list:
        result += sum_of_multiples_of_n_below_b(n, b)
    # Substract one of multiples of multiples of the list
    # Which has been added two times
    # Example: 15, 30 and 45 if 3 and 5 are in the list
    i = 0
    while i < len(list):
        j = i + 1
        while j < len(list):
            z = list[i] * list[j]
            result -= sum_of_multiples_of_n_below_b(z, b)
            j += 1
        i += 1
    
    return [True, result]

# Given a number n, return the sum of its multiples below b
def sum_of_multiples_of_n_below_b(n, b):
    # n > 0
    # b > 0
    count_multiples = math.trunc(b / n)
    if b % n == 0:
        count_multiples -= 1
    count_multiples_th_triangular_number = \
        (count_multiples / 2) * (count_multiples + 1)
    return count_multiples_th_triangular_number * n

def check_sum_of_multiples_of_a_list_of_numbers_below_b(list, borne):
    checking = sum_of_multiples_of_a_list_of_numbers_below_b.__name__
    if borne < 2:
        return (False, 0, checking, 'Borne < 2')

    if len(list) == 0:
        return (False, 0, checking, 'List is empty')
    
    i = 0
    while i < len(list):
        j = i + 1
        while j < len(list):
            if list[i] == list[j]:
                return (False, 0, checking, 'There are doublons in list')
            else:
                j += 1
        i += 1
    
    for i in range(len(list)):
        if list[i] < 1:
            return (False, 0, checking, 'Numbers in list must be strictly positive')

    return (True, '', '', '')
