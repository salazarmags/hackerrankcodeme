n = int(raw_input())

if n >= 1 and n <= 100:
    if n % 2 != 0:
        print "Weird"
    elif n % 2 == 0:
        if n >= 2 and n <= 5:
            print "Not Weird"
        elif n >= 6 and n <= 20:
            print "Weird"
        else: print "Not Weird"
else: print "Number must be between 1 and 100"






