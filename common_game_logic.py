import random

def pause():
  """
  To pause the game so can easily see the output
  """
  _ = input('Press <ENTER> to continue')

def create_board(N):
  """
  Create a square N x N board
  INPUT:  <N> (int) is the size of the square
  OUTPUT: <board_dict> is the dictionary of the board with <key> being the absolute 
          postition and value is initiated to None
  Ref: https://stackoverflow.com/questions/20079681/initializing-a-dictionary-in-python-with-a-key-value-and-no-corresponding-values
  """
  board_dict = dict.fromkeys(list(range(1, N**2 + 1)))
  return board_dict

def coin_toss(p1, p2):
  """
  Choose one player at random to go first
  INPUT:  <p1>, <p2> are both class object Player
  OUTPUT: <p1> or <p2>
  """
  flip = random.randint(0,2)    # 2 possible outcomes,
  if flip == 0:
    print(p1.name + ' starts first!\n\n')   # each outcome is assigned to a player
    return p1
  else:
    print(p2.name + ' starts first!\n\n' )
    return p2

def place_card(board_dict, player, card_num, position):
  """
  Place a player's card to his chosen cell in the board
  INPUT:  <player> (Player object) is the current player who is placing the card
          <card_num> (int) is the key/card's name that the player wants to play
          <position> (int) from 1 to N**2 is the position on the board to be placed

  OUTPUT: <board_dict> (dict) with card (value) at the chosen position (key)

  """
  hand = player.hand
  card = hand[card_num]
  board_dict.update({position : card})
  return board_dict

def check_empty_cell(board_dict):
  """
  Check for empty cell on the board that can be played
  INPUT:  <board_dict> (dict) with card (value) at the chosen position (key)
  OUTPUT: <possible_list> (list) a list of possible key with None value from the board_dict
  """
  possible_pos = []
  for key, value in board_dict.items():
    if value == None:
      possible_pos.append(key)
  return possible_pos

def tabulate(p1, p2):
  """
  Check who owned more won_cards between 2 player at the end of the game
  INPUT:  <p1>, <p2> are both class object Player
  OUTPUT: (<player>, <margin>) a tuple with class object <player> as the winner 
                             and <margin> as the winning differences
  """
  p1_cards = sum(p1.won_cards_pos.values())
  p2_cards = sum(p2.won_cards_pos.values())

  player = p1
  if p1_cards < p2_cards:
    player = p2
  return (player, int(abs(p1_cards - p2_cards))) 