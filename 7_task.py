import sys
def check(num, li):
    for val in li:
        if num % val == 0:
            return False
    return True
li = [2]
found = False
count = 3
while not found:
    if check(count, li):
        li.append(count)
        if len(li) == 10001:
            print "found "
            print count
            sys.exit()
        print count
    
    
    count += 2
print n