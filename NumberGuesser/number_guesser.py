from random import randint


def number_guesser():
  answer = randint(1, 100)
  print(answer)
  guess = 0
  while (guess != answer):
    guess = int(input('Guess a number: '))
    if (guess > answer):
      print('Lower!')
    elif (guess < answer):
      print('Higher!')
  print('You got it! The number was ' + str(answer) + '.')

number_guesser()