def dz_3()->bool:
    width_chocolade:int = 0 
    height_chocolade:int = 0

    input_dim_ch:str = input("enter 2 numbers separated by commas for the size of the chocolate bar: ")
    
    if not ','  in input_dim_ch:
        raise Exception(f"Chocolate dimension error !")

    else:
        dim_size_chocolade = input_dim_ch.split(',')
        if len(dim_size_chocolade) > 1:
            width_chocolade = int(dim_size_chocolade[0])
            height_chocolade = int(dim_size_chocolade[1])
        else:
            raise Exception(f"Chocolate dimension error !")

    cute_size_ch:str = input("enter the size of a piece chocolate: ")

    if not cute_size_ch.isnumeric():
        raise Exception(f"Piece size error !")
    
    size_piece:int = int(cute_size_ch)
    area_chocolade:int = width_chocolade * height_chocolade
    if area_chocolade % 2 == 0 and size_piece % 2 == 0:
        if area_chocolade > size_piece:
            return True
        else:
            return False
    return False