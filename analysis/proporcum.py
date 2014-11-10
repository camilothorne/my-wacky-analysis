'''
Created on Nov 10, 2014
@author: camilothorne
'''

#===================#
#===================#
#                                            #
# Class likelihoods              #
#                                             #
#===================#
#===================#


# python
from __future__ import division
from operator import attrgetter
#from math import ceil


# my plotting + test classes
from corpuspkg.statsplot import MyPlot
from corpuspkg.statstests import STest


# nltk
from nltk.corpus import PlaintextCorpusReader


# my classes
from analysis.proporclasses import MyClass2, MyPatts2, MyClassStats2
from analysis.savestats import SaveStats
from analysis.buildsen import *


####################################################################
#################################################################### 

s0 = ".*"        # anything!

####################################################################
####################################################################
# A. simple classes
####################################################################
####################################################################

# 1. exists

s10 = " someone/nn"
s12 = " somebody/nn"
s12a = " anybody/nn"
s14 = " something/nn"
s16 = " some/dt"
s18 = " a/dt"
s20 = " many/dt "
s20a = " many/jj */nns"
s22 = " there/ex"

####################################################################

# 4. all

s40 = " every/dt "
s42 = " all/dt "
s44 = " the/dt .*/nns "
s46 = " everything/nn "
s48 = " everyone/nn " 
s4a = " everybody/nn " 
s4c = " each/dt "
s4e = " no/dt "

####################################################################

# 8.1 exactly one

s74 = " the/dt "

####################################################################
####################################################################

# 6. at most k, less than k (k integer)

s60 = " at/in most/jjs .*/cd "
s20b = " less/jjr than/in .*/cd "
s20bb = " fewer/jjr than/in .*/at .*/cd "
s22b = " less/jjr than/in .*/at .*/cd "
s22bb = " fewer/jjr than/in .*/at .*/cd "

####################################################################

# 7. at least k, more than k (k integer)

s60b = " at/in least/jjs .*/cd "
s20 = " more/jjr than/in .*/cd "
s22 = " more/jjr than/in .*/at .*/cd "

####################################################################

# 8. exactly k (k integer)

s70 = " .*/cd .*/nns "
s71 = " exactly/rb .*/cd "

####################################################################
####################################################################

# 9. more than p/k (p, k integers)

s80 = " more/ap than/in half/abn "
s82 = " more/ap than/in .*/cd .*/od "

####################################################################

# 9.1 less than p/k (p, k integers)

s80b = " less/jjr than/in half/nn "
s80bb = " fewer/jjr than/in half/nn "
s82b = " less/jjr than/in .*/nns of/in "
s82bb = " fewer/jjr than/in .*/nn of/in "

####################################################################

# 9.2 p/k (p, k integers)

s80c = " half/dt "
s80d = " half/pdt "
s80c = " half/nn of/in"
s81c = "   .*/nns of/in "
s81d = "  .*/nn of/in "

####################################################################

# 3. more than k% (k a percentage)

s30 = " more/jjr than/in .*/cd percent/nn "
s30a = " more/jjr than/in %/cd "

####################################################################

# 3.1 less than k% (k a percentage)

s30b = " less/jjr than/in .*/cd percent/nn "
s30bb = " less/jjr than/in %/cd "

####################################################################

# 3.2 k% (k a percentage)

s30c = " ./cd percent/nn "
s30d = " %/cd "

####################################################################

# 5. most, more than half

s51 = " most/jjs "
s51a = " most/dt "
s53 = " more/jjr than/in half/nn "

####################################################################

# 5.1 few, less than half, fewer than half

s51b = " few/jj "
s51bb = " few/jj "
s53b = " less/jj than/in half/nn "
s53bb = " fewer/jj than/in half/nn "


####################################################################
####################################################################
# B. superclasses
####################################################################
####################################################################


aristotelian = [s10,s12,s12a,s14,s16,s18,s20,s20a,s22,
                s40,s42,s44,s46,s48,s4a,s4c,s4e,
                s74]

