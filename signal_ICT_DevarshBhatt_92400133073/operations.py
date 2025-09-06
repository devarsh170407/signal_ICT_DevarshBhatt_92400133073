import numpy as np
import matplotlib.pyplot as plt


def time_shift(signal,k):
    shifted_signal = np.roll(signal,k)
    return shifted_signal

def time_scale(signal,k):
    scale_signal = signal[::k]
    return scale_signal


def signal_addition(signal1, signal2):
    return np.add(signal1, signal2)


def signal_multiplication(signal1, signal2):
    return np.multiply(signal1,signal2)