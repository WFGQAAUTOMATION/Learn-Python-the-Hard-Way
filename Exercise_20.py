from sys import argv

script, input_file = argv

# Func to print contents of file
def print_all(f):
    print f.read()

# Func to move to the beginning of the file
def rewind(f):
    f.seek(0)

# Func to print the given line from the file
def print_a_line(line_count, f):
    print line_count, f.readline()

# Opens file and loads the variable
current_file = open(input_file)

print "First let's print the whole file:\n"
print_all(current_file)

print "\nNow let's rewind, kind of like a tape.\n"
rewind(current_file)

print "Let's print three lines:\n"
current_line = 1
print_a_line(current_line, current_file)

#current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)


#current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)
