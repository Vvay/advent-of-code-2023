from posixpath import join
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

def get_nof_steps(last_node, nodes, instructions, nof_instructions):
  not_finished = True
  i = 0
  while not_finished:
    last_node = nodes[last_node][instructions[i % nof_instructions]]

    if last_node[2] == 'Z':
      not_finished = False
    i += 1

  return i

def find_a_way(input_data):
  instructions = input_data[0]
  instructions = instructions.replace('R', '1').replace('L', '0')
  instructions = list(instructions)
  instructions = [int(instruction) for instruction in instructions]
  nof_instructions = len(instructions)

  nodes   = prepare_nodes(input_data[2:])
  last_nodes = [x for x in nodes if x[2]== 'A']
  steps = []

  for last_node in last_nodes:
    steps.append(get_nof_steps(last_node, nodes, instructions, nof_instructions))

  print(steps)
  return math.lcm(*steps)

def main():
  input_data  = load_input()
  result      = find_a_way(input_data)

  print(result)

if __name__ == "__main__":
  main()