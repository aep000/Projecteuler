t1 = 1
t2 = 2
total = 2
limit = True
while limit:
    t3 = t1+t2
    if t3 < 4000000:
        if t3 % 2 == 0:
            total += t3
            print t3
        t1 = t2
        t2 = t3
    else:
        limit = False
print total