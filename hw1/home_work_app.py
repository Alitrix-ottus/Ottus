from dz_1 import dz_1
from dz_2 import dz_2
from dz_3 import dz_3
from dz_4 import dz_4
from dz_5 import dz_5

if __name__ == "__main__":

    reverse_int:int = dz_1()
    print(f"Reverse 3 number at center input number: {reverse_int}\n")

    total_count_hilidays:int = dz_2()
    print(f"Total number of days before vacation: {total_count_hilidays}\n")

    piece_chocolade:bool = dz_3()
    print(f"You can break off a piece:{piece_chocolade}\n") if piece_chocolade else print(f"You can't break off a piece:{piece_chocolade}\n")

    rome_number:str = dz_4()
    print(f"Roman equivalent: {rome_number}\n") if rome_number != "" else print(f"Error number !\n")

    pos_neg, float_number = dz_5()
    print(f"Input positive float number: {float_number}\n") if pos_neg else print(f"Input negative float number: {float_number}\n")