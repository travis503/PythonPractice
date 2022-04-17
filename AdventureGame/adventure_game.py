def adventure_game():

  class ShipRoom:
    def __init__(self, name, issue, issue_broken, issue_fixed, issue_is_fixed, left, right, forward, behind, left_room, right_room, forward_room, behind_room):
      self.name = name
      self.issue = issue
      self.issue_broken = issue_broken
      self.issue_fixed = issue_fixed
      self.issue_is_fixed = issue_is_fixed
      self.left = left
      self.right = right
      self.forward = forward
      self.behind = behind
      self.left_room = left_room
      self.right_room = right_room
      self.forward_room = forward_room
      self.behind_room = behind_room

  engine_room = ShipRoom('the engine room', 'the engines', 'The engines are silent.', 'The engines are humming away.', False, False, False, True, False, None, None, 'the medbay', None)
  medbay_room = ShipRoom('the medbay', 'the bioscanner', 'The bioscanner is flashing red.', 'The bioscanner is indicating green.', False, True, True, True, True, 'the weapons room', 'the shields room', 'the navigation room', 'the engine room')
  weapons_room = ShipRoom('the engine room', 'the engines', 'The engines are silent.', 'The engines are humming away.', False, False, False, True, False, None, None, 'the medbay', None)
  shields_room = ShipRoom('the engine room', 'the engines', 'The engines are silent.', 'The engines are humming away.', False, False, False, True, False, None, None, 'the medbay', None)
  navigation_room = ShipRoom('the engine room', 'the engines', 'The engines are silent.', 'The engines are humming away.', False, False, False, True, False, None, None, 'the medbay', None)

  position = engine_room
  global victory_conditions_met
  victory_conditions_met = False

  def describe_room(room):
    global victory_conditions_met
    user_choice = ''
    user_choice_valid = False
    print("------------------------------")
    print("You are in the " + room.name + ".")
    if (room.issue_is_fixed):
      print(room.issue_fixed)
    else:
      print(room.issue_broken)
    if (room.left):
      print('To the left is the ' + room.left_room + ".")
    if (room.right):
      print('To the right is the ' + room.right_room + ".")
    if (room.forward):
      print('Ahead of you is the ' + room.forward_room + ".")
    if (room.behind):
      print('You came from the ' + room.behind_room + ".")
    while (not(user_choice_valid)):
      user_choice = input('What would you like to do? ')
      user_choice = user_choice.lower()
      if (user_choice.lower() not in ['left', 'right', 'forward', 'back', 'fix', 'win']):
        print("Please enter 'left', 'right', 'forward', 'back', or 'fix'. ")
      else:
        user_choice_valid = True
    if (user_choice == 'fix'):
      print("You fixed " + room.issue + "!")
      room.issue_is_fixed = True
    if (user_choice == 'win'):
      victory_conditions_met = True
      print('You win!')


  print("Welcome to the adventure! Progress by inputting 'left', 'right', 'forward', 'back', or 'fix'. Good luck!")
  while (not(victory_conditions_met)):
    describe_room(position)



adventure_game()