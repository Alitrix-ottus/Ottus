def user_input_number()->int:
    input_value:str = input('Please enter int number:')

    try:
        input_int:int = int(input_value)
    except Exception as ex:
        raise Exception(f"Wrong input number: {ex}")
    finally:
        return input_int

def split_number(int_value:int)->list[int]:
    try:
        lst_int:list[int] = [int(i) for i in str(int_value)]
    except Exception as ex:
        raise Exception(f"Error splitting integer number: {ex}")
    finally:
        return lst_int

def calculate_int(lst_int:list[int])->int:
    total_sum:int = 0

    for item in lst_int: # sum(lst_int)
        total_sum += item
    
    if total_sum > 9:
        split_int:list[int ] = split_number(total_sum)
        return calculate_int(split_int)
    else:
        return total_sum

def dz_1()->int:
    input_number:int = user_input_number()
    split_int:list[int ] = split_number(input_number)
    final_number:int = calculate_int(split_int)

    return final_number