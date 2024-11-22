import math

FILENAME = 'data.txt'

CARD_LABELS = 'J23456789TQKA'
HIGH_CARD, ONE_PAIR, TWO_PAIR, THREE_OF_A_KIND, FULL_HOUSE, FOUR_OF_A_KIND, FIVE_OF_A_KIND = range(7)

# Five of a kind, where all five cards have the same label: AAAAA
# Four of a kind, where four cards have the same label and one card has a different label: AA8AA
# Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
# Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
# Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
# One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
# High card, where all cards' labels are distinct: 23456

def load_input():
  content = None
  with open(FILENAME, 'r') as f:
    content = f.read()

  return content.splitlines()

def process_joker(hand):
  hand_temp = hand
  hand_temp = hand_temp.replace('J', '')
  if len(hand_temp) == 0:
    return 'AAAAA'

  hand_type = get_hand_type(hand):


  hand_temp = ''.join(sorted(hand_temp, key=lambda word: [CARD_LABELS.index(c) for c in word], reverse = True))
  joker = hand_temp[0]

  return hand.replace('J', joker)

def count_hand_characters(hand):
  char_count = {}

  for char in hand:
    char_count[char] = hand.count(char)

  return sorted(char_count.values(), reverse=True)

def get_hand_type(hand):
  char_count = count_hand_characters(hand)

  if 5 in char_count.values():
    return FIVE_OF_A_KIND

  if 4 in char_count.values():
    return FOUR_OF_A_KIND

  if 3 in char_count.values() and 2 in char_count.values():
    return FULL_HOUSE

  if 3 in char_count.values():
    return THREE_OF_A_KIND

  if 2 in char_count.values() and len(char_count) == 3:
    return TWO_PAIR

  if 2 in char_count.values():
    return ONE_PAIR

  return HIGH_CARD

def sort_hands_by_type(input_data):
  result = [list() for _ in range(7)]

  for line in input_data:
    hand = line.split(' ')
    hand[0] = process_joker(hand[0])
    result[get_hand_type(hand[0])].append(hand)

  return result

def sort_hands_by_strength(hands):
  return sorted(hands, key=lambda word: [CARD_LABELS.index(c) for c in word[0]])

def get_hands_in_order(hands):
  result = []

  for hand_type in range(7):
    if hands[hand_type] == None:
      continue

    hands[hand_type] = sort_hands_by_strength(hands[hand_type])
    result.extend(hands[hand_type])
  
  return result

def process_camel_cards(input_data):
  hands   = sort_hands_by_type(input_data)
  print(hands)
  result  = get_hands_in_order(hands)
  
  sum = 0
  for i in range(len(result)):
    sum = sum + (int(result[i][1]) * (i + 1))

  return sum

def main():
  input_data  = load_input()
  result      = process_camel_cards(input_data)

  print(result)

if __name__ == "__main__":
  main()