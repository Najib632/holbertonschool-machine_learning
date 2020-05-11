#!/usr/bin/env python3
"""
Converts a numeric label vector into a one-hot matrix:
"""
import numpy as np


def one_hot_encode(Y, classes):
    """
    converts to one-hot-matrix
    :param Y: numpy.ndarray with shape (m,) containing numeric class labels
    :param classes: the maximum number of classes found in Y
    :return: a one-hot encoding of Y with shape (classes, m), or None on
    failure
    """
    if type(classes) is not int or len(Y) != classes:
        return None
    if type(Y) is not np.ndarray or len(Y) < 1:
        return None
    one_hot = np.zeros((classes, Y.max() + 1))
    one_hot[np.arange(classes), Y] = 1
    return one_hot
