from random import randint

def dice_roller():
  yesOrNo = input('Would you like to roll a die? ')
  if (yesOrNo == 'Yes'):
    oneToSix = randint(1, 6)
    print('Your number is: ' + str(oneToSix) + '!')
  elif (yesOrNo == 'No'):
    print('Have a nice day!')
  else:
    print('Please type "Yes" or "No"')

dice_roller()