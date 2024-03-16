import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter, sawtooth

image_counter = 1
folder_path = './graphs/'

def generate_white_noise(Ts, range):
    t = np.arange(0, range + Ts, Ts)
    x = np.random.randn(len(t))
    
    return t, x
    
    
def plot_signal(t, x, title=None, histogram=False):
    global image_counter
    if histogram:
        plt.hist(x, bins=50, color='skyblue', edgecolor='black')
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.title(title if title else 'Histogram of white noise')
        plt.grid(axis='y', alpha=0.75)
        plt.savefig(f'{folder_path}{image_counter}. {title}.png')
        image_counter += 1
        plt.show()
        return
    else:
        plt.plot(t, x)
        plt.grid()
        plt.xlabel('Time(s)')
        plt.ylabel('Function y(t)')
        plt.title(title if title else 'White noise signal')
        plt.savefig(f'{folder_path}{image_counter}. {title}.png')
        image_counter += 1
        plt.show()
        return


def filter_signal(Ts, x):
    om0 = 2 * np.pi
    dz = 0.005
    A = 1
    oms = om0 * Ts
    a = [1 + 2 * dz * oms + oms ** 2, -2 * (1 + dz * oms), 1]
    b = [A * 2 * oms ** 2]
    y1 = lfilter(b, a, x) 
    
    return y1


def generate_signal(R, step,sawtooth_signal=False, random=False):
    m = np.arange(0, R, step)
    if random:
        d = np.random.rand(len(m)) - 0.5
        
        return m, d
    
    if sawtooth_signal:
        s = 2 * sawtooth(3 * np.pi * m + np.pi/6)
        return m, s
    
    s = 2 * m * (0.9 ** m)
    
    return m, s


def plot_multiple_signals(m, signals, labels=None, title=None):
    global image_counter
    if not labels:
        labels = [f'Signal {i+1}' for i in range(len(signals))]
        
    for i in range(len(signals)):
        plt.plot(m, signals[i], label=labels[i])
    
    plt.grid()
    plt.xlabel('Time index n')
    plt.ylabel('Amplitude')
    plt.title(title if title else 'Multiple signals')
    
    if len(signals) > 1:
        plt.legend()
        
    plt.savefig(f'{folder_path}{image_counter}. {title}.png')
    image_counter += 1
    plt.show()


def filter_signal_mfa(M, x):
    a = 1
    b = np.ones(M) / M
    y1 = lfilter(b, a, x) 
    
    return y1