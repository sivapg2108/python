import random
target_num, guess_num = random.randint(1, 9), 0
while target_num != guess_num:
    guess_num = int(input('Guess a number between 1 and 9 until you get it right : '))
print('Well guessed!')
