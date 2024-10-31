RED_COUNT = 12
GREEN_COUNT= 13
BLUE_COUNT = 14

FILENAME = 'data.txt'

def load_records():
  content = None
  with open(FILENAME, 'r') as f:
    content = f.read()

  return content.splitlines()

def extract_cube_set(game_set):
  cubes = game_set.split(',')
  red_count, green_count, blue_count = 0, 0, 0
  for cube in cubes:
    parts = cube.strip().split()
    if not parts:
      continue

    count = int(parts[0])
    color = parts[1]
    if color == 'red':
      red_count += count
    elif color == 'green':
      green_count += count
    elif color == 'blue':
      blue_count += count

  return red_count, green_count, blue_count

def check_game_record(game_record):
  game_sets = game_record.split(';')
  for game_set in game_sets:
    red_count, green_count, blue_count = extract_cube_set(game_set)
    if red_count > RED_COUNT or green_count > GREEN_COUNT or blue_count > BLUE_COUNT:
      return False

  return True

def extract_game_id(input_string):
  parts = input_string.split()
  for part in parts:
    if part.isdigit():
      return int(part)

  return None

def process_records(records):
  result = []
  for record in records:
    game_id, game_record = record.split(':')
    if check_game_record(game_record):
      result.append(extract_game_id(game_id))

  return result

def main():
  records = load_records()
  game_ids = process_records(records)
  total_sum  = sum(game_ids)

  print(total_sum)

if __name__ == "__main__":
  main()