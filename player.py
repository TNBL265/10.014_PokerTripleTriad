import random

class Player():
  """
  Player is an object representing the player with:
    N             is the dimension of the cell s/he is playing in 
    name          is the name of the player
    num_val       is the number of values to be generated on each card
    num_cards     is the number of cards each player has
    diff_lv       is a list of possible values that can be generated base on chosen difficulty
      "EASY" mode: diff_lv = [7, 14] # generate cards from 7 up to ACE
      "MEDIUM" mode: diff_lv = [4, 11] # generate cards from 4 up to JACK
      "HARD" mode: diff_lv = [2, 9] # generate cards from 2 up to 9
    hand          is a dictionary of all the cards that the player currently has
                  it has the <key> as the card's 'name' and <value> as a list of values on each card
    won_cards_pos is a dictionary with key from 1 to N**2 showing which position ont the 
                  board belongs to this player 
  """

  # Some self variables that can be called
  N = None
  num_val = 4
  num_cards = None
  name = None
  diff_lv = None
  hand = None
  won_cards_pos = None

  # __init__ to define arguments for object Cards
  def __init__(self, name, num_cards, diff_level, N):
    """
    INPUT: <name> (str) of the player
           <num_cards> (int) is the number of cards to be generated for each player
           <diff_level> (str) is the chosen difficulty level (EASY, MEDIUM or HARD)
           <N> (int) is the dimension of the board the player is playing in 
    """
    self.N = N
    self.name = name
    self.num_cards = num_cards
    self.won_cards_pos = dict.fromkeys(list(range(1, N**2 + 1)), 0)

    # Adjust difficulty level
    if diff_level == "EASY":
      self.diff_lv = [7, 14];
    elif diff_level == "MEDIUM":
      self.diff_lv = [4, 11];
    elif diff_level == "HARD":
      self.diff_lv = [2, 9];
    

  def generate_hand(self, num_val=num_val):
    """
    Generate <num_cards> cards with <num_val> values for player
    """
    # Collect constant
    num_cards = self.num_cards
    diff_lv = self.diff_lv

    tmp_hand = {}
    for k in range(num_cards): 
      # preallocate list of value for each card, this should have length of 4 eventually
      # e.g: card = [1, 2, 3, 4] means (in ACW direction): 
      # TOP value is 1; LEFT value is 2; BOTTOM value is 3; RIGHT value is 4
      card = []
      for i in range(num_val): 
        # Choose a random value from difficulty range
        n = random.randint(diff_lv[0], diff_lv[1])
        # If the number is larger than 10, convert to Poker value
        if n == 11:
          n = "JACK"
        if n == 12:
          n = "QUEEN"
        if n == 13:
          n = "KING"
        if n ==14:
          n = "ACE"

        # add each value to the card
        card.append(n)
      # after a card has been create, add to the <hand> dictionary
      tmp_hand.update({k+1 : card})
    self.hand = tmp_hand

  def update_hand(self, card_num):
    """
    Update the player's hand
    INPUT: <card_num> is the key/card's name that has just been played
    """
    self.hand.pop(card_num)