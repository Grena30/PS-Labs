import matplotlib.pyplot as plt
import numpy as np
import time

def generate_sequence():
  a = np.array([-2, 0, 1, -1, 3])
  b = np.array([1, 2, 0, -1])
  d = 5
  n = np.arange(1, d+1)
  c = 4
  l = np.arange(1, c+1)

  return a, b, n, l

def plot_graphs(a, b, subplot_check=False, subplot_count=1, subplot_index=1, title='basic'):
  if (subplot_check):
    plt.subplot(subplot_count, 1, subplot_index)
    
  plt.stem(a, b)
  plt.xlabel('Time index')
  plt.ylabel('Amplitude')
  plt.title(f'{title}')

def sequence_conv(a, b):
  return np.convolve(a, b)

def time_convolution(n):
  t = np.arange(0, n, 1)
  t1 = np.arange(1, n, 1)

  a = 2 * np.sign(np.sin(20 * np.pi * t1 + 1))
  b = 3 * np.cos(15 * np.pi * t + np.pi/6)

  start_time = time.time()
  c = np.convolve(a, b)

  return time.time() - start_time

def time_fft_ifft(n):
  t = np.arange(0, n, 1)
  t1 = np.arange(1, n, 1)

  a = 2 * np.sign(np.sin(20 * np.pi * t1 + 1))
  b = 3 * np.cos(15 * np.pi * t + np.pi/6)

  m = n * 2
  start_time = time.time()

  AE = np.fft.fft(a, m)
  BE = np.fft.fft(b, m)

  product = AE * BE

  y1 = np.fft.ifft(product)

  return time.time() - start_time