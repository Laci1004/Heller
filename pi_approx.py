import numpy as np
import random
from multiprocessing import Process
square = 0
circle = 0


def pi_approx(n):
  for i in range(1, n):
    x_coord = random.uniform(-1, 1)
    y_coord = random.uniform(-1, 1)
    square += 1
    if (x_coord ** 2 + y_coord ** 2) < 1:
      circle += 1


def main():
    p = Process(target=pi_approx, args=(1000,))
    p.start()
    p.join()