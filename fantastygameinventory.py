# Assume s is a string of lower case characters.

# Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print: Number of times bob occurs is: 2

s = 'azcbobobegghakl'
sub_string = 'bob'
counter = 0
lengthStr = len(s)
lengthSubStr = len(sub_string)
for i in range(lengthStr):
    if s[i:i + lengthSubStr] == sub_string:
        counter += 1
print('Number of times bob occurs is: ' + str(counter))
