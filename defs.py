from random import random
import numpy as np

def rarray(n):
    "Array of n random elements."
    return np.array([random() for _ in range(n)])
