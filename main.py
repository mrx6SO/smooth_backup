# -*- coding: utf-8 -*-

"""

   smooth_backup
   
   coder: mrx6SO
   
   https://github.com/mrx6SO
   
   @2019
   
"""

import os
import sys
import re
import shutil
import time


# function to find the files

# função para encontrar os arquivos

def find_files(pattern, path):

    for path, dirs, files in os.walk(path):

        for filename in files:

            full_file_name = os.path.join(path, filename)
            
            match = re.match(pattern, full_file_name)

            if(match):

                yield full_file_name


#function that copy matched files for the destination path / pendrive / email

# função responsável pela cópia dos arquivos compatíveis para pasta / pendrive/ email selecionados

def copy_files(pattern, src_path, dest_path):

    """
        function receive 3 arguments:
        
        - pattern of files : '.'
        - src_path = 'source path', where files are located
        - dest_path = 'destination path', where the files will be copied
        
    """

    for full_file_name in find_files(pattern,src_path):

        print(full_file_name) + ' file was copied into ' + (dest_path)

        try:
           
            shutil.copy(full_file_name, dest_path)

        except IOError:

            return

if __name__ == "__main__":
   
    while True:

        try:
           
            patt = '.' #the pattern
           
            if(os.name == 'nt'): # if system is Windows based

                """

                   select the source to do the copy
                   select destination path that will receive the previously copyed files

                   :    the pattern is '.' cause it gets all the extensions
                        if is needed set up one or many different extension
                   :    just modify the part of code that handle with it

                """  

                print('source path must be, for ex. | C:\\Users | with 2 slashs.')
                src = raw_input('Source path: ')
                dst = raw_input('Destination path: ')
             
                copy_files(patt, src, dst)
                time.sleep(2)

            elif(os.name == 'posix'):
                
                srce = raw_input('Source path: ')
                destin = raw_input('Destination path: ')

                copy_files(patt, srce, destin)
                time.sleep(2)

            else:

                print('\nError ocurred...\n')
                                              
        except KeyboardInterrupt:

            print('\nExiting...\n')

            sys.exit(0)
