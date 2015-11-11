def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)


print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


crackers = raw_input("How many crackers do you have? ")
cheese = raw_input("How much cheese do you have? ")
cheese_and_crackers(int(cheese), int(crackers))


def this_is_not_difficult(place1, place2):
    print "Do you like %s" % place1
    print "I like %s" % place2
    print "Do you want %s or %s \n" % (place1, place2)

best_taco = "Del Taco"
best_steak = "Subway"

this_is_not_difficult(best_steak,best_taco)
this_is_not_difficult("Taco Bell", "Stoney River")
