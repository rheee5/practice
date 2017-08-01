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
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the fifle."

target.write("%s\n%s\n%s" % (line1, line2, line3))

print "ANd finally, we close it."
target.close()