_ALPHABET_ = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def get_alph_symb(index:int, alph:str)->str:
    if index <= len(alph) - 1:
        return alph[index]
    
    raise Exception(f"Error index out of bound list!")

def rle_encrypt(user_text:str, enc_key:int, alph:str):
    user_text = user_text.replace(' ','')

    translated = ''
    for character in user_text:
        if character in alph:
            search_num_alph:int = alph.find(character)
            search_num_alph = search_num_alph + enc_key
            
            if search_num_alph > len(alph) - 1:
                need_shift:int = search_num_alph - len(alph)
                translated += get_alph_symb(need_shift, alph)

            elif search_num_alph < 0:
                search_num_alph = search_num_alph + len(alph)

            else:
                translated += get_alph_symb(search_num_alph, alph)
                
        else:
            translated += character

    return translated

def dz_4():
    user_input_text:str = input('Please enter text for Cesar encrypt:')
    
    user_input_key_str:str = input('Please enter key:')
    if not user_input_key_str.isdigit():
        raise Exception(f"Error input is not digit !")
    
    user_input_key:int = int(user_input_key_str)
    if user_input_key > len(_ALPHABET_):
        raise Exception(f"Error, the key cannot be greater than the alphabet length !")
    
    enc_user_text:str = rle_encrypt(user_input_text, user_input_key, _ALPHABET_)

    return enc_user_text