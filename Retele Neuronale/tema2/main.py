import _pickle as cPickle
import numpy as np
import gzip

f = gzip.open('mnist.pkl.gz', 'rb')
train_set, valid_set, test_set = cPickle.load(f, encoding="latin1")
f.close()


weights = np.zeros((10, 784))
biases = np.zeros((10, 1))

rate = 0.2


def activation(input):
    if input > 0:
        return 1
    return 0

def online_training(nr_iterations, perceptron):
    all_classified = False
    while not all_classified and nr_iterations:
        all_classified = True
        for i in range(50000):
            x = np.array(train_set[0][i]).transpose()
            z = np.matmul(np.array(weights[perceptron]), x) + biases[perceptron]
            output = activation(z)
            t = 1 if train_set[1][i] == perceptron else 0
            if t != output:
                weights[perceptron] = np.add(weights[perceptron], np.dot(x, (t - output) * rate).transpose())
                biases[perceptron] = biases[perceptron] + rate * (t - output)
                all_classified = False
        nr_iterations -= 1




def accuracy():
    count = 0
    for i in range(10000):
        m = np.matmul(np.array(test_set[0][i]), weights.transpose())
        m = m + biases.transpose()
        for j in range(10):

            m[0][j] = activation(m[0][j])
            if j == test_set[1][i] and m[0][j] == 1 or j != test_set[1][i] and m[0][j] == 0:
                count += 1

    return count/100000


def accuracy1():
    count = 0
    for i in range(10000):
        m = np.matmul(np.array(test_set[0][i]), weights.transpose())
        m = m + biases.transpose()
        for j in range(10):

            m[0][j] = activation(m[0][j])
            if j == test_set[1][i] and m[0][j] == 1 or j != test_set[1][i] and m[0][j] == 0:
                count += 1
            else:
                count -= 1

    return count/100000


def acc_perceptron(perceptron):
    count = 0
    for i in range(10000):
        x = np.array(test_set[0][i]).transpose()
        z = np.matmul(np.array(weights[perceptron]), x) + biases[perceptron]
        t = 1 if test_set[1][i] == perceptron else 0
        if activation(z) == t:
            count += 1
    return count / 10000

def accuracy2():
    count = 0
    for i in range(10000):
        m = np.matmul(np.array(test_set[0][i]), weights.transpose())
        m = m + biases.transpose()
        correct = True
        for j in range(10):
            m[0][j] = activation(m[0][j])
            if j == test_set[1][i] and m[0][j] == 0:
                correct = False
                break
            elif j != test_set[1][i] and m[0][j] == 1:
                correct = False
                break
        if correct:
            count += 1
    return count/10000


def accuracy3():
    count = 0
    for i in range(10000):
        m = np.matmul(np.array(test_set[0][i]), weights.transpose())
        m = m + biases.transpose()
        maxim = -1
        ind_max = -1
        for j in range(10):
            if maxim < m[0][j]:
                maxim = m[0][j]
                ind_max = j

        if ind_max == test_set[1][i]:
            count += 1
    return count / 10000


if __name__ == "__main__":
    rate = 0.001
    weights = np.load("weights1.npy")
    biases = np.load("biases1.npy")
    print(accuracy())
    print(accuracy1())
    print(accuracy2())
    aux = accuracy3()
    print(aux)


    while aux < 0.95:
        for i in range(10):
            online_training(5, i)
        aux = accuracy3()
        print(aux)

    np.save("weights2", weights)

    np.save("biases2", biases)


'''
retele tema -> dimensiune fixa la comenzi ca sa nu citesc octet cu octet pana la new line
- de trimis mai intai dimensiunea raspunsului
- autentificare, nu am nevoie de parola n stuff
    doar nu vector de utilizatori, daca am sau nu am, si permite aces 
- find recursiva
'''
