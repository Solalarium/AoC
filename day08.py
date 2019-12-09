from util import Day
import numpy as np
import matplotlib.pyplot as plt

def get_layers(obj, wide, tall):
    layers = {}
    for i in range(0,len(obj.data[0]),(wide*tall)):
        layers[i//(wide*tall)] = []
        for j in range(i,i+(wide*tall),wide):
            layers[i//(wide*tall)].append(obj.data[0][j:j+wide])
    return layers

def fewest_zero_layer(layers):
    minimum = np.inf
    for k in layers:
        zero_count = 0
        for i in layers[k]:
            i = list(i)
            zero_count += i.count('0')
        if zero_count < minimum:
            minimum = zero_count
            min_layer = k
    return min_layer

def number_of_x_digits(layers, layer, x):
    count = 0
    for i in layers[layer]:
            i = list(i)
            count += i.count(x)
    return count

def str_to_list(layers):
    for i in range(0,len(layers)):
        for j in range(0,len(layers[0])):
            layers[i][j] = list(layers[i][j])
    return layers

def decode_image(layers):
    for i in range(1,len(layers)):
        for j in range(0,len(layers[0])):
            for k in range(0,len(layers[0][j])):
                if layers[0][j][k] == '2' or layers[0][j][k] == 2:
                    layers[0][j][k] = int(layers[0+i][j][k])
                elif layers[0][j][k] == '1':
                    layers[0][j][k] = 1
                elif layers[0][j][k] == '0':
                    layers[0][j][k] = 0
    return layers[0]

if __name__ == "__main__":

    # --Part1--
    # part1 = Day(8,1)
    # part1.load(typing=str)
    # layers = get_layers(part1, 25, 6)
    # zero_layer = fewest_zero_layer(layers)
    # print(part1.answer(number_of_x_digits(layers,zero_layer,'1')*number_of_x_digits(layers,zero_layer,'2')))

    # --Part2-- LGYHB
    part2 = Day(8,2)
    part2.load(typing=str)
    layers = get_layers(part2, 25, 6)
    print(str_to_list(layers))
    print(decode_image(str_to_list(layers)))
    plt.imshow(decode_image(str_to_list(layers)))
    plt.show()
    
