from sys import argv

script, file = argv

print "We're going to read %r." % file
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("You ready?")

print "Opening the file..."
target = open(file, 'r')

print "Reading the file!"

print target.read()
target.close()