import _pickle as cPickle
import numpy as np
import gzip

f = gzip.open('mnist.pkl.gz', 'rb')
train_set, valid_set, test_set = cPickle.load(f, encoding="latin1")
f.close()

neurons_per_layer = [100]

lr = 0.5

def sigmoid(x):
    return 1 / (1 + np.exp(-x))
sigmoid_v = np.vectorize(sigmoid)


def softmax(x):
    exps = np.exp(x-np.max(x))
    return exps / np.sum(exps)


def init_network(nr_neurons):
    network = list()
    weights = np.random.rand(nr_neurons[0], 784)  # dintre input si hidden layer
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

def feed_forword(network, input):
    my_outputs = list()
    for layer in range(len(network)):
        result = np.matmul(input, network[layer][0].transpose()) # calculam outputul pt fiecare layer
        result = result + network[layer][1]# adaugam bias-urile
        if layer != len(network) - 1:
            input = sigmoid_v(result)  # trecem prin functia sigmoid si noul input pt urmatorul strat devine rezultatul
        else:
            input = softmax(result[0])
        my_outputs.append(input)
    return my_outputs # outputul final

def feed_forword2(network, input):
    my_outputs = list()
    for layer in range(len(network)):
        result = np.matmul(input, network[layer][0].transpose()) # calculam outputul pt fiecare layer
        result = result + network[layer][1]# adaugam bias-urile
        input = sigmoid_v(result)  # trecem prin functia sigmoid si noul input pt urmatorul strat devine rezultatul
        my_outputs.append(input)
    return my_outputs # outputul final


def init_network_delta():
    network = list()
    weights = np.zeros((neurons_per_layer[0], 784))
    biases = np.zeros((1, neurons_per_layer[0]))
    network.append([weights, biases])
    for i in range(1, len(neurons_per_layer)):
        weights = np.zeros((neurons_per_layer[i], neurons_per_layer[i-1]))
        biases = np.zeros((1, neurons_per_layer[i]))
        network.append([weights, biases])
    weights = np.zeros((10, neurons_per_layer[-1]))
    biases = np.zeros((1, 10))
    network.append([weights, biases])
    return network

def train(network):
    for x in range(2):

        network_delta = init_network_delta()
        for k in range(1000):
            my_outputs = feed_forword2(network, train_set[0][k]) # rezultatul retelei neuronale

            target = [0 for i in range(10)]
            target[train_set[1][k]] = 1

            output_error = my_outputs[-1] - np.array(target)  # eroare output
            output_error = output_error.transpose() * lr
            network_delta[-1][1] = np.add(network_delta[-1][1], output_error)
            output_error = np.array([output_error]).transpose()
            weights_delta = np.matmul(output_error, my_outputs[0])
            network_delta[-1][0] = np.add(network_delta[-1][0], weights_delta)
            my_outputs.insert(0, np.array([train_set[0][k]]))

            output_error = np.matmul(network[-1][0].transpose(), output_error)
            gradient = my_outputs[-2] * (1 - my_outputs[-2])
            gradient = np.multiply(gradient.transpose(), output_error) * lr
            network_delta[-2][1] = np.add(network_delta[-2][1], gradient.transpose())
            gradient = np.matmul(gradient, my_outputs[-3])
            network_delta[-2][0] = np.add(network_delta[-2][0], gradient)


        for i in range(len(network)):
            network[i][0] = np.add(network[i][0], network_delta[i][0] )
            network[i][1] = np.add(network[i][1], network_delta[i][1] )

        correct = 0
        for i in range(100):
            my_outputs = feed_forword(network, train_set[0][i])
            if my_outputs[-1].argmax() == train_set[1][i]:
                correct = correct + 1

        print(correct/ 1000)


    return network



def train2(network):
    MSE = list()
    for i in range(10):

        network_delta = init_network_delta()
        for k in range(1000):
            target = [0 for i in range(10)]
            target[train_set[1][k]] = 1

            my_outputs = feed_forword2(network, train_set[0][1]) # rezultatul retelei neuronale
            output_error = np.array(target) - my_outputs[-1] # eroare output
            output_error = np.array([output_error]).transpose()


            gradient = my_outputs[-1] * (1 - my_outputs[-1])
            gradient = np.multiply(gradient.transpose(), output_error) * lr
            network_delta[-1][1] = np.add(network_delta[-1][1], gradient.transpose())
            gradient = np.matmul(gradient, my_outputs[-2])
            network_delta[-1][0] = np.add(network_delta[-1][0], gradient)
            my_outputs.insert(0, train_set[1][k])
            for j in range(len(neurons_per_layer)):
                output_error = np.matmul(network[-j-1][0].transpose(), output_error)
                gradient = my_outputs[-j-2] * (1 - my_outputs[-j-2])
                gradient = np.multiply(gradient.transpose(), output_error) * lr
                network_delta[-j-2][1] = np.add(network_delta[-j-2][1], gradient.transpose())
                gradient = np.matmul(gradient, my_outputs[-3-j])
                network_delta[-j-2][0] = np.add(network_delta[-j-2][0], gradient)

        for i in range(len(network)):
            network[i][0] =np.add(network[i][0], network_delta[i][0])
            network[i][1] = np.add(network[i][1], network_delta[i][1])

        correct = 0
        for i in range(1000):
            my_outputs = feed_forword(network, train_set[0][i])
            if my_outputs[-1].argmax() == train_set[1][i]:
                correct = correct + 1
        print(correct)



    return network

def accuratete:
    for i in range(1000):
        my_outputs = feed_forword(network, train_set[0][i])
        if my_outputs[-1].argmax() == train_set[1][i]:
            correct = correct + 1
    print(correct)

if __name__ == "__main__":
    my_network = init_network(neurons_per_layer)
    train2(my_network)
    #print(train_set[0][0])
    #print(weights[-2])
    #print(weights)
    #print(feed_forword(weights, biases, train_set[0][0])[-2])
    #print(train_set[1][0])




