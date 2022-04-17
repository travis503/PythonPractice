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
  weapons_room = ShipRoom('the weapons room', 'the lasers', 'The lasers are misaligned.', 'The lasers are perfectly aligned.', False, False, False, False, True, None, None, None, 'the medbay')
  shields_room = ShipRoom('the shields room', 'the shields', 'The shields are flickering.', 'The engines are holding strong.', False, False, False, False, True, None, None, None, 'the medbay')
  navigation_room = ShipRoom('the navigation room', 'the starmap', 'The starmap is faded.', 'The starmap is nice and vivid.', False, False, False, False, True, None, None, None, 'the medbay')
  engine_room.forward = medbay_room
  medbay_room.forward = navigation_room
  medbay_room.left = weapons_room
  medbay_room.right = shields_room
  weapons_room.behind = medbay_room
  shields_room.behind = medbay_room
  navigation_room.behind = medbay_room

  global position
  position = engine_room
  global victory_conditions_met
  victory_conditions_met = 0

  def describe_room(room):
    global victory_conditions_met
    global position
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
      print('Behind you is the ' + room.behind_room + ".")
    while (not(user_choice_valid)):
      user_choice = input('What would you like to do? ')
      user_choice = user_choice.lower()
      if (user_choice.lower() not in ['left', 'right', 'forward', 'back', 'fix', 'quit']):
        print("Please enter 'left', 'right', 'forward', 'back', 'fix', or 'quit'. ")
      else:
        user_choice_valid = True
    if (user_choice == 'fix'):
      if (not(room.issue_is_fixed)):
        print("You fixed " + room.issue + "!")
        room.issue_is_fixed = True
        victory_conditions_met += 1
      else:
        print("You've already fixed that.")
    if (user_choice == 'quit'):
      victory_conditions_met = 6
    if (user_choice == 'forward'):
      if (room.forward):
        position = room.forward
      else:
        print("There's nothing ahead of you.")
    if (user_choice == 'left'):
      if (room.left):
        position = room.left
      else:
        print("There's nothing to your left.")
    if (user_choice == 'right'):
      if (room.right):
        position = room.right
      else:
        print("There's nothing to the right.")
    if (user_choice == 'back'):
      if (room.behind):
        position = room.behind
      else:
        print("There's no going back.")


  print("Welcome to the adventure! You are adrift in space, and your ship has been damaged. Traverse the ship and fix the damaged components to continue on your mission!")
  print("Progress by inputting 'left', 'right', 'forward', 'back', or 'fix'. Type 'quit' to exit. Good luck!")
  while (victory_conditions_met < 5):
    describe_room(position)
  if (victory_conditions_met == 6):
    print('The imposters win!')
    return
  # if (victory_conditions_met == 5):
  print("The ship is repaird, and you're ready to blast off. You win!")



adventure_game()