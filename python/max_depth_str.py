from typing import List, Tuple

def strings_in_max_depth(s):
    depth = max_depth = 0
    depth_strs: List[Tuple[int, int]] = [(0, len(s)-1)]
    start_idx = None
    for i, c in enumerate(s):
        if c == "(":
            depth += 1
            if depth > max_depth:
                max_depth = depth
                depth_strs = []
            if depth == max_depth:
                start_idx = i+1
        if c == ")":
            if depth == max_depth:
                depth_strs.append((start_idx, i-1))
                start_idx = None
            depth -= 1
    
    return [s[start: end+1] for start, end in depth_strs]

print(strings_in_max_depth("sd(g)dsa"))
print(strings_in_max_depth("sd(g)dsa()"))
print(strings_in_max_depth("()sd(g)dsa"))
print(strings_in_max_depth("()s(d(g))ds((a))"))
print(strings_in_max_depth("AA(XX((YY))(U))"))
print(strings_in_max_depth("AA"))
print(strings_in_max_depth(""))