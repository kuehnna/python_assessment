'''
Created on Aug 9, 2017

@author: kuehnna
'''


import sys
import matplotlib as plt
import pandas as pd
from pylab import *


#Checks number of command-line arguments and provides appropriate reaction
def argumnumber():
  if (len(sys.argv) > 2): 
    print "Please only use one file at a time. If you were trying to provide max values as commandline arguments, please rerun without those and wait until prompted to enter them."
    exit()

#Lets user decide whether or not to print plot to a file (before displaying it) and lets user either pick their own filename or get an automatically generated one.
def printtofile():
  expfile = raw_input("Do you want to export figure as .png? Enter [y/n] or enter a filename: ")
  if (expfile == 'y'):
    expname = 'scat_' + 'maxtot_' + str(maxtot) + '_maxinter_' + str(maxinter) + '.png'
    plt.savefig(expname,format='png')
  elif (expfile != 'n'):
    plt.savefig(expfile,format='png')

def main():
  #Before anything happens, number of command-line arguments is checked and appropriate action taken.
  argumnumber()
  if (len(sys.argv) < 2):
    file = raw_input("Please provide a sorted_models file: ")
  else:
    file = sys.argv[1] 
  #Prompts user to provide maxtot and maxinter before progam continues.
  global maxtot
  maxtot = float(raw_input("Please enter maximum total_score: "))
  global maxinter
  maxinter = float(raw_input("Please enter maximum interface_delta_X: "))

  #Imports DataFrame and filters based on max values provided.
  models_raw = pd.read_csv(file,sep=' ', names=['model', 'total_score', 'interface_delta_X'])
  models = models_raw.loc[(models_raw['total_score'] <= maxtot) & (models_raw['interface_delta_X'] <= maxinter)]
  #Creates the plot.
  x = models['total_score']
  y = models['interface_delta_X']
  plt.figure(figsize=[16,9])
  plot1 = plt.scatter(x,y, s=2, c='Green', marker='.')
  plt.tick_params(axis='both',direction='inout',width=1,length=6,labelsize=13,pad=4)
  plt.title('interface_delta_x vs total_score', size=16)
  plt.xlabel("total_score", fontsize=13)
  plt.ylabel("interface_delta_X", fontsize=13)
  printtofile()
  plt.show()

'''
Runs main function
'''

if __name__ == '__main__':
    main()



