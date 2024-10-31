import re

FILENAME = 'data.txt'
RE = '\d'

def load_records():
  content = None
  with open(FILENAME, 'r') as f:
    content = f.read()

  return content.splitlines()

def get_calibration_value_from_record(record):
  matches = re.findall(RE, record)
  first_digit = matches[0]
  last_digit = matches[-1]

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