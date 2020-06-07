import random
import numpy as np

import _pickle as cPickle
import gzip

f = gzip.open('mnist.pkl.gz', 'rb')
train_set, valid_set, test_set = cPickle.load(f, encoding="latin1")
f.close()

sizes = [784, 100, 10]


epoci = 300

mini_batch_len = 10

lr = 0.5


def sigomid(x):
    return 1.0 / (1.0 + np.exp(-x))


def dsigmoid(x):
    return sigomid(x) * (1 - sigomid(x))


def softmax(x):
    exps = np.exp(x - np.max(x))
    return exps / np.sum(exps)


def feedforword(weights, biases, input):
    result = sigomid(np.dot(weights[0], input))
    result = softmax(np.dot(weights[1], result))
    return result


def train(weights, biases):
    for k in range(epoci):

        shuffled_test_set = list()

        indexes = list(range(len(train_set[1])))
        while indexes:
            r_index = random.randint(0, len(indexes) - 1 )
            shuffled_test_set.append((train_set[0][indexes[r_index]], train_set[1][indexes[r_index]]))
            indexes.pop(r_index)



        mini_batches = [shuffled_test_set[m:m + mini_batch_len] for m in range(0, len(train_set), mini_batch_len)]


        for mini_batch in mini_batches:
            delta_b = [np.zeros(b.shape) for b in biases]
            delta_w = [np.zeros(w.shape) for w in weights]


            for test in mini_batch:
                t_delta_b = [np.zeros(b.shape) for b in biases]
                t_delta_w = [np.zeros(w.shape) for w in weights]

                y = [[0.0 for i in range(10)]]
                y[0][test[1]] = 1.0
                y = np.array(y).transpose()
                x = np.array([test[0]]).transpose()

                layer_outputs = list()
                activation = x
                activations = [x]

                for b, w in zip(biases, weights):
                    output = np.dot(w, activation) + b
                    layer_outputs.append(output)
                    activation = sigomid(output)
                    activations.append(activation)

                #delta = (activations[-1] - y) * dsigmoid(layer_outputs[-1])
                delta = softmax(layer_outputs[-1]) - y
                t_delta_b[-1] = delta
                t_delta_w[-1] = np.dot(delta, activations[-2].transpose())
                delta = np.dot(weights[-1].transpose(), delta) * dsigmoid(layer_outputs[-2])
                t_delta_b[0] = delta
                t_delta_w[0] = np.dot(delta, activations[0].transpose())

                delta_b = [db + bb for bb, db in zip(t_delta_b, delta_b)]
                delta_w = [dw + bw for bw, dw in zip(t_delta_w, delta_w)]

            weights = [w - (lr / len(mini_batch)) * dw for w, dw in zip(weights, delta_w)]
            biases = [b - (lr / len(mini_batch)) * db for b, db in zip(biases, delta_b)]
        print(accuratete(weights, biases))
    return weights, biases

def accuratete(weights, biases):
    count = 0
    for k in range(len(test_set[1])):
        result = np.argmax(feedforword(weights, biases, test_set[0][k]))
        if result == test_set[1][k]:
            count += 1

    return count/ len(test_set[1])


if __name__ == "__main__":
    biases = [np.random.randn(i, 1) for i in sizes[1:]]
    weights = [np.random.randn(j, i) / np.sqrt(i) for i, j in zip(sizes[:-1], sizes[1:])]
    weights, biases = train(weights, biases)
    print(accuratete(weights, biases))
