#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 09:21:34 2019

@author: iquaye
"""
import math
import matplotlib.pyplot as plt
from wav_utils import *
j = 1j

def DTFT_value(x, omega):
    """
    Takes a list of samples of a time-domain signal, and a value of omega; and
    returns a single number representing X(omega), where X is the DTFT of the
    given sequence.

    For example:
        value = DTFT_value([1, 1, 1, 1, 1], math.pi/4)
    """
    result = 0
    for n in range(len(x)):
        result+=x[n]*math.e**(-j*omega*n)
    return result
    

#def DTFT_function(x):
#    """
#    Takes a list of samples of a time-domain signal, and returns a Python
#    function representing X(.), which takes a value of omega as input and
#    returns the value of X(omega).
#
#    For example:
#        f = DTFT_function([1, 1, 1, 1, 1])
#        value = f(math.pi/4)
#    """
#    def X(omega):
#        pass  # your code here
#    return X

def plot_DTFT(fname):
    y_real =[]
    y_imag =[]
    x =[]
    samples, fs = wav_read(fname)
    d_omega = 0.01
    omega = 0
    while omega<2*math.pi:
        y_real.append(DTFT_value(samples,omega).real)
        y_imag.append(DTFT_value(samples,omega).imag)
        if DTFT_value(samples,omega).real > 150:
            print(omega)
        x.append(omega)
        omega +=d_omega
    return (x,y_real,y_imag)

cos1 = plot_DTFT("cos1.wav")
cos2 = plot_DTFT("cos2.wav")
cos3 = plot_DTFT("cos3.wav")
cos4 = plot_DTFT("cos4.wav")
cos5 = plot_DTFT("cos5.wav")
cos6 = plot_DTFT("cos6.wav")


fig = plt.figure()
ax1 = fig.add_subplot(211)
ax1.plot(cos6[0],cos6[1])
ax1 = fig.add_subplot(212)
ax1.plot(cos6[0],cos6[2])
plt.show()