from random import randint

def dice_roller():
  yesOrNo = input('Would you like to roll a die? ')
  while (yesOrNo.lower() == 'yes'):
    oneToSix = randint(1, 6)
    print('Your number is: ' + str(oneToSix) + '!')
    yesOrNo = input('Would you like to roll again? ')
  if (yesOrNo.lower() == 'no'):
    print('Have a nice day!')
  else:
    print('Please type "Yes" or "No" ')
    dice_roller()

dice_roller()