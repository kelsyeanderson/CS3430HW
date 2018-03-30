#!/usr/bin/python

#########################################
# module: img_ann.py
# Kelsye Anderson
# A02093326
#########################################

'''
websites used
https://wiki.python.org/moin/UsingPickle
'''



import numpy as np
import pickle

from img_ann_data import DATA, X, y, EVAL_DATA, EX, ey

# sigmoid function you may want to use in training/evaluating
# your ANN.
def sigmoid(x, deriv=False):
    if (deriv == True):
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))

def build_5_layer_nn(wmats_list):
    ## your code
    ansList = []
    for x in range(len(wmats_list) - 1):
        ansList.append(np.random.randn(wmats_list[0], wmats_list[1]))
        del wmats_list[0]
    return tuple(ansList)
    pass

def train_5_layer_nn(numIters, X, y, build):
    ## your code
    W1, W2, W3, W4 = build()
    for i in range(numIters):
        Z2 = np.dot(X, W1)
        a2 = sigmoid(Z2)

        Z3 = np.dot(a2, W2)
        a3 = sigmoid(Z3)

        Z4 = np.dot(a3, W3)
        a4 = sigmoid(Z4)

        Z5 = np.dot(a4, W4)
        yHat = sigmoid(Z5)

        yHat_error = y - yHat
        yHat_delta = yHat_error * sigmoid(yHat, deriv=True)

        a4_error = yHat_delta.dot(W4.T)
        a4_delta = a4_error * sigmoid(a3, deriv= True)

        a3_error = a4_delta.dot(W3.T)
        a3_delta = a3_error * sigmoid(a3, deriv=True)

        a2_error = a3_delta.dot(W2.T)
        a2_delta = a2_error * sigmoid(a2, deriv=True)

        W4 += a4.T.dot(yHat_delta)
        W3 += a3.T.dot(a4_delta)
        W2 += a2.T.dot(a3_delta)
        W1 += X.T.dot(a2_delta)
    return W1, W2, W3, W4

def fit_5_layer_nn(x, wmats, thresh=0.4, thresh_flag=False):
    ## your code
    a2 = sigmoid(np.dot(x, wmats[0]))
    a3 = sigmoid(np.dot(a2, wmats[1]))
    a4 = sigmoid(np.dot(a3, wmats[2]))
    yHat = sigmoid(np.dot(a4, wmats[3]))
    if thresh_flag == True:
        for y in np.nditer(yHat, op_flags=['readwrite']):
            if y > thresh:
                y[...] = 1
            else:
                y[...] = 0
        return yHat.astype(int)
    else:
        return yHat

def eval_img_nn(fit_fun, wmats, EX, ey):
    count = 0
    acc = 0
    for i in range(len(EX)):
        if np.array_equal(fit_fun(EX[i], wmats, thresh_flag=True), ey[i]) == True:
            acc += 1
        count += 1
    return float(acc)/count

def find_best_nn(lower_num_iters, upper_num_iters, step, train_fun, fit_fun, eval_fun, bn, X, y):
    for numIters in range(lower_num_iters, upper_num_iters, step):
        wmats = train_fun(numIters, X, y, bn)
        acc = eval_fun(fit_fun, wmats, X, y)
        print (numIters, acc)
        if acc > 0.8:
            return wmats
    return None
          
def pickle_nn(fp, wmats):
    ## your code
    with open(fp, "wb") as file:
        pickle.dump(wmats, file)

def unpickle_nn(fp):
    ## your code
    pickle.load(open(fp, "wb"))



    

    