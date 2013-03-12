# imports the argv method/function from the sys module
from sys import argv

#assigns argv
script, filename = argv

# opens the file entered into the command line
txt = open(filename)

# prints the name of the file
print "Here's your file %r:" % filename

# prints the text of the file
print txt.read()

# asks the user to enter the name of the file again
print "Type the filename again:"

# takes the user input of the file name a second time
file_again = raw_input(" > ")

# opens the file again
txt_again = open(file_again)
 
# prints the text of the file again
print txt_again.read()

close(txt_again)
