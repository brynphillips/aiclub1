#Copy a file from one local to another.

import os
import os.path
from os import path


filename = input("What file would you like to copy?\n")

def copy(filename):
    print(filename)
    if path.isfile(filename + '.txt') == False:
        filename = input("This file does not exist, enter another filename please.\n")
        # copy(filename)
    # else:
        # copy('filename'+'txt')    

copy(filename)




# print(filename)