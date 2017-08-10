
# coding: utf-8

# In[ ]:

import sys
import matplotlib as plt
import pandas as pd
from pylab import *

#Checks if there are too many command-line arguments and tells the user to not use too many if there are.
def argumnumber():
    if (len(sys.argv) > 2):
        print "Please only use one file with this this script. For specifying additional parameters, please wait until prompted to do so."
        quit()

#Prompts user to enter max values for rmsd and interface_delta_X
def maxprompt():
    global rmsdlim
    rmsdlim = float(raw_input("Please enter max value for rmsd: "))
    global interlim
    interlim = float(raw_input("Please enter max value for interface_delta_X: "))


#Imports data file. If none is given hrough command-line, user gets prompt to enter one.
def loadfile():
    global file
    if (len(sys.argv) < 2):
        file = raw_input('Please provide a rmsd_score_ligand file: ')
    else:
        file = sys.argv[1]
    #global data_raw
    data_raw = pd.read_csv(file, delim_whitespace=True,header=0, usecols=['total_score','ligand_rms_no_super_X','interface_delta_X'], skiprows=[0])
    global data
    data = data_raw.loc[(data_raw['ligand_rms_no_super_X'] <= rmsdlim) & (data_raw['interface_delta_X'] <= interlim)]

#Divides data into upper and lower half (if a value equals the average, it is part of lower half)
def divide():
    global avgtot
    avgtot = (sum(data['total_score']) / (len(data['total_score'])))
    global datlo
    datlo = data.loc[data['total_score'] <= avgtot]
    global dathi
    dathi = data.loc[data['total_score'] > avgtot]




#Makes the graph.
def graph():
    #Sets some values.
    x1 = datlo['ligand_rms_no_super_X']
    y1 = datlo['interface_delta_X']
    x2 = dathi['ligand_rms_no_super_X']
    y2 = dathi['interface_delta_X']
    #Calls actual max values for ligand_rms_no_super_X and interface_delta_X
    maxrmsd = data['ligand_rms_no_super_X'].max()
    minrmsd = data['ligand_rms_no_super_X'].min()
    maxint = data['interface_delta_X'].max()
    minint = data['interface_delta_X'].min()
    #Following lines define everything about the actual figure
    plt.figure(figsize=[16,9])
    plt.xlim(xmin = minrmsd, xmax = maxrmsd)
    plt.ylim(ymin = minint, ymax = maxint)
    plot1 = plt.scatter(x1,y1, s=4, c='Blue', marker='o')
    plot2 = plt.scatter(x2,y2, s=4, c='Red', marker='o')
    plt.tick_params(axis='both',direction='inout',width=1,length=6,labelsize=13,pad=4)
    plt.title('interface_delta_x vs ligand_rms_no_super_X', size=16)
    plt.xlabel("ligand_rms_no_super_X", fontsize=13)
    plt.ylabel("interface_delta_X", fontsize=13)
    plt.legend(['total_score <= average', 'total_score > average'], markerscale=5, fontsize=12)
    #Prompts user to decide on whether to export png file
    printfile()
    #Displays plot
    plt.show()
    
#Lets user decide whether to print to a file (y gives automatic parameter-based filename, otherwise users can enter their own filename)
def printfile():
    expfile = raw_input("Do you want to save the figure as a .png file? Enter [y/n] or specify filename: ")
    if (expfile == 'y'):
        expname = 'scat_maxrmsd_' + str(rmsdlim) + '_maxinter_' + str(interlim) + '.png'
        plt.savefig(expname,format='png')
    elif (expfile != 'n'):
        plt.savefig(expfile, format='png')
        

    
#Main function does nothing but call other functions.
def main():
    #Firstly, checks whether there are too many command-line arguments. Quits if there are, otherwise continues.
    argumnumber()
    #Secondly, prompts user for max values
    maxprompt()
    #Loads data file (including prompt if none is defined yet). Filters out values over set max values.
    loadfile()
    #Divides dataframe into upper and lower as defined by the average total_score.
    divide()
    #Creates the graph. Includes a prompt that enables user to export figure as png
    graph()


#Executes main function
if __name__ == '__main__':
    main()
    
    
    

