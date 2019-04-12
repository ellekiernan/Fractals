import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

mandolin = np.loadtxt('mandolin_2560x1600.txt')

Image.fromarray(mandolin).show()