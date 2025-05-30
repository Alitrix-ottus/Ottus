from typing import OrderedDict

def to_rome_number(numbers:int)->str:
    rome_numbers = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I'),
        ]
    
    result:str = ''
    for (n, roman) in rome_numbers:
        (d, numbers) = divmod(numbers, n)
        result += roman * d

    return result

def dz_4()->str:
    input_number:str = input("Enter a positive integer 1 - 4000: ")
    try:
        input_int:int = int(input_number)
    except Exception as ex:
        raise Exception(f"Error input number: {ex.args[0]}")
    

    if input_int <= 0 or input_int > 4000:
        raise Exception(f"The entered number is less than 1 or more 4000")
    
    rome_number:str = to_rome_number(input_int)
    return rome_number