def update_owner(board_dict, curr_p, other_p, pos, N):
  """
  Compare current card with the neighboring cards to see if cards change owners.
  INPUT: <board_dict> (dict) with card (value) at the chosen position (key)
         <curr_p> (Player object) the person who just played the card
         <other_p> (Player object) the other person
         <pos> (int) is the position (from 1 to N**2) as absolute value on the board
         <N> (int) is the dimension of the board being played in
  """
  # For each card, there will be a list of value in ACW order: [TOP, LEFT, BOTTOM, RIGHT]
  curr_card = board_dict[pos]
  curr_p.won_cards_pos[pos] = 1

  # Given the position on the board, find list of neighboring position
  # There will be 9 cases in total (4 Corner, 4 Side and 1 Middle Case)
  neighbor_pos_list = find_neighbor(pos, N)

  # Standard comparison, by value magnitude only
  # Each player self.won_cards_pos will be updated accordingly to reflect which
  # card s/he has just won
  standard_compare(board_dict, pos, neighbor_pos_list, curr_p, other_p)

  
def find_neighbor(pos, N):
  """
  Find the neighboring position give the current played position
  INPUT:  <pos> (int) position of the card just played
          <N> (int) size of the board being played in
  OUTPUT: <neighbor_pos_dict> (dict) dictionary of neighboring postion 
          key is the relative position of the neighbor cell (TOP, BOTTOM, LEFT, RIGHT)
          and value is the absolute position of the cell (from 1 to N**2)
  """
  neighbor_pos_dict = {}

  # There will be 9 cases in total

  # Case 1: LEFT UPPER CORNER ==> 2 neighbors 
  if pos == 1:
    neighbor_pos_dict.update({'RIGHT' : pos + 1})
    neighbor_pos_dict.update({'BOTTOM' : pos + N}) 
    
  # Case 2: TOP ==> 3 neighbors
  elif 1 < pos < N:
    neighbor_pos_dict.update({'LEFT' : pos - 1})  
    neighbor_pos_dict.update({'RIGHT' : pos + 1})
    neighbor_pos_dict.update({'BOTTOM' : pos + N}) 

  # Case 3: RIGHT UPPER CORNER ==> 2 neighbors 
  elif pos == N:
    neighbor_pos_dict.update({'LEFT' : pos - 1})  
    neighbor_pos_dict.update({'BOTTOM' : pos + N}) 

  # Case 4: LEFT SIDE ==> 3 neighbors 
  elif pos%N == 1 and pos != 1 and pos != N**2 - N +1:
    neighbor_pos_dict.update({'TOP' : pos - N})
    neighbor_pos_dict.update({'RIGHT' : pos + 1})
    neighbor_pos_dict.update({'BOTTOM' : pos + N}) 

  # Case 5: RIGHT SIDE ==> 3 neighbors 
  elif pos%N == 0 and pos != N and pos != N**2:
    neighbor_pos_dict.update({'TOP' : pos - N})
    neighbor_pos_dict.update({'LEFT' : pos - 1})
    neighbor_pos_dict.update({'BOTTOM' : pos + N}) 

  # Case 6: LEFT LOWER CORNER ==> 2 neighbors
  elif pos == N**2 - N +1:
    neighbor_pos_dict.update({'TOP' : pos - N})
    neighbor_pos_dict.update({'RIGHT' : pos + 1})

  # Case 7: BOTTOM ==> 3 neighbors 
  elif N**2 - N +1 < pos < N**2:
    neighbor_pos_dict.update({'LEFT' : pos - 1})  
    neighbor_pos_dict.update({'RIGHT' : pos + 1})
    neighbor_pos_dict.update({'TOP' : pos - N}) 

  # Case 8: RIGHT LOWER CORNER ==> 2 neighbors 
  elif pos == N**2:
    neighbor_pos_dict.update({'TOP' : pos - N})
    neighbor_pos_dict.update({'LEFT' : pos - 1})

  # Case 9: MIDDLE ==> 4 neighbors
  else:
    neighbor_pos_dict.update({'LEFT' : pos - 1})  
    neighbor_pos_dict.update({'RIGHT' : pos + 1})
    neighbor_pos_dict.update({'TOP' : pos - N}) 
    neighbor_pos_dict.update({'BOTTOM' : pos + N}) 

  return neighbor_pos_dict


