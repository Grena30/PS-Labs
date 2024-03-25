import matplotlib.pyplot as plt
import numpy as np
import os
import time
from utils import *

image_counter = 1
folder_path = './graphs/'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Task 1
a, b, n, l = generate_sequence()

plt.figure(image_counter)
plot_graphs(n, a, subplot_check=True, subplot_count=2, subplot_index=1, title='Sequence A')
plot_graphs(l, b, subplot_check=True, subplot_count=2, subplot_index=2, title='Sequence B')
plt.tight_layout()
plt.savefig(f'{folder_path}{image_counter}. {"Sequences"}.png')
image_counter += 1
plt.show()

# Task 2
c = sequence_conv(a, b)
m = 8
k = np.arange(1, m+1)

plt.figure(image_counter)
plot_graphs(k, c, title='Convolution of A and B')
plt.savefig(f'{folder_path}{image_counter}. {"Convolution"}.png')
image_counter += 1
plt.show()

# Task 3
AE = np.fft.fft(a, m)
BE = np.fft.fft(b, m)

product = AE * BE

plt.figure(image_counter)
plot_graphs(k, product, title='Product of Fourier transforms')
plt.savefig(f'{folder_path}{image_counter}. {"Fourier transforms"}.png')
image_counter += 1
plt.show()

# Task 4
y1 = np.fft.ifft(product)
plt.figure(image_counter)
plot_graphs(k, y1, title='Inverse Fourier transform')
plt.savefig(f'{folder_path}{image_counter}. {"Inverse Fourier transform"}.png')
image_counter += 1
plt.show()

# Task 5
error = c[:m] - y1

plt.figure(image_counter, figsize=(10, 10))
plot_graphs(k, c, subplot_check=True, subplot_count=3, subplot_index=1, title='Convolution of A and B')
plot_graphs(k, y1, subplot_check=True, subplot_count=3, subplot_index=2, title='Inverse Fourier transform')
plot_graphs(k, error, subplot_check=True, subplot_count=3, subplot_index=3, title='Error')
plt.tight_layout()
plt.savefig(f'{folder_path}{image_counter}. {"Multiple graphs"}.png')
image_counter += 1
plt.show()

# Task 6-7

n = [2**16, 2**18]

for i in n:
  convolution = time_convolution(i)
  print("Time taken for convolution:", convolution, "seconds", "for n =", i)
  fourier = time_fft_ifft(i)
  print("Time taken for Fourier transforms and inverse Fourier transform:", fourier, "seconds", "for n =", i)

# Task 8
a = [1, 4, 2]
b = [1, 2, 3, 4, 5, 4, 3, 3, 2, 2, 1, 1]
c = np.convolve(a, b)
print("Convolution of A and B: ", c)

# Task 9
b1 = b[0:6]
b2 = b[6:]
m = np.arange(1, len(c)+1)

c1 = np.convolve(a, b1)
c2 = np.convolve(a, b2)
print("B1 block: ", b1)
print("B2 block: ", b2)
print("Convolution of A and B1: ", c1)
print("Convolution of A and B2: ", c2)

# Task 10
c_add = []
c_add.extend(c1[0:6])
c_add.extend(c1[6:8]+c2[0:2])
c_add.extend(c2[2:])

plot_graphs(m, c, title='Convolution of A and B')
plt.savefig(f'{folder_path}{image_counter}. {"Convolution v2"}.png')
image_counter += 1
plt.show()