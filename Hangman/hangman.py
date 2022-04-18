from random import randint

def hangman():
  print('Hangman!')
  global answer
  global answer_word
  global guesses_left
  global word_revealed
  global guessed_letters
  answer_word = ''
  answer = []
  guesses_left = 7
  guessed_letters = []
  word_revealed = False

  def generate_answer():
    answer_bank = ['warthog', 'mutant', 'iris', 'microphone', 'trash', 'squad', 'verbiage', 'keyring', 'bottle', 'waltz']
    this_answer = answer_bank[randint(0, len(answer_bank) -1)]
    print('Guess a ' + str(len(this_answer)) + ' letter word.')
    return this_answer

  def check_response(response):
    print('You guessed: ' + response)
    global answer
    global answer_word
    global guesses_left
    global word_revealed
    if (response not in answer):
      guesses_left -= 1
      print('Nope! ' + str(guesses_left) + ' guesses left.')
    else:
      for i in (range(0, len(answer) - 1, 2)):
        if (answer[i] == response):
          answer[i + 1] = 1
    word_revealed = True
    revealed = ''
    for i in range(0, len(answer) - 1, 2):
      if (answer[i + 1] == 0):
        revealed += '_'
        word_revealed = False
      elif (answer[i + 1] == 1):
        revealed += answer[i]
    print(revealed)

  def validate_response(response):
    try:
      val = int(response)
      return False
    except:
      try:
       val = float(response)
       return False
      except:
        return True

  answer_word = generate_answer()
  for i in range(len(answer_word)):
    answer.append(answer_word[i])
    answer.append(0)

  # print('The answer is: ' + answer_word)
  # print('Answer key: ' + str(answer))

  while (guesses_left > 0 and not(word_revealed)):

    guess = input('Guess a word or letter: ')
    is_valid = validate_response(guess)
    if (not(is_valid)):
      print('Need a letter or word there, bucko.')
    else:
      if (len(guess) > 1):
        if (guess == answer_word):
          print('You win!')
          return
        else:
          guesses_left -= 1
          print('Nope! ' + str(guesses_left) + ' guesses left.')
      else:
        if (guess in guessed_letters):
          print("You've already guessed that letter!")
        else:
          guessed_letters.append(guess)
          check_response(guess)
          if (word_revealed):
            print('You win!')
            return

  print("Too bad, you've been hanged!")


hangman()