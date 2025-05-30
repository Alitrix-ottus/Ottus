def input_number_values(test_input:str)->int:
    input_data:str = input(test_input)
    if len(input_data) > 0:
        return int(input_data)
    else:
        raise Exception("Error enter number days")

def dz_2()->int:
    input_number:int = input_number_values('Enter the number of days until your next vacation: ')
    if input_number == -1:
        raise Exception('You enter wrong count number!')
    
    is_d = (input_number // 7)
    prop_n = input_number % 7
    
    if prop_n == 6:
        total_day_off:int = is_d * 2 + 1
    else:
        total_day_off:int = is_d * 2
    
    return total_day_off