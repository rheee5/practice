# version 2 of mit 600 week 1 problem 3
previousChar = ''
currentSub = ''
maxSub = ''
s = 'ifaewabcjioabcdef'

for char in s:
    if char >= previousChar:
        currentSub += char
        if len(currentSub) > len(maxSub):
            maxSub = currentSub
    else:
        currentSub = char
    previousChar = char
print(maxSub)
