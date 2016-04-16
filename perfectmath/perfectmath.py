def is_perfect_number(x):
    """
    Test if the number given is perfect
    Ref: https://nl.wikipedia.org/wiki/Perfect_getal (Dutch)
    """

    dividers = []
    i = 1
    result = 0

    while i < x:
        if x % i == 0:
            dividers.append(i)

        i += 1

    for y in dividers:
        result += y

    if result == x:
        return True
    else:
        return False
