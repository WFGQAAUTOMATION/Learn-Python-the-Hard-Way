from sys import argv

script, filename = argv

# Packs the variable with the contents
# of the file.
txt = open(filename)

# Prints the file name on the screen
print "Here's your file %r:" % filename
# Prints the content of the variable
print txt.read()
# Close the file
txt.close()
# Asks for the name of the file again.
print "Type the filename again:"
# User types in the file name
file_again = raw_input("> ")
# Pack the new variable with the contents of the file
txt_again = open(file_again)
# Print the contents of the variable
print txt_again.read()
# Close the file
txt_again.close()