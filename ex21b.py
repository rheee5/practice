def add(a, b):
	print "Adding %d + %d" % (a, b)
	return a + b 

def subtract(a, b):
	print "Subtracting %d - %d" % (a, b)
	return a - b 

def multiply(a, b):
	print "Multiplying %d * %d" % (a, b)
	return a * b 

def divide(a, b):
	print "Dividing %d / %d" % (a, b)
	return a / b 
	
	
print "Let's do some math with just functions!"

print "Let's add two numbers to calculate age"
print "Enter a number for Age A1" 
a1 = float(raw_input())
print "Enter a number for Age B1" 
b1 = float(raw_input())
age = add(a1, b1)
height = subtract(3, 3)
weight = multiply(4, 2)
iq = divide(5, 2)

print "Age: %d, Height: %d, weight: %d, iq: %d" % (age, height, weight, iq)


# A puzzle for extra credit, type it in anyway
print "Here is a puzzle"

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"
