# pip install scikit-rf
import skrf as rf
import math
import matplotlib.pyplot as plt
import numpy as np
# Formulas from [Owen Duffy](https://owenduffy.net/calc/s11s21toloss.htm)

def plot_s_parameters(filepath):
    '''
    Plot S-parameters
    filepath = file to Touchstone S2P file.
    '''
    nw = rf.Network(filepath)
    fig, ax = plt.subplots()
    nw.plot_s_db(m=0, n=0, ax=ax, color='r')
    nw.plot_s_db(m=1, n=0, ax=ax, color='b')
    ax.grid()
    ax.set_ylabel('S-Parameters [dB]')

def calc_load_loss_dB(filepath):
    '''
    Calculate loss of connecting 2400Ω resistor in series between port 1 and port 2 using as short a connection as possible, no SMA-cable used.
    '''
    nw = rf.Network(filepath)
    s11_mag = nw.s11.s_mag.squeeze()
    s21_mag = nw.s21.s_mag.squeeze()
    # https://owenduffy.net/blog/?p=20312
    # https://owenduffy.net/calc/s11s21toloss.htm
    load_loss = (1 - np.power(s11_mag,2)) / np.power(s21_mag,2)
    load_loss_dB = 10*np.log10(load_loss)
    return load_loss_dB
    #plt.plot(nw.f, resistor_loss_db)
    #plt.xlabel('Frequency')
    #plt.ylabel('Loss')
    #plt.show()

def plot_transformer_loss(filepath_transformer, filepath_2400_cal, graph_title):
    '''
    Plot transformer loss
    filepath_transformer = file to Touchstone S2P file.
    filepath_2400_cal = Touchstone S2P file of calibration measurement of 2400 ohm between port 1 and port 2
    graph_title = title of the graph
    
    return loss_db
    '''
    fig, ax = plt.subplots()
    nw = rf.Network(filepath_transformer)
    s11_mag = nw.s11.s_mag.squeeze()
    s21_mag = nw.s21.s_mag.squeeze()
    #insertion loss [dB] = -20*log10(|s21|)
    insertion_loss_db = -20*np.log10(s21_mag)
    # Correct for the loss of the 2400Ω series resistor
    attenuator_loss_db = calc_load_loss_dB(filepath_2400_cal)
    insertion_loss_db = insertion_loss_db - attenuator_loss_db 
    #return loss [dB] = -20*log10(|s11|)
    #mismatch loss [dB] = -10*log10(1-|s11|²)
    mismatch_loss_db = -10*np.log10(1 - np.power(s11_mag,2))
    #insertion loss = loss + mismatch loss
    loss_db = insertion_loss_db- mismatch_loss_db 

    plt.plot(nw.f, loss_db)
    plt.plot(nw.f, mismatch_loss_db)
    plt.plot(nw.f, insertion_loss_db)
    plt.xlabel('Frequency')
    plt.ylabel('Loss [dB]')
    ax.set_title(graph_title)
    plt.legend(['loss', 'mismatch', 'insertion'], loc ='upper right')
    ax.grid()
    plt.show()
    return loss_db

def plot_efficiency(frequencies, loss_db, graph_title):
    '''
    Plot efficiency

    frequencies = list of frequencies
    loss_db = loss in dB
    graph_title = title of the graph
    '''
    fig, ax = plt.subplots()
    efficiency = [1/math.pow(10,x/10)*100 for x in loss_db]
    plt.plot(frequencies, efficiency)
    plt.xlabel('Frequency')
    plt.ylabel('Efficiency [%]')
    ax.set_title(graph_title)
    ax.grid()
    plt.show()