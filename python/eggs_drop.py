# https://www.codewars.com/kata/54cb771c9b30e8b5250011d4


def eggs_drop(n, m):
    """
    Parameters:
    n (int): number of eggs
    m (int): number of drop attemps
    """
    if m == 1:
        return 1
    if n == 1:
        return m
    return 1 + eggs_drop(n - 1, m - 1) + eggs_drop(n, m - 1)

def print_res(n, m):
    print(f"{n} eggs, {m} drops: {eggs_drop(n, m)}")


def eggs_drop_iter(n, m):
    floors = 0
    while n > 0 and m > 0:
        floors += m
        pass

print_res(1, 1)
print_res(2, 1)
print_res(1, 2)
print_res(2, 2)
print_res(3, 2)
print_res(2, 3)
print_res(3, 3)
print_res(1, 100)
print()
print_res(1, 4)
print_res(2, 4)
print_res(3, 4)