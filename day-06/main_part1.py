import math

FILENAME = 'data.txt'

def load_input():
  content = None
  with open(FILENAME, 'r') as f:
    content = f.read()

  return content.splitlines()

def extract_data(races_data):
  _, times      = races_data[0].split(':')
  times         = times.strip().split(' ')
  times         = list(filter(None, times))
  times         = [int(time) for time in times]
  _, distances  = races_data[1].split(':')
  distances     = distances.strip().split(' ')
  distances     = list(filter(None, distances))
  distances     = [int(distance) for distance in distances]

  return times, distances

def process_races(races_data):
  times, distances  = extract_data(races_data)
  result = []

  for i, time in enumerate(times):
    better_distances = []

    for j in range(time):
      if j * (time - j) > distances[i]:
        better_distances.append(j)

    result.append(len(better_distances))

  return result

def main():
  races_data  = load_input()
  best_races  = process_races(races_data)
  result      = math.prod(best_races)

  print(result)

if __name__ == "__main__":
  main()