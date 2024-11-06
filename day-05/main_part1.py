import re

FILENAME = 'data.txt'

def load_file():
  content = None
  with open(FILENAME, 'r') as f:
    content = f.read()

  return content

def extract_card_data(scratchcard):
  _, game_record  = scratchcard.split(':')
  card_data       = game_record.split('|')
  card_numbers    = card_data[0].strip().split(' ')
  card_numbers    = list(filter(None, card_numbers))
  winning_numbers = card_data[1].strip().split(' ')
  winning_numbers = list(filter(None, winning_numbers))

  return (card_numbers, winning_numbers)

def get_source_number(searched_value, data_set):
  for line in data_set:
    destination_range_start, source_range_start, range_length = line.split(' ')
    destination_range_start, source_range_start, range_length = int(destination_range_start), int(source_range_start), int(range_length)
    if searched_value >= source_range_start and searched_value <= source_range_start + range_length:
      return destination_range_start + searched_value - source_range_start

  return searched_value

def process_data(content):
  seeds = re.search('(seeds:(\s\d+)*)', content).group()[7:].split(' ')
  seeds = list(map(int, seeds))
  seed_to_soil            = re.search('(seed-to-soil map:(\n\d+\s\d+\s\d+)*)',            content).group().splitlines()[1:]
  soil_to_fertilizer      = re.search('(soil-to-fertilizer map:(\n\d+\s\d+\s\d+)*)',      content).group().splitlines()[1:]
  fertilizer_to_water     = re.search('(fertilizer-to-water map:(\n\d+\s\d+\s\d+)*)',     content).group().splitlines()[1:]
  water_to_light          = re.search('(water-to-light map:(\n\d+\s\d+\s\d+)*)',          content).group().splitlines()[1:]
  light_to_temperature    = re.search('(light-to-temperature map:(\n\d+\s\d+\s\d+)*)',    content).group().splitlines()[1:]
  temperature_to_humidity = re.search('(temperature-to-humidity map:(\n\d+\s\d+\s\d+)*)', content).group().splitlines()[1:]
  humidity_to_location    = re.search('(humidity-to-location map:(\n\d+\s\d+\s\d+)*)',    content).group().splitlines()[1:]

  locations = []
  for seed in seeds:
    soil        = get_source_number(seed, seed_to_soil)
    fertilizer  = get_source_number(soil, soil_to_fertilizer)
    water       = get_source_number(fertilizer, fertilizer_to_water)
    light       = get_source_number(water, water_to_light)
    temperature = get_source_number(light, light_to_temperature)
    humidity    = get_source_number(temperature, temperature_to_humidity)
    location    = get_source_number(humidity, humidity_to_location)

    locations.append((seed, location))

  return locations

def main():
  content       = load_file()
  locations     = process_data(content)
  min_location  = min(locations, key=lambda x: x[1])

  print(min_location)

if __name__ == "__main__":
  main()