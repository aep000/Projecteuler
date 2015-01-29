val = 1000
total = 0
while val > 0:
    val -= 1
    if val % 5 == 0:
        total += val
    elif val % 3 == 0:
        total += val
print total