# Assume s is a string of lower case characters.
# Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print: Number of vowels: 5
sum = 0
s = 'azcbobobegghakl'
for i in s:
    if i == ('a') or i == ('e') or i == ('i') or i == ('o') or i == ('u'):
        sum += 1

print('Number of vowels:', str(sum))
