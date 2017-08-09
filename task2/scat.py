'''
Created on Aug 8, 2017

@author: kuehnna
'''

import sys
if (len(sys.argv) > 2): 
  print "Please only use one file at a time."
  exit()



if (len(sys.argv) < 2):
  file = raw_input("Please provide a sorted_models file:")
else:
  file = sys.argv[1] 


import matplotlib as plt
import pandas as pd
from pylab import *

#Define maximum total_score and maximum interface_delta_X
maxtot = float(raw_input("Please enter maximum total_score: "))
maxinter = float(raw_input("Please enter maximum interface_delta_X: "))



models_raw = pd.read_csv(file, sep=' ', names=['model', 'total_score', 'interface_delta_X'])
#This is where to go on



x = models['total_score']
y = models['interface_delta_X']

plt.figure()
plot1 = plt.scatter(x,y, s=2, c='Green', marker='.')
plt.rcParams["figure.figsize"]= [16, 9]
plt.show()





