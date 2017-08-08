import sys

if (len(sys.argv) > 2):
    print " Please don't be ridiculous. This script can only handle one file at a time."
    exit()

import numpy as np
import matplotlib as plt
import pandas as pd
from pylab import *
import scipy

#file = sys.argv[1]
models = pd.read_csv('/home/kuehnna/gitrepos/python_assessment/sorted_models.txt', sep=' ', names=['model', 'total_score', 'interface_delta_X'])
x = models['total_score']
y = models['interface_delta_X']

# I am not fully aware of how or why the following code works. I found it online and modified it to suit my data. I just thought it was pretty cool given the high density of the dots in the bottom-left area.
# (The comments after this point are also not mine, but I copied them along with the code to make it more understandable for me.)

#histogram definition
xyrange = [[-1200,-700],[-50,200]] # data range
bins = [200,200] # number of bins
thresh = 15 #density threshold

#data definition
xdat, ydat = x, y

# histogram the data
hh, locx, locy = scipy.histogram2d(xdat, ydat, range=xyrange, bins=bins)
posx = np.digitize(xdat, locx)
posy = np.digitize(ydat, locy)

#select points within the histogram
ind = (posx > 0) & (posx <= bins[0]) & (posy > 0) & (posy <= bins[1])
hhsub = hh[posx[ind] - 1, posy[ind] - 1] # values of the histogram where the points are
xdat1 = xdat[ind][hhsub < thresh] # low density points
ydat1 = ydat[ind][hhsub < thresh]
hh[hh < thresh] = np.nan # fill the areas with low density by NaNs

plt.figure(figsize=[16,9])
plot1 = plt.imshow(np.flipud(hh.T),cmap='jet',extent=np.array(xyrange).flatten(), interpolation='none', origin='upper')
plot2 = plt.colorbar()   
plot3 = plt.scatter(xdat1, ydat1, marker='.', s=2, color='darkblue')
plt.show()
