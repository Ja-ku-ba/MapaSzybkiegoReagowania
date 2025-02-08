from .constants import *

def get_type_by_int(type):
    if type == 1:
        return C_ALL
    elif type == 2:
        return C_NATURAL
    elif type == 3:
        return C_LAW
    elif type == 4:
        return C_UTILITIES
    return C_ALL

def get_type_by_shorname(type):
    try:
        type = type.upper()
    except:
        # someone call via api with incoret type leter size
        pass
    if type == C_ALL:
        return C_ALL_EVENTS
    return [type] if type in C_ALL_EVENTS else None