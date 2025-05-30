def id_to_str(number:int)->str:
    number_str:str = str(number)
    return '0' * (8 - len(number_str)) + number_str

def check_and_replace(name:str)->str:
    if not name.isalpha():
        raise Exception("Error name and surname can be only letter!")
    
    if not name[0].isupper():
        name = name.replace(name[0], name[0].upper(), 1)
    return name

def input_user_data()->dict:
    loop:bool = True
    lst_user_data:dict = {}

    while loop:
        user_name:str = input('Input Name:')
        user_surname:str = input('Input Surname:')
        user_age:str = input('Input age:')
        user_id:str = input('Input ID:')

        if not user_name or not user_surname or not user_age or not user_id:
            loop = False
            continue
        
        user_age = int(user_age)
        user_id = int(user_id)

        if user_id in lst_user_data:
            print(f"input only unique id! Repeat input:")
            continue
        
        if user_age < 18 and user_age > 61:
            print('Error, age must be between 18 and 60! Repeat input:')
            continue
        
        user_name = check_and_replace(user_name)
        user_surname = check_and_replace(user_surname)
        
        lst_user_data[user_id] = ( 
                    user_name,
                    user_surname,
                    user_age
                    )
    
    return lst_user_data

def print_data(lst_user_data:dict):
    for item in lst_user_data.items():
        user_name, user_surname, user_age = item[1]
        text_view:str = f"ID:{id_to_str(item[0])}, Name:{user_name}, Surname:{user_surname}, Age:{user_age}"
        print(text_view)
    
def dz_4():
    lst_user_data:dict = input_user_data()
    print_data(lst_user_data)