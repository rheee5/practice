# bobcounter.py

# Assume s is a string of lower case characters.

# Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print: Number of times bob occurs is: 2

s = 'azcbobobeggbobhakl'
sub_string = 'bob'
counter = 0
lengthStr = len(s)  # counts the length of the string we're searching at
lengthSubStr = len(sub_string)  # counts the length of the substring we look for
for i in range(lengthStr):  # does a for loop going through the length of the string
    if s[i:i + lengthSubStr] == sub_string:  # searches i:i + lengthSubStr index's to see if it's equal to our substring, if so add the
        counter += 1
print('Number of times bob occurs is: ' + str(counter))
