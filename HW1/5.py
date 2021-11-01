numbers = list(range(1, 100))

while True:
    mid = len(numbers) // 2
    if len(numbers) == 0 or mid == 99:
        print('cant find your number')
        break
    guess = numbers[mid]
    print('is', guess, 'your number?')
    user_answer = input()
    if user_answer.lower() == 'k':
        numbers = numbers[:mid]
        continue
    elif user_answer.lower() == 'b':
        numbers = numbers[mid:]
        continue
    elif user_answer.lower() == 'd':
        print('found your number', guess)
        break
    else:
        print('invalid input')
