from .type import type_error_message

debug_mode = False

def display_error(msg, error):
    message = '{} | {}'.format(msg, error[3])
    if debug_mode:
        message = message + '\n{} in {}'.format(type_error_message(error[1]), error[2])
    return message
