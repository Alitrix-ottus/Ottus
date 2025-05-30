def is_character_string(sequence_text:str)->bool:
    check = [item for item in list(sequence_text) if item.isdigit()]

    return True if len(check) == 0 else False

def to_rle(sequence_text:str)->str:
    src_text:list[str] = list(sequence_text)
    cumul_symbol_count:dict = {i:src_text.count(i) for i in src_text}
    text_rle:str = ''
    for item in cumul_symbol_count.items():
        text_rle += f"{item[1]}{item[0]}"

    return text_rle

def dz_3()->str:
    user_sequence_input:str = input("Please input sequence:")
    if not is_character_string(user_sequence_input):
        raise Exception(f"Error input sequence ! Needded only symbolic string.")
    
    rle_text:str = to_rle(user_sequence_input)

    return rle_text
