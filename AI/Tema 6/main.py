import numpy as np


training_set = [[1, 1, 1, 0, 1, 1, 1],
                [0, 0, 1, 0, 0, 1, 0],
                [1, 0, 1, 1, 1, 0, 1],
                [1, 0, 1, 1, 0, 1, 1],
                [0, 1, 1, 1, 0, 1, 0],
                [1, 1, 0, 1, 0, 1, 1],
                [1, 1, 0, 1, 1, 1, 1],
                [1, 0, 1, 0, 0, 1, 0],
                [1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 0, 1, 1],
                [1, 1, 1, 1, 0, 1, 1]]


target = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]

def sigmoid(x):
    return 1 / (1 + np.exp(-x))
sigmoid_v = np.vectorize(sigmoid)

max_error = float(input("Eroare maxima : "))
num_iterations = int(input("Numbar de epoci : "))
lr = float(input("Rata invatare :"))
nr_layers = input("Numar straturi: ")
nr_neurons = list()
for i in range(int(nr_layers)):
    nr_neurons.append(int(input("Numar neuroni stratul " + str(i) + " : ")))


def init_network():
    network = list()
    weights = np.random.rand(nr_neurons[0], 7)  # dintre input si hidden layer
    biases = np.random.rand(1, nr_neurons[0])
    network.append([weights, biases])
    for i in range(1, len(nr_neurons)):
        weights = np.random.rand(nr_neurons[i], nr_neurons[i-1])
        biases = np.random.rand(1, nr_neurons[i])
        network.append([weights, biases])
    weights = np.random.rand(10, nr_neurons[-1])  # dintre input si hidden layer
    biases = np.random.rand(1, 10)
    network.append([weights, biases])
    return network


def init_network_delta():
    network = list()
    weights = np.zeros((nr_neurons[0], 7))
    biases = np.zeros((1, nr_neurons[0]))
    network.append([weights, biases])
    for i in range(1, len(nr_neurons)):
        weights = np.zeros((nr_neurons[i], nr_neurons[i-1]))
        biases = np.zeros((1, nr_neurons[i]))
        network.append([weights, biases])
    weights = np.zeros((10, nr_neurons[-1]))
    biases = np.zeros((1, 10))
    network.append([weights, biases])
    return network


def forword(network, inputs):
    inputs = np.array([inputs])
    my_outputs = list()
    for layer in network:
        result = np.matmul(inputs, layer[0].transpose()) # calculam outputul pt fiecare layer
        result = result + layer[1] # adaugam bias-urile
        inputs = sigmoid_v(result) # trecem prin functia sigmoid
        my_outputs.append(inputs)
    return my_outputs # outputul final


def train(network):
    MSE = list()
    for i in range(num_iterations):

        network_delta = init_network_delta()
        for k in range(10):
            my_outputs = forword(network, training_set[k]) # rezultatul retelei neuronale
            output_error = np.array(target[k]) - my_outputs[-1] # eroare output
            output_error = output_error.transpose()

            gradient = my_outputs[-1] * (1 - my_outputs[-1])
            print(gradient)
            gradient = np.multiply(gradient.transpose(), output_error) * lr
            print(gradient)
            network_delta[-1][1] = np.add(network_delta[-1][1], gradient.transpose())
            gradient = np.matmul(gradient, my_outputs[-2])
            network_delta[-1][0] = np.add(network_delta[-1][0], gradient)
            my_outputs.insert(0, np.array([training_set[k]]))
            for i in range(int(nr_layers)):
                output_error = np.matmul(network[-i-1][0].transpose(), output_error)
                gradient = my_outputs[-i-2] * (1 - my_outputs[-i-2])
                gradient = np.multiply(gradient.transpose(), output_error) * lr
                network_delta[-i-2][1] = np.add(network_delta[-i-2][1], gradient.transpose())
                gradient = np.matmul(gradient, my_outputs[-3-i])
                network_delta[-i-2][0] = np.add(network_delta[-i-2][0], gradient)

        for i in range(len(network)):
            network[i][0] =np.add(network[i][0], network_delta[i][0])

            network[i][1] = np.add(network[i][1], network_delta[i][1])

        MSE = list()
        for i in range(10):
            my_outputs = forword(network, training_set[i])
            MSE.append(np.square(np.subtract(target[i], my_outputs[-1])).mean())

        if np.array(MSE).mean() < max_error:
            print(np.array(MSE).mean())
            return network
    print(np.array(MSE).mean())
    return network


if __name__ == "__main__":
    my_network = init_network()

    #my_network = train(my_network)
    print("Done training")
    i = 0
    while i != -1:
        i = int(input())
        output = forword(my_network, training_set[i])
        print(output[-1])
        print(output[-1].argmax())

    inp = list()
    print("Introduceti lista:")
    for i in range(7):
        inp.append(int(input(str(i) + " : ")))

    output = forword(my_network, inp)
    print(output[-1].argmax())


