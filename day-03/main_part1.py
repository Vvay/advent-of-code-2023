import re

FILENAME = 'data.txt'

def load_file_to_2D_array():
  array2D = []
  with open(FILENAME, 'r') as f:
    for line in f.readlines():
      array2D.append(list(line))

  return array2D

def get_numbers_in_line(input_string):
  results = []
  for match in re.finditer(r'\d+', input_string):
    results.append((match.start(), match.end() - match.start(), int(match.group())))

  return results

def array_to_str(array_data):
  return ''.join(str(x) for x in array_data)


def array_contains_special_character(array_2D):
  for row in array_2D:
    row_str = array_to_str(row)
    if re.search(r'[^\d.]', row_str) != None:
      return True

    return False

def get_neighbors_array(number, file_content_2D, row_id):
  x, length, _ = number
  a,b,c,d = 0,0,0,0
  a = x if x == 0 else x - 1
  b = x + length if x + length == len(file_content_2D[0]) else x + length + 1
  c = row_id if row_id == 0 else row_id - 1
  d = row_id + 1 if row_id + 1 < len(file_content_2D) else row_id

  return file_content_2D[c:d][a:b]

def process_data(file_content_2D):
  result = []
  row_lenghth = len(file_content_2D[0])
  for i, row in enumerate(file_content_2D):
    row_str = array_to_str(row)
    numbers = get_numbers_in_line(row_str)
    for number in numbers:
      neigbors_2D = get_neighbors_array(number, file_content_2D, i)
      if not array_contains_special_character(neigbors_2D):
        result.append(number[2])

  return result

def main():
  file_content_2D = load_file_to_2D_array()
  game_ids = process_data(file_content_2D)
  total_sum  = sum(game_ids)

  print(total_sum)

if __name__ == "__main__":
  main()