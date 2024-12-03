import math

FILENAME = 'data.txt'

def load_input():
  content = None
  with open(FILENAME, 'r') as f:
    content = f.read()

  return content.splitlines()

def prepare_nodes(nodes):
  nodes_dict = {}
  for line in nodes:
    line = line.replace('(','').replace(')','').replace('=','').replace(',','')
    line = line.strip().split(' ')
    line = list(filter(None, line))
    nodes_dict[line[0]] = [line[1], line[2]]

  return nodes_dict

def find_a_way(input_data):
  steps = input_data[0]
  steps = steps.replace('R', '1').replace('L', '0')
  steps = list(steps)
  steps = [int(step) for step in steps]
  nof_steps = len(steps)

  nodes   = prepare_nodes(input_data[2:])
  last_node = 'AAA'

  not_finished = True
  i = 0
  while not_finished:
    last_node = nodes[last_node][steps[i % nof_steps]]

    if last_node == 'ZZZ':
      not_finished = False
    i += 1

  return i

def main():
  input_data  = load_input()
  result      = find_a_way(input_data)

  print(result)

if __name__ == "__main__":
  main()