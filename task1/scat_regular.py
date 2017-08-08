
# coding: utf-8
import sys
if (len(sys.argv) > 2): 
  print "Please contain your enthusiasm and use no more than one file at a time."
  exit()



import numpy as np
import matplotlib as plt
import pandas as pd
from pylab import *


file = sys.argv[1]
models = pd.read_csv(file, sep=' ', names=['model', 'total_score', 'interface_delta_X'])
x = models['total_score']
y = models['interface_delta_X']

plt.figure()
plot1 = plt.scatter(x,y, s=2, c='Green', marker='.')
plt.rcParams["figure.figsize"]= [16, 9]
plt.show()





