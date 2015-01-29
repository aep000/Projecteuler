tot1 = 1
tot2 = 1

for i in range(2, 101):
    tot1 += i
    tot2 += i * i
tot = tot1 * tot1
print tot - tot2