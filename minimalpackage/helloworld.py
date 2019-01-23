
"""
Reads data from text file in hellofile/names.
Each line should contain one name
The script then says hello to each name
"""

import os
from matplotlib import pyplot as plt

def readNameFile():
    current_dir = os.path.dirname(__file__)
    names_file = os.path.join(current_dir, 'hellofile', 'names.txt')
    lines = list(open(names_file))
    return lines

def say_hello(name):
    print(f'Hello, {name.rstrip()}')

def say_hello_to_everyone():
    names = readNameFile()
    for name in names:
        say_hello(name)

def plot_name_length(): 
    names = readNameFile()
    name_lengths = [len(name.rstrip()) for name in names]
    plt.figure()
    plt.ion()
    plt.plot(name_lengths)
    plt.show()


if __name__ == "__main__":
    say_hello_to_everyone()