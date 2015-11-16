numbers = []


def print_nums(counter):
    i = 0
    while i < counter:
        print "At the top i is %d" % i
        numbers.append(i)

        i += 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i


print_nums(6)

print "The numbers: "

for num in numbers:
    print num
