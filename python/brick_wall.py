def calc_bricks(width, height):
    s, m, l = 0, 0, 0
    l_per_row = width // 60
    rows = height // 5
    for i in range(rows):
        if i % 3 == 0:
            l += l_per_row
        else:
            s += 1
            m += 1
            l += l_per_row - 1
    return f"{l}L{m}M{s}S" if rows > 1 else f"{l}L"

calc_bricks(180, 45)