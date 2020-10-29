from ghcn.types import State


def parse_states(filepath):
    states = []

    reader = open(filepath, 'r')
    for line in reader:
        abbrev = line[:2]
        name = line[3:].rstrip()
        state = State(abbrev, name)
        states.append(state)
    return states
