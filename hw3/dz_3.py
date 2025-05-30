def is_prime(number:int)->bool:
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False
    return True

def dz_3(numbers:list[int])->list[tuple]:
    result:list[bool] = list(map(is_prime, numbers))
    result:list[tuple] = list(zip(numbers, result))

    return result