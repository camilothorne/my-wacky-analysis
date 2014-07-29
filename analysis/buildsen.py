'''
Created on Jul 29, 2014
@author: camilothorne
'''

# class to open big files
class OpenFile:


    # constructor
    def __init__(self,filename):

        self.file = filename
        self.lines = None


    # load file in huge list    
    def open(self):
        
        bigfile = open(self.filename, 'r')
        try:
            self.lines = bigfile.read()
        finally:
            bigfile.close()


    # free memory
    def destroy(self):
        self.lines = None