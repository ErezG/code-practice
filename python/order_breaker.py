from collections import deque


def order_breaker(input):
    prv = deque(maxlen=2)
    prv.append(input[0])
    for i in input[1:]:
        last_prv = prv[len(prv) - 1]
        if i < last_prv:
            if len(prv) == 2 and i < prv[0]:
                return i
            else:
                return last_prv
        prv.append(i)

    raise Exception("bad input - no breakers")


