'''
Created on Nov 17, 2010

@author: mendenjl
'''

import os
import sys
import os.path

"""
function to print out prompt
"""
def usage():
  print("SplitFileAfter.py input-file output_file ids")
  sys.exit(1)

"""
main function
"""
def main():
  arguments = sys.argv[1::1]
  
  # check the number of parameter  
  if len(arguments) < 3:
    usage()
  """
  Include i the rest of your code here
  """

"""
run main function
"""
if __name__ == '__main__':
    main()
