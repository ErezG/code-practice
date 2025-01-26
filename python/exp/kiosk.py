

coins = 15
wraps = 0
chochlates = 0
while coins + wraps/3 >= 1:
    new_c = coins + int(wraps/3)
    coins = 0
    wraps = wraps%3
    chochlates += new_c
    wraps += new_c

print(chochlates)