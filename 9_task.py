import sys
found = False
count = 1
while not found:
    tp =500000- 1000*count
    bt = 1000-count
    val = tp/bt
    c2 = val**2 + count**2
    c = c2**.5
    if val%1 == 0 and c%1 == 0:
        print "b"
        print count
        print "a"
        print val
        print "c"
        print c
        print "product"
        print count * val * c
        sys.exit()
    count +=1