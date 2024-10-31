import regex as re

FILENAME = 'data.txt'
DIGIT_NAMES = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
RE = '\d|' + '|'.join(DIGIT_NAMES)

def load_records():
  content = None
  with open(FILENAME, 'r') as f:
    content = f.read()

  return content.splitlines()

def get_int_value(value):
  if value in DIGIT_NAMES:
    return DIGIT_NAMES.index(value) + 1

  return value

def get_calibration_value_from_record(record):
  matches = re.findall(RE, record, overlapped=True)
  first_digit = get_int_value(matches[0])
  last_digit = get_int_value(matches[-1])

  return int(str(first_digit) + str(last_digit))

def process_records(records):
  result = []
  for record in records:
    result.append(get_calibration_value_from_record(record))

  return result

def main():
  records = load_records()
  calibration_values = process_records(records)
  total_sum  = sum(calibration_values)

  print(total_sum)

if __name__ == "__main__":
  main()