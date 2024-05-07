# gameplay.py
# Aidan Nachi
# 2024.06.05
# 
# This file defines a win finder class that finds the best poker
# hand in a five-card draw.


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import itertools
from collections import defaultdict



# Numpy Seed for generating random numbers
np.random.seed(0)