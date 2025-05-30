def input_number_values(test_input:str)->int:
    input_data:str = input(test_input)
    
    if len(input_data) == 5 and input_data.isnumeric():
        return int(input_data)
    else:
        raise Exception("Error enter numbers")

def dz_1()->int:
    input_numbers:int = input_number_values("Please enter 5 number:")
    
    if input_numbers == -1:
        print('You enter wrong 5 number!')
        raise Exception("Error enter numbers")

    arr_symb:list = list(str(input_numbers))
    change_value:str = arr_symb[1]
    arr_symb[1] = arr_symb[3]
    arr_symb[3] = change_value

    return int(''.join(arr_symb))