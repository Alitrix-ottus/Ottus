from dz_1 import dz_1
from dz_2 import dz_2
from dz_3 import dz_3
from dz_4 import dz_4


if __name__ == "__main__":

    #------- DZ 1 ----------------------------------------------

    fn_names:list[str] = [
                        "otus_course", 
                        "PythonIsTheBest",
                    ]
    renames:list[tuple] = dz_1(fn_names)    
    print(f"DZ 1 - Result: {renames}\n{'-'*100}")

    #------- DZ 2 ----------------------------------------------
    
    examples_date:list[str] = [
                                "29.02.2000",
                                "29.02.2001",
                                "31.04.1962"
                            ]
    result:list[tuple] = dz_2(examples_date)
    print(f"DZ 2 - Result: {result}\n{'-'*100}")

    #------- DZ 3 ----------------------------------------------

    max_number:int = 50
    src_list_int:list[int] = [item for item in range(3, max_number)]
    result:list[tuple] = dz_3(src_list_int)
    print(f"DZ 3 - Result: {result}\n{'-'*100}")

    #------- DZ 4 ----------------------------------------------

    dz_4()