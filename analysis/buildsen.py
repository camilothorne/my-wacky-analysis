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
        self.bigfile = open(filename, 'r')


#     # load file in huge list    
#     def myopen(self):
#         
# #        bigfile = open(self.filename, 'r')
#         try:
#             self.lines = self.myread(self.bigfile)
#         except:
#             print 'error'
#             while tmp_lines:
#                 tmp_lines = bigfile.readlines(10000)
#             self.lines = self.read(bigfile)
#         finally:
#             bigfile.close()
            
        
    # close file
    def myclose(self):
        
            self.bigfile.close()
            self.destroy()
    

    # buffered reading of file
    def myread(self):
        
            lines = []
            try:
                lines = self.bigfile.readlines(100000)
            except:
                print 'error'
            return lines
            
            
    # free memory buffer
    def destroy(self):
        self.lines = None
        
        
####################################################################


# Class to generate sentences
class MySen:
    
    
        #begin : begin of sentence?
        #end    : end of sentence?
        #sen     : current sentence
        
        
        # init to false, empty sentence      
        def __init__(self):
            self.sen      = ""
            self.begin  = False
            self.end     = False
            self.len      = 0
            
            
        # build a sentence
        def buildSen(self,i,lines):
            
                #print line
                tokens = lines[i].split()
                #print tokens
                                
                if tokens[0] == '<s>':
                    self.begin = True
                    posi = i+1
                    #print 'pos ', i
                    #print 'curr len ', len
                    tokens = lines[posi].split()
                    #while not(tokens[0] == '</s>'):
                    while not(lines[posi+1].split()[0] == '</s>'):
                        posi = posi + 1
                        tokens = lines[posi].split()
                        #print 'up len ', len
                        #print tokens
                        self.sen = self.sen + tokens[0]+ '\\' + tokens[2] + ' '
                    self.len = posi - (i+1)
                    self.end = True
                
                self.sen = self.sen.lower()
                #print self.sen + '\n'
                #print self.len
        
        
        # reset object
        def reset(self):
            self.sen      = ""
            self.end     = False
            self.begin  = False
            self.len       = 0   