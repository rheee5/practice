name = 'Edwin'
age = 30 # not a lie
height = 70.5 # inches
weight = 155 # lbs
eyes ='Brown'
teeth = 'White'
hair = 'Black'
inches = 2.54
kilograms = 2.20
fatty = 'lardo'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "In centimeters he is %d cm." % (height * inches) 
print "He's %d pounds heavy." % weight
print "In Kilograms that is %d kg" % (weight / kilograms)
print "Actually that's not too heavy." 
print "I can't call you a %s ass" % (fatty)
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If i add %d, %d, and %d i get %d." % (age, height, weight, age + height + weight)