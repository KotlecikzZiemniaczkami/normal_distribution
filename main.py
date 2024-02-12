import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# function which generates a sequence of random numbers
def random_seq(how_many: int):
    # list which will be returned with a sequence
    seq = []
    # point of generation. We generate till we have enough records in seq
    while len(seq) < how_many:
        # we need to have 2 numbers, both random, but from normal distribution
        # we will examine them later. Two seq will go only one of them
        # parameters there means N(0,1)
        num1 = np.random.normal(0, 1)
        num2 = np.random.normal(0, 1)
        # rejection conditions
        if num1 ** 2 + num2 ** 2 < 1:
            seq.append(num1)
        elif 2 * (num2 ** 2) < 1:
            seq.append(num2)
    return seq

# function which devides list for parts
def devider(parts: int, data: list):
    devided = []
    summary = 0
    counter = 0
    for i in range(len(data)):
        if counter == parts:
            summary = summary/parts
            devided.append(summary)
            summary = 0
            counter = 0
        summary += data[i]
        counter += 1
    return devided

# generating random numbers
randoms = random_seq(1000001)
how_to_devide = [1, 2, 5, 10]
data_done = {}
for i in range(len(how_to_devide)):
    data_done[str(how_to_devide[i])] = pd.Series(devider(how_to_devide[i], randoms))

# histogram
for key in data_done.keys():
    ax, fig = plt.subplots(1,1)
    data_done[key].plot(kind = 'hist', bins = 1000, title = 'simulation', xlabel = 'Values', ax = ax)
plt.show()