tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t1 Cat food
\t2 Fishies
\t3 Catnip\n\t4 Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# This loop will not end and makes a cool graphic.
while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,