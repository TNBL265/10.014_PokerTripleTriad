### 1. Display cards

def card_display(number):
  """
  Display a list of value (a card)
  INPUT:  <number> (list) list of values in a card
  OUTPUT: <result> (str) this can be printed to show the card
  """
  # Convert value to symbol
  for i in range(len(number)):
    number[i] = symbol_val(number[i])
  # individual cards to show to player. Not 3x3 board form.
  pad = '  '; pad2 = pad*2 ; pad3 = pad*3 + '  '
  row = len(number) * 3 + len(pad)
  h = ''.join(['┌'] + ['─' *(row)] + ['┐']) 
  g = ''.join(['└'] + ['─' *(row)] + ['┘'])
  left_border = '\n'"│ "
  right_border = " │"'\n'
  result = h 
  result +=  left_border + pad2 + ' ' + str(number[0]) + pad2 + '  ' + right_border + '│              │' 
  result +=  left_border + ' ' + str(number[1]) + pad3  + str(number[3]) + ' ' + right_border + '│              │' 
  result += left_border + pad2 + ' ' + str(number[2]) + pad2 + '  ' + right_border 
  result += g
  return result 

def symbol_val(val):
  """
  Convert card value represented as 10, JACK, QUEEN, KING, ACE into symbol 
  INPUT:  <val> (str) values on card, can be any of 10, JACK, QUEEN, KING, ACE
  OUTPUT: <val> (str) respective symbols in T, J, Q, K, A
  """
  if str(val) == "JACK":
    val = "J"
  elif str(val) == "QUEEN":
    val = "Q"
  elif str(val) == "KING":
    val = "K"
  elif str(val) == "ACE":
    val = "A"
  elif val == 10:
    val = "T"
  return val

### 2. Display board
def show_board(board_dict):
  """
  Display an empty boards.
  Relative position (from 1 to 9) is also displayed on each empty cell.
  """
  num_list = []
  for key in board_dict:
    num_list.append(board_dict[key])

  print(board_display(num_list[0], num_list[1], num_list[2], 1))
  print(board_display(num_list[3], num_list[4], num_list[5], 2))
  print(board_display(num_list[6], num_list[7], num_list[8], 3))


def board_display(num_list1, num_list2, num_list3, row_num):
  """
  Display a list of value (a card)
  INPUT:  <num_listn> (list) list of values in a card at position n
          <row_num> (int) row position of num_list
  OUTPUT: <result> (str) can be called using print() to display the board
  """
  ind = row_num * 3
  # Graphic element of card using space and lines
  pad = ' '*2; pad2 = pad*2 ; pad3 = pad2*2 
  row = 4 * 3 + len(pad)

  top_border = ''.join(['┌'] + ['─' *(row)] + ['┐']) * 3
  bottom_border = ''.join(['└'] + ['─' *(row)] + ['┘']) * 3

  # If the card is not an empty list, prepare to display
  if num_list1 != None:
    # Convert value (10, 11, 12, 13, 14) to symbol (T, J, Q, K, A)
    for i in range(4):
      num_list1[i] = symbol_val(num_list1[i])
    a1 = str(num_list1[0])
    b1 = str(num_list1[1])
    c1 = str(num_list1[2])
    d1 = str(num_list1[3])
  # Else if no card, show empty cell
  else:
    a1 = str(ind-2)
    b1 = ' '
    c1 = ' '
    d1 = ' '

  if num_list2 != None:
    # Convert value to symbol
    for i in range(4):
      num_list2[i] = symbol_val(num_list2[i])
    a2 = str(num_list2[0])
    b2 = str(num_list2[1])
    c2 = str(num_list2[2])
    d2 = str(num_list2[3])
  else:
    a2 = str(ind-1)
    b2 = ' '
    c2 = ' '
    d2 = ' '
  
  if num_list3 != None:
    # Convert value to symbol
    for i in range(4):
      num_list3[i] = symbol_val(num_list3[i])
    a3 = str(num_list3[0])
    b3 = str(num_list3[1])
    c3 = str(num_list3[2])
    d3 = str(num_list3[3])
  else:
    a3 = str(ind)
    b3 = ' '
    c3 = ' '
    d3 = ' ' 
  
  # inserting card number values into card.          
  #      n1
  #  n2      n4
  #      n3       form.
  num1_row1 = a1
  num2_row1 = a2
  num3_row1 = a3

  num1_row2 = b1 + pad3  + d1
  num2_row2 = b2 + pad3  + d2
  num3_row2 = b3 + pad3  + d3
  
  num1_row3 = c1
  num2_row3 = c2
  num3_row3 = c3

  left_border = '\n'"│ "
  right_border1 = pad2 + ' ' + num1_row1 + pad2 + pad
  right_border1 += " │" '│' + pad2 + '  ' + num2_row1 + pad2 + '   ' + '│' 
  right_border1 += '│' + pad2 + '  ' + num3_row1 + pad2 + '   ' + '│''\n'

  right_border2 = ' ' + num1_row2 + ' '
  right_border2 += " │" '│' '  ' +  num2_row2 + '  ''│'
  right_border2 +='│' '  ' +  num3_row2 + '  ''│'+'\n'

  right_border3 = pad2 + ' ' + num1_row3 + pad2 + '  '
  right_border3 += " │" '│' + pad2 + '  ' + num2_row3 + pad2 + '   ' + '│' 
  right_border3 += '│' + pad2 + '  ' + num3_row3 + pad2 + '   ' + '│''\n'
  blank= 3 *('│              │' )
  # combining different rows generated to form a card as a whole.
  result = top_border
  result +=  left_border  + right_border1 + blank
  result +=  left_border + right_border2 + blank
  result += left_border + right_border3 
  result += bottom_border
  return result