def standard_compare(board_dict, pos, neighbor_pos_dict, curr_p, other_p):
  """
  Do standard comparison by magnitude only
  Update curr_p.won_cards_pos and other_p.won_cards_pos accordingly 
  INPUT:  <board_dict> (dict) with card (value) at the chosen position (key)
          <pos> (int) position of the card just played
          <neighbor_pos_dict> (dict) dictiionary of position of neighboring value
          <curr_p> (Player object) the one who just played the card
          <other_p> (Player object) the other person
  """
  # Our current card to be compared:
  curr_card = board_dict[pos]
  # The total difference in value of all the neighboring values
  total_difference = 0

  # If the neighbor card is not enemy card (other_p) or is cell is None, skip comparison
  # This will be indicated by other_p.won_cards_pos[ind] == 0, meaning the enemy 
  # doesn't own the card at that position (so either me or no one own) 
  # So we will look at the absolute position
  for rel_pos, abs_pos in neighbor_pos_dict.items():
    if other_p.won_cards_pos[abs_pos] == 0:
      continue
    
    neighbor_card = board_dict[abs_pos]
    total_difference += compare_value(curr_card, neighbor_card, rel_pos)
    
  if total_difference > 0:
    print("\nThis is a winning choice!")
    # We will change all cards to curr_p (set to 1) from other_p (set to 0)
    for rel_pos, abs_pos in neighbor_pos_dict.items():
      if other_p.won_cards_pos[abs_pos] == 0:
        continue

      curr_p.won_cards_pos[abs_pos] = 1
      other_p.won_cards_pos[abs_pos] = 0

      curr_p.won_cards_pos[pos] = 1
      other_p.won_cards_pos[pos] = 0

  elif total_difference < 0:
    print("\nThis is a losing choice!")
    # We will change all cards from curr_p (set to 0) to other_p (set to 1)
    for rel_pos, abs_pos in neighbor_pos_dict.items():
      if other_p.won_cards_pos[abs_pos] == 0:
        continue

      curr_p.won_cards_pos[abs_pos] = 0
      other_p.won_cards_pos[abs_pos] = 1

      curr_p.won_cards_pos[pos] = 0
      other_p.won_cards_pos[pos] = 1

  else: # draw
    print("\nThis is a normal choice!")
    # only update our card
    curr_p.won_cards_pos[pos] = 1
    other_p.won_cards_pos[pos] = 0


def compare_value(curr_card, neighbor_card, rel_pos):
  """
  Find the difference in value between our card and a neighbor card based on the relative position
  INPUT:  <curr_card> (list) list of values on our card
          <neighbor_card> (list) list of values on neighbor_card
          <rel_pos> (int) the relative position to be compared, can be TOP, BOTTOM, LEFT or RIGHT
  OUTPUT: <difference> (int) the differnce between our value and the neighbor value
  """
  # There will be 4 cases to compare, according to TOP, BOTTOM, LEFT and RIGHT value
  if rel_pos == "TOP":
    # Compare the TOP of our card with the BOTTOM of neighbor's card
    curr_val = curr_card[0] 
    neighbor_val = neighbor_card[2]

    # If value is Jack, Queen, King or Ace, convert to 11 to 14
    curr_val = convert_val(curr_val)
    neighbor_val = convert_val(neighbor_val)

    difference = curr_val - neighbor_val

  elif rel_pos == "BOTTOM":
    # Compare the BOTTOM of our card with the TOP of neighbor's card
    curr_val = curr_card[2] 
    neighbor_val = neighbor_card[0]

    curr_val = convert_val(curr_val)
    neighbor_val = convert_val(neighbor_val)

    difference = curr_val - neighbor_val

  elif rel_pos == "LEFT":
    # Compare the LEFT value of our card with the RIGHT value of the neighbor's card
    curr_val = curr_card[1] 
    neighbor_val = neighbor_card[3]

    curr_val = convert_val(curr_val)
    neighbor_val = convert_val(neighbor_val)

    difference = curr_val - neighbor_val

  elif rel_pos == "RIGHT":
    # Compare the RIGHT value of our card with the LEFT value of the neighbor's card
    curr_val = curr_card[3] 
    neighbor_val = neighbor_card[1]

    # If value is Jack, Queen, King or Ace, convert to 11 to 14
    curr_val = convert_val(curr_val)
    neighbor_val = convert_val(neighbor_val)

    difference = curr_val - neighbor_val

  return difference


def convert_val(val):
  """
  Convert card value represented as JACK, QUEEN, KING, ACE into 11 to 14 (int)
  INPUT:  <val> (str) values on card, can be any of JACK, QUEEN, KING, ACE
  OUTPUT: <val> (int) according values on card, can be from 11 to 14
  """
  if str(val) == "J":
    val = 11
  elif str(val) == "Q":
    val = 12
  elif str(val) == "K":
    val = 13
  elif str(val) == "A":
    val = 14
  elif str(val) == "T":
    val = 10
  return val