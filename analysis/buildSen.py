'''
Created on Jul 29, 2014
@author: camilothorne
'''

class openFile:


    def __init__(self,filename):

        self.file = filename
        self.lines = None

    
    def open(self):
        
        bigfile = open(self.filename, 'r')
        try:
            self.lines = bigfile.read()
        finally:
            bigfile.close()
        