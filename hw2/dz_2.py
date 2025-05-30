import random
from enum import Enum

class TypePlaceSeatGetting(Enum):
    DEFAULT = 0
    RANDOM = 1

def get_rnd(total_number:int)->any:
    count_number:int = 0
    while True:
        if count_number == total_number:
            break

        rnd = random.choice([0, 1])
        yield rnd
        count_number += 1

def sample_seat_list()->list[list]:
    lst_seat:list[list] = [[0,1,1,0], [1,0,0,0], [0,1,0,0],[0,1,1,0], [1,0,1,0], [1,1,0,1]]

    return lst_seat
    
def random_seat_list(count_row:int, count_seat:int)->list[list]:
    list_of_lists = [[i for i in get_rnd(count_seat)] for _ in range(0, count_row) for _ in range(1)]
    
    return list_of_lists[0]

def user_input_seat_param()->tuple[int, int]:
    row_str:str = input('Please input count of row seats:')
    try:
        count_row:int = int(row_str)
        if count_row <= 0:
            raise Exception(f"Error input count row, count cannot be less than 0.")
        
    except Exception as ex:
        raise Exception(f"Error input count row: {ex}")
    
    seats_str:str = input('Please input count of seats in row:')
    try:
        count_seats:int = int(seats_str)
        if count_seats <= 0:
            raise Exception(f"Error input count seats, count cannot be less than 0.")
        
    except Exception as ex:
        raise Exception(f"Error input count seats: {ex}")

    return (count_row, count_seats)

def user_request_seats()->int:
    seats_str:str = input('Please input how mane seats are you need:')
    try:
        count_seats:int = int(seats_str)
        if count_seats <= 0:
            raise Exception(f"Error input count seats, count cannot be less than 0.")
        
        return count_seats
    except Exception as ex:
        raise Exception(f"Error input count seats: {ex}")

def print_view_seats(lst_seats:list[list]):
    for number_row, row in enumerate(lst_seats, 1):
        print(f"Number row:{number_row}\t{row}")

def search_free_seats(request_seats:int, lst_seat:list[list])-> int | bool:
    for i, row in enumerate(lst_seat):
        free_seats:int = 0
        for seat in row:
            if seat == 0:
                free_seats += 1
            else:
                free_seats = 0

            if free_seats == request_seats:
                return i + 1
    return False

def dz_2(type_input_seat:TypePlaceSeatGetting)-> int | bool:
    match type_input_seat:
        case TypePlaceSeatGetting.DEFAULT:
            lst_seat:list[list] = sample_seat_list()
            print_view_seats(lst_seat)
            
        case TypePlaceSeatGetting.RANDOM:
            (count_row, count_sets) = user_input_seat_param()
            lst_seat:list[list] = random_seat_list(count_row=count_row, count_seat=count_sets)
            print_view_seats(lst_seat)
    
    request_seats:int = user_request_seats()
    result_row = search_free_seats(request_seats, lst_seat)

    return result_row