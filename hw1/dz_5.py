def dz_5()->tuple[bool, float]:
    input_number:str = input("Enter float number: ")
    input_float:float = 0.0
    try:
        input_float = float(input_number)
    except Exception as ex:
        raise Exception(f"Error input float number:{ex.args[0]}")
    
    return (True, input_float) if input_float > 0 else (False, input_float)
        