FILENAME = 'data.txt'

def load_records():
  content = None
  with open(FILENAME, 'r') as f:
    content = f.read()

  return content.splitlines()

def calculate_points(number_of_wins):
  return pow(2, number_of_wins - 1) if number_of_wins > 0 else 0

def check_card(card_numbers, winning_numbers):
  wins            = [number for number in card_numbers if number in winning_numbers]
  number_of_wins  = len(wins)

  return calculate_points(number_of_wins)

def extract_card_data(scratchcard):
  _, game_record  = scratchcard.split(':')
  card_data       = game_record.split('|')
  card_numbers    = card_data[0].strip().split(' ')
  card_numbers    = list(filter(None, card_numbers))
  winning_numbers = card_data[1].strip().split(' ')
  winning_numbers = list(filter(None, winning_numbers))

  return (card_numbers, winning_numbers)

def process_scratchcards(records):
  result = []
  for record in records:
    card_numbers, winning_numbers = extract_card_data(record)
    card_points = check_card(card_numbers, winning_numbers)
    result.append(card_points)

  return result

def main():
  records     = load_records()
  win_points  = process_scratchcards(records)
  total_sum   = sum(win_points)

  print(total_sum)

if __name__ == "__main__":
  main()