
def to_CamelCase(src_name:str)->str:
    return "".join([word.replace(word[0], word[0].upper(), 1) for word in src_name.split('_')])

def to_snake_case(src_name:str)->str:
  return "_".join("".join([(" " + symb.lower() if symb.isupper() else symb) for symb in src_name]).strip().split())

def change_name(name:str)->str:
  return to_CamelCase(name) if name[0].islower() else to_snake_case(name)   

def dz_1(names:list[str])->list[tuple]:
    result:list[str] = list(map(change_name, names))
    result:list[tuple] = list(zip(names, result))
    return result