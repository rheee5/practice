from sys import argv

script, file = argv

print "We're going to erase %r." % file
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(file, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")

print "I'm going to write these to the file."

target.write(line1)

print "ANd finally, we close it."
target.close()