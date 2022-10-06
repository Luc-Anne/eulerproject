import sys
import math

from utils import sum_of_multiples_of_a_list_of_numbers_below_b
from utils import check_sum_of_multiples_of_a_list_of_numbers_below_b
from error import display_error

def view_result_sum_of_multiples_below_borne(list, borne):
    result = sum_of_multiples_of_a_list_of_numbers_below_b(list, borne)
    if result[0]:
        message_result = str(int(result[1]))
        message_list = ', '.join(map(str, list))
        message = 'The sum of multiples of {} below {} is : {}'\
            .format(message_list, str(borne),message_result)
    else:
        message = display_error('Some inputs were invalids', result)
    return message

def view_input_sum_of_multiples_below_borne():
    print("Quelle est la somme des multiples d'une liste de nombre inférieurs à une borne supérieure ?")
    valid_input = False
    while not valid_input:
        input_liste = input('List of numbers separated by comma : ')
        liste = list(map(int,input_liste.split(',')))
        input_borne = input('Borne : ')
        borne = int(input_borne)
        
        check = check_sum_of_multiples_of_a_list_of_numbers_below_b(liste, borne)
        if check[0]:
            valid_input = True
            print(view_result_sum_of_multiples_below_borne(liste, borne))
        else:
            print(display_error('Some inputs are invalids', check))
    '''
    266341
    '''

# CLI
if __name__ == '__main__':
    sys.exit(view_input_sum_of_multiples_below_borne())
