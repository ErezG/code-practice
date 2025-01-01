

def get_divisors_number(n):
    last_div = -1
    divs_num = 0
    for i in range(1, n + 1):
        div = n / i
        if div.is_integer():
            divs_num += 1
            last_div = div
            if div != i:
                divs_num += 1
        if last_div > 0 and i+1 >= last_div:
            break
    return divs_num
            
def get_divisors_number2(n):
    divs = set();
    for i in range(1, n + 1):
        if n % i != 0:
            continue
        divs.add(i)
        comp_div = n / i
        if comp_div in divs:
            break
        else:
            divs.add(comp_div)
    return len(divs)

def proc_arrInt(numbers):
    prime_nums = 0
    max_divs = 0
    max_div_nums = []
    for n in numbers:
        divs_num = get_divisors_number(n)
        if divs_num == 2:
            prime_nums += 1
        if divs_num > max_divs:
            max_divs = divs_num
            max_div_nums = [n]
        elif divs_num == max_divs:
            max_div_nums.append(n)
    max_div_nums.sort()
    return [len(numbers), prime_nums, [max_divs, max_div_nums]]

print(proc_arrInt([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))