import numpy as np

X = np.array(([2, 9], [1, 5], [3, 6]), dtype = float)
y = np.array(([92], [86], [89]), dtype = float)
X = X/np.amax(X, axis = 0)
y = y/np.amax(y)

def sigmoid(x):
                return (1/(1 + np.exp(-x)))

def derivatives_sigmoid(x):
                return x * (1 - x)

epoch = 7000
#epoch = 2
lr = 0.1
inputlayer_neurons = 2
hiddenlayer_neurons = 3
outputlayer_neurons = 1

#wh = 2 x 3
wh = np.random.uniform(size = (inputlayer_neurons, hiddenlayer_neurons))

#bh = 1 x 3
bh = np.random.uniform(size = (1, hiddenlayer_neurons))

#wout = 3 x 1
wout = np.random.uniform(size = (hiddenlayer_neurons, outputlayer_neurons))

#bout = 1 x1
bout = np.random.uniform(size = (1, outputlayer_neurons))

for i in range(epoch):
                #between input layer and hidden layer
                #dot product of X and wh
                hinp1 = np.dot(X, wh)
                hinp = hinp1 + bh
                hlayer_act = sigmoid(hinp)
                #between hiddden layer and output layer
                #dot product of outputs of hidden layer and wout
                outinp1 = np.dot(hlayer_act, wout)
                outinp = outinp1 + bout
                output = sigmoid(outinp)

                #BackProporgation of error
                EO = y - output
                if i == 0:
                                print('Error', EO)
                outgrad = derivatives_sigmoid(output)
                d_output = EO * outgrad
                EH = d_output.dot(wout.T)
                hiddengrad = derivatives_sigmoid(hlayer_act)

                #weight adjustments
                d_hiddenlayer = EH * hiddengrad
                wout += hlayer_act.T.dot(d_output) * lr

                bout += np.sum(d_output, axis = 0, keepdims = True)
                wh += X.T.dot(d_hiddenlayer) * lr

print('Error', EO)
print("Input : \n" + str(X))
print("Actual Output : \n" + str(y))
print("Predicted Output : \n", output)