proportional = [s51b,s51bb,s53b,s53bb,
                s51,s51a,s53,
                s30c,s30d,
                s30b,s30bb,
                s30,s30a,
                s80c,s80d,
                s80b,s80bb,s82b,s82bb,
                s80,s82]
                
counting   = [s70,s71,
                s20,s22,s60b,
                s20b,s22b,s20bb,s22bb]


####################################################################
####################################################################


# Class encoding the plot(s) + test(s)


class ProporStats:
   
    
    # corpus            : path to corpora
    # format            : format of corpora (e.g. .txt files)
    # stats             : hash table with class stats of each corpus
    # classstats        : list with global stats (mean frequency) 
    # list              : list of legends in figure
    # plotting          : directory of compiled report

    
    # object constructor
    def __init__(self,path,myformat,mylist,plotting):
        self.stats = {} # stats
        self.classstats = [] # classes
        self.path = path # path of corpus
        self.format = myformat # format of file(s)
        self.occStats(path,myformat,list,plotting) # collects stats + plots them
        self.statTestB(self.classstats) # runs the stat tests
        self.list = mylist
        self.plotting = plotting    

    
    #############################################################
    #############################################################
        
    
    # collecting statistics
    def occStats(self,path,format,list,plotting):
        wordlists = PlaintextCorpusReader(path,format)
        fileids = wordlists.fileids()
        k = len(fileids)
        
        # computing rel frequencies
        self.fileStats(path,fileids)
        
        # plotting vars
        figname = "Base GQs"
        figpath = plotting +'/'+ figname.replace(' ', '-') + '-stats.pdf'
        savpath = plotting +'/'+ figname.replace(' ', '-')
        
        # plotting
        MyPlot(self.stats,self.classstats,figname, "three",plotting,list) # all
        
        # generating report
        SaveStats(self.classstats,self.stats,figpath,savpath,plotting) # all
        
        
    #############################################################
    #############################################################        
 
            
    # creating the classes
    def fileStats(self,path,fileids):
                
        # starting the title
        tit = "Base GQs"
        
        # stat classes
        C1 = MyClassStats2("ari",[],0,tit)
        C2 = MyClassStats2("cnt",[],0,tit)
        C3 = MyClassStats2("pro",[],0,tit)

        self.classstatsCum = [C1,C2,C3]     
        
        print "###################################################"
        print "GQ STATS (by class)"
        print "###################################################"
        
        # computing the stats
        for idf in fileids:
                        
            ####################################################################
            
            filestats = []
            mydata = OpenFile(path+'/'+idf)
            mydata.lines = mydata.myread()
            
            ####################################################################
            
            #print "==================================================="
            print idf
            print "==================================================="
            
            ####################################################################
 
            # patterns
            rest = []  
            
            # corpus
            corpus = MyClass2([".*"],[],idf,0,0,"corpus")
            
            ####################################################################  
            
            # class 1
            P1 = MyPatts2(aristotelian).P
            N1 = MyPatts2(rest).P
            c1 = MyClass2(P1,N1,idf,0,0,"ari")
            
            # class 2
            P2 = MyPatts2(counting).P
            N2 = MyPatts2(rest).P           
            c2 = MyClass2(P2,N2,idf,0,0,"cnt")           
                
            # class 3
            P3 = MyPatts2(proportional).P
            N3 = MyPatts2(rest).P
            c3 = MyClass2(P3,N3,idf,0,0,"pro")                                 
            
            ####################################################################  
            ####################################################################            
            
            # examine only k chunks of the big file at a time
            while mydata.lines:
                
                i = 0
                my_max = len(mydata.lines)
                
                # loop over chunk
                while i  <  my_max:
            
                    # parse the chunk
                    lines = mydata.lines
                    line = mydata.lines[i]
                    
                    # build sentence            
                    sen = MySen()
                    sen.buildSen(i,lines,my_max)
                
                    # if sentence built, apply patterns       
                    if sen.end == True:
                        
                        # retrieve POS tagged sentence
                        myline = sen.sen
            
                        ####################################################################           
                    
                        # corpus
                        corpus.openSen(myline,corpus.pats,corpus.patts)        
                    
                        ####################################################################
                        ####################################################################            
                        
                        # class 1
                        c1.openSen(myline,c1.pats,c1.patts)
                        
                        ####################################################################
                        
                        # class 2    
                        c2.openSen(myline,c2.pats,c2.patts)
                        
                        ####################################################################
                        ####################################################################
             
                        # class 3 
                        c3.openSen(myline,c3.pats,c3.patts)    
                                    
                        ####################################################################
                    
                    # if a sentence is found, skip the lines it
                    # covers in the loop, otherwise move to the
                    # next line
                    if sen.len > 0:
                        i = i + sen.len
                        # print 'senlen=', sen.len, '\n'
                        print 'sen= ', sen.sen, '\n'
                    else:    
                        i = i + 1
                    # print 'explore at line= ', i, '\n'
                
                # move to new chunk
                mydata.lines = mydata.myread()
            
            ####################################################################
            ####################################################################
                       
            # total cum count
            tot = (c1.count + c2.count + c3.count) + 1
    
            print "corpus size : " + `corpus.count` + " sentences"        
            print "==================================================="
            print "total matches: " + `tot` + " GQs"
            
            #relative frequencies
            c1.freq  = round(c1.count/tot,2)
            c2.freq  = round(c2.count/tot,2)
            c3.freq  = round(c3.count/tot,2)
            
            ####################################################################            
            
            filestats = [c1,c2,c3]
            
            ####################################################################  
            
            self.stats[idf] = filestats
            
            ####################################################################  
            
            for cla in self.classstats:
                for thiscls in filestats:
                    if (thiscls.tag == cla.tag):
                        cla.classes.append(thiscls)

            ####################################################################  
                                
        # updating the distribution 
        self.classAvg(self.classstats)
        self.classAvg2(self.classstats)
        sort = self.sortClass(self.classstats)
        self.classstats = sort
        print "###################################################"
        self.printClasses(self.classstats)
    

    ############################################################# 
    #############################################################     
        
                
    # sorts stats classes
    def sortClass(self,classlist):
        sort = sorted(classlist,key=attrgetter('avg'))
        return sort
    
    
    # computes list of averages    
    def classAvg(self,classstats):
        for cla in classstats:
            meanj = 0
            for idf in cla.classes:
                meanj = meanj + idf.freq
            meanj = (meanj/len(cla.classes))
            cla.avg = meanj
            
            
    # computes list of frequencies    
    def classAvg2(self,classstats):
        for cla in classstats:
            meanf = 0
            for idf in cla.classes:
                meanf = meanf + idf.count
            meanf = (meanf/len(cla.classes))
            cla.fre = meanf
    
    
    #############################################################
    #############################################################
    
        
    # prints the stats
    def printClasses(self,classstats):
        for cla in classstats:
            print cla.tag
            print "---------------------------------------------------"            
            print `cla.avg` + ": avg rel. freq"
            print "---------------------------------------------------"
            for idf in cla.classes:
                print `idf.freq` + ": rel. freq "+ idf.fileid
                print `idf.count` + ": freq "+ idf.fileid              
            print "###################################################"


    #############################################################
    #############################################################

        
    # statistical tests
    def statTestB(self,classstats):
        
        s = STest()
           
        # simple samples:   
             
        # freqs (cross corpus, per corpus)     
        sample1 = [] 
        for cla in classstats:
            sample1.append(sum([cl.count for cl in cla.classes]))
                                
        # rel. freqs (cross-corpus, per class)
        sample2 = []
        for cla in classstats:
            sample2.append(round(cla.avg,2))                
            
        # simple stats methods
        print "###################################################"        
        print "Simple statistical tests:"
        print "---------------------------------------------------"
        print "sam1 = ", sample1,"(GQ freqs per class)"
        print "sam2 = ", sample2,"(GQ rel freqs per class)"  
        ##########################################################
        s.mySkew(sample1)                       # skewness     
        s.myEntropy(sample2)                    # entropy
        s.myChiTest(sample1,s.uniFor(sample1))  # X^2 test   


