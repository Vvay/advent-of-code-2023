
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

def get_min_cube_set(game_record):
  red_count, green_count, blue_count = 0, 0, 0
  game_sets = game_record.split(';')
  for game_set in game_sets:
    new_red_count, new_green_count, new_blue_count = extract_cube_set(game_set)
    if new_red_count > red_count:
      red_count = new_red_count
    if new_green_count > green_count:
      green_count = new_green_count
    if new_blue_count > blue_count:
      blue_count = new_blue_count

  return red_count, green_count, blue_count

def process_records(records):
  result = []
  for record in records:
    _, game_record = record.split(':')
    red_count, green_count, blue_count = get_min_cube_set(game_record)
    result.append(red_count * green_count * blue_count)

  return result

def main():
  records = load_records()
  result = process_records(records)
  total_sum  = sum(result)

  print(total_sum)

if __name__ == "__main__":
  main()