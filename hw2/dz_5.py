def default_test_data()->list[dict]:
    default_list_data:list[dict] = []
    default_list_data.append({'subject': 'Математика', 'surname': 'Иванов', 'rating': 5})
    default_list_data.append({'subject': 'Математика', 'surname': 'Петров', 'rating': 3})
    default_list_data.append({'subject': 'Литература', 'surname': 'Иванов', 'rating': 4})
    default_list_data.append({'subject': 'Математика', 'surname': 'Сидоров', 'rating': 5})
    default_list_data.append({'subject': 'Литература', 'surname': 'Петров', 'rating': 4})
    default_list_data.append({'subject': 'Математика', 'surname': 'Иванов', 'rating': 5})
    default_list_data.append({'subject': 'Литература', 'surname': 'Сидоров', 'rating': 2})
    default_list_data.append({'subject': 'Литература', 'surname': 'Сидоров', 'rating': 5})
    default_list_data.append({'subject': 'Математика', 'surname': 'Иванов', 'rating': 3})

    return default_list_data

def get_data_from_input_string(input_text:str)->dict:
    try:
        split_data:list[str] = input_text.split(' ')
        if len(split_data) > 3 or len(split_data) < 3:
            raise Exception(f"Error input count data, needed (subject name, surname, rating)")
        
        return {'subject': split_data[0], 'surname': split_data[1], 'rating': split_data[2]}
    except Exception as ex:
        raise Exception(f"Error input data: {ex}")

def user_input_data()->list[dict]:
    _exit_input:bool = False
    lst_data:list[dict] = []
    while not _exit_input:
        user_input_data:str = input("please enter 'subject surname rating':")
        if len(user_input_data) == 0:
            break
        record:dict = get_data_from_input_string(user_input_data)
        lst_data.append(record)
    
    return lst_data

def print_user_data(lst_data:list[dict]):
    for item in lst_data:
        print(f"{item['subject']} {item['surname']} {item['rating']}")

def filter(lst_data:list[dict], field:str, filter_value:str)->list[dict]:
    filter_data:list = [item for item in lst_data if item[field] == filter_value]

    return filter_data

def print_group_user_data(lst_data:list[dict], field:str):
    unique_lst:list = list({v[field]:v for v in lst_data}.values())
    group_result:dict = {}
    for unique_item in unique_lst:
        group_field_value = unique_item [field]
        lst_stud_rating:list[dict] = []
        for filter_item in filter(lst_data, field, group_field_value):
            fnd_elem:list = [item for item in lst_stud_rating if item['surname'] == filter_item['surname']]
            if fnd_elem:
                fnd_elem = fnd_elem[0]
                fnd_elem['rating'] += f" {str(filter_item['rating'])}"
            else:
                lst_stud_rating.append({'surname': filter_item['surname'], 'rating': f"{str(filter_item['rating'])}"})
        
        group_result[group_field_value] = lst_stud_rating

    for group_item in group_result.items():
        print(f"{group_item[0]}")
        for elem_item in group_item[1]:
            print(f"{elem_item['surname']} {elem_item['rating']}")
        print('\n')

def dz_5(manual_input:bool=False):
    if manual_input:
        lst_data:list = user_input_data()
    else:
        lst_data:list = default_test_data()

    print('='*100)
    print_user_data(lst_data)
    print('='*100)
    print_group_user_data(lst_data, 'subject')
    print('='*100)