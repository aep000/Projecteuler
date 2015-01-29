import sys
def check(num):
    num2 = int(str(num)[::-1])
    return num == num2
mx = 998001
mn = 10000
curs = mx
while curs > mn:
    if check(curs):
        val = 999
        while val >= 100:
            if curs % val == 0 and curs/val >= 100 and curs/val <= 999:
                print curs
                sys.exit()
            val -= 1
    curs -= 1