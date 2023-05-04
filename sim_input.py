"""
Module for functions that parse the input into the simulation.
"""
import re

regex_dictionary = {
    'topology': re.compile(r'topology = (?P<topology>[a-zA-Z]+)\s+\# .*'),
    'size': re.compile(r'size = (?P<size>\d+x\d+)\s+\# .*'),
    'node_amount': re.compile(r'node_amount = (?P<node_amount>\d+)\s+\# .*\n'),
    'transmission_range': re.compile(r'transmission_range = (?P<transmission_range>\d+)\s+\# .*\n'),
    'natural_skew': re.compile(r'natural_skew = (?P<natural_skew>\d+.\d+)\s+\# .*\n'),
    'initial_offset': re.compile(r'initial_offset = (?P<initial_offset>\d+)\s+\# .*\n')
}

def parse_input(file):
    """
    Parse input file and return it as a set.
    """
    parsed_data = ["random", (10, 10), 30, 5, 0.0005, 3000]
    print(parsed_data)
    # Open the file and read through it line by line
    with open(file, 'r', encoding='utf-8') as file_object:
        line = file_object.readline()
        while line:
            for key, regex in regex_dictionary.items():
                found = regex.search(line)
                if found:
                    match key:
                        case 'topology':
                            parsed_data[0] = found.group(key)
                        case 'size':
                            dimensions = found.group(key).split('x')
                            parsed_data[1] = (int(dimensions[0]), int(dimensions[1]))
                        case 'node_amount':
                            parsed_data[2] = int(found.group(key))
                        case 'transmission_range':
                            parsed_data[3] = int(found.group(key))
                        case 'natural_skew':
                            parsed_data[4] = float(found.group(key))
                        case 'initial_offset':
                            parsed_data[5] = int(found.group(key))
                        case _:
                            pass

            line = file_object.readline()

    return parsed_data

if __name__ == '__main__':
    #Test function for module sim_input
    FILE_PATH = 'test.txt'
    data = parse_input(FILE_PATH)
    print(data)
