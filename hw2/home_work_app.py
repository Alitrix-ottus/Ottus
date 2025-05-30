from dz_1 import dz_1
from dz_2 import dz_2, TypePlaceSeatGetting
from dz_3 import dz_3
from dz_4 import dz_4
from dz_5 import dz_5

if __name__ == "__main__":

    int_number:int = dz_1()
    print(f"Result: {int_number}\n")
    
    result = dz_2(TypePlaceSeatGetting.DEFAULT)
    if isinstance(result, int):
        print(f"Row {int(result)} has the right number of empty seats.\n")
        print(f"Result:{result}")
    else:
        print(f"Result is no seat.")

    result = dz_2(TypePlaceSeatGetting.RANDOM)
    if isinstance(result, int):
        print(f"Row {int(result)} has the right number of empty seats.\n")
        print(f"Result:{result}")
    else:
        print(f"Result is no seat.")

    result = dz_3()
    print(f"Result RLE text: {result}")

    result = dz_4()
    print(f"Result Cesar encrypt string: {result}")

    dz_5(manual_input=False)