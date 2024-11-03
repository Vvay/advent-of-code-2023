FILENAME = 'data.txt'

def load_records():
  content = None
  with open(FILENAME, 'r') as f:
    content = f.read()

  return content.splitlines()

def check_card(card_numbers, winning_numbers):
  wins = [number for number in card_numbers if number in winning_numbers]

  return len(wins)

def extract_card_data(scratchcard):
  _, game_record  = scratchcard.split(':')
  card_data       = game_record.split('|')
  card_numbers    = card_data[0].strip().split(' ')
  card_numbers    = list(filter(None, card_numbers))
  winning_numbers = card_data[1].strip().split(' ')
  winning_numbers = list(filter(None, winning_numbers))

  return (card_numbers, winning_numbers)

def process_scratchcards(records):
  scratchcard_copies = [1] * len(records)
  for i, record in enumerate(records):
    card_numbers, winning_numbers = extract_card_data(record)
    card_points = check_card(card_numbers, winning_numbers)

    for j in range(i + 1, i + card_points + 1):
      scratchcard_copies[j] += 1 * scratchcard_copies[i]

  return scratchcard_copies

def main():
  records       = load_records()
  scratchcards  = process_scratchcards(records)
  total_sum     = sum(scratchcards)

  print(total_sum)

if __name__ == "__main__":
  main()