def collatz(number):
    if user_input % 2 == 0:
        print(user_input // 2)
        return user_input // 2
    else:
        print(3 * user_input + 1)
        return 3 * user_input + 1

while True:
    try:
        user_input = int(input('Enter a number to collatz: '))
        break
    except ValueError:
        print('You must enter an integer')

while user_input > 1:
    user_input = collatz(user_input)
