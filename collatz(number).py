def collatz(number):
    if user_input % 2 == 0:
        print(user_input // 2)
        return user_input // 2
    else:
        print(user_input * 3 + 1)
        return user_input * 3 + 1


user_input = int(input('Enter a number to collatz: '))

while user_input > 1:
    collatz(user_input)
