from datetime import datetime, date

def check_date(str_date:str)->bool:
    try:
        split_date = str_date.split('.')
        day, month, year = map(int, split_date)
        _ = datetime(year, month, day)
        return True
    except ValueError as ex:
        return False

def dz_2(lst_date:list[str])->list[tuple]:
    result:list[bool] = list(map(check_date, lst_date))
    result:list[tuple] = list(zip(lst_date, result))
    return result