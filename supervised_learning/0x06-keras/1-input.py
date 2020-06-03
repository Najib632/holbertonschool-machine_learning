#!/usr/bin/env python3
"""
Builds a neural network with the Keras library
"""
import tensorflow.keras as K


def build_model(nx, layers, activations, lambtha, keep_prob):
    """
    a function that builds a NN with Keras
    :param nx: the number of input features to the network
    :param layers: a list containing the number of nodes in each layer of the
    network
    :param activations: a list containing the activation functions used for
    each layer of the network
    :param lambtha: the L2 regularization parameter
    :param keep_prob: the probability that a node will be kept for dropout
    :return: the keras model
    """
    x = K.Input(shape=(nx,))
    layer_l2 = K.layers.Dense(layers[0], activation=activations[0],
                              kernel_regularizer=K.regularizers.l2(
                                  lambtha))
    y_prev = layer_l2(x)

    for i in range(1, len(layers)):
        layer_drop = K.layers.Dropout(1 - keep_prob)
        y = layer_drop(y_prev)
        layer_l2 = K.layers.Dense(layers[i], activation=activations[i],
                                  kernel_regularizer=K.regularizers.l2(
                                     lambtha))
        y_prev = layer_l2(y)
    model = K.Model(inputs=x, outputs=y_prev)
    return model
