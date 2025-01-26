def closest(lst):
    min_gap = abs(lst[0])
    nums_in_gap = set(lst[:1])
    for n in lst[1:]:
        if abs(n) < min_gap:
            min_gap = abs(n)
            nums_in_gap.clear()
            nums_in_gap.add(n)
        elif abs(n) == min_gap:
            nums_in_gap.add(n)
    if len(nums_in_gap) == 1:
        return nums_in_gap.pop()
    return None

def closest2(lst):
    m = min(lst, key=abs)
    return m if m == 0 or -m not in lst else None

print(closest2([10, 3, 9, 1]))
print(closest2([2, 4, -1, -3]))
print(closest2([5, 2, -2]))
print(closest2([5, 2, 2]))