'''
Created on Nov 10, 2014
@author: camilothorne
'''

#===================#
#===================#
#
# Class likelihoods
#
#   (by Q class)
# 
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

ss10 = " someone/nn"
ss12 = " somebody/nn"
ss12a = " anybody/nn"
ss14 = " something/nn"
ss16 = " some/dt"
ss18 = " a/dt"
ss20 = " many/dt "
ss20a = " many/jj */nns"
ss22 = " there/ex"

####################################################################

# 4. all

ss40 = " every/dt "
ss42 = " all/dt "
ss44 = " the/dt .*/nns "
ss46 = " everything/nn "
ss48 = " everyone/nn " 
ss4a = " everybody/nn " 
ss4c = " each/dt "
ss4e = " no/dt "

####################################################################

# 8.1 exactly one

ss74 = " the/dt "

####################################################################
####################################################################

# 6. at most k, less than k (k integer)

ss60 = " at/in most/jjs .*/cd "
ss20b = " less/jjr than/in .*/cd "
ss20bb = " fewer/jjr than/in .*/at .*/cd "
ss22b = " less/jjr than/in .*/at .*/cd "
ss22bb = " fewer/jjr than/in .*/at .*/cd "

####################################################################

# 7. at least k, more than k (k integer)

ss60b = " at/in least/jjs .*/cd "
ss20 = " more/jjr than/in .*/cd "
ss22 = " more/jjr than/in .*/at .*/cd "

####################################################################

# 8. exactly k (k integer)

ss70 = " .*/cd .*/nns "
ss71 = " exactly/rb .*/cd "

####################################################################
####################################################################

# 9. more than p/k (p, k integers)

ss80 = " more/ap than/in half/abn "
ss82 = " more/ap than/in .*/cd .*/od "

####################################################################

# 9.1 less than p/k (p, k integers)

ss80b = " less/jjr than/in half/nn "
ss80bb = " fewer/jjr than/in half/nn "
ss82b = " less/jjr than/in .*/nns of/in "
ss82bb = " fewer/jjr than/in .*/nn of/in "

####################################################################

# 9.2 p/k (p, k integers)

ss80c = " half/dt "
ss80d = " half/pdt "
ss80c = " half/nn of/in"
ss81c = "   .*/nns of/in "
ss81d = "  .*/nn of/in "

####################################################################

# 3. more than k% (k a percentage)

ss30 = " more/jjr than/in .*/cd percent/nn "
ss30a = " more/jjr than/in %/cd "

####################################################################

# 3.1 less than k% (k a percentage)

ss30b = " less/jjr than/in .*/cd percent/nn "
ss30bb = " less/jjr than/in %/cd "

####################################################################

# 3.2 k% (k a percentage)

ss30c = " ./cd percent/nn "
ss30d = " %/cd "

####################################################################

# 5. most, more than half

ss51 = " most/jjs "
ss51a = " most/dt "
ss53 = " more/jjr than/in half/nn "

####################################################################

# 5.1 few, less than half, fewer than half

ss51b = " few/jj "
ss51bb = " few/jj "
ss53b = " less/jj than/in half/nn "
ss53bb = " fewer/jj than/in half/nn "


####################################################################
####################################################################
# B. superclasses
####################################################################
####################################################################


aristotelian = [ss10,ss12,ss12a,ss14,ss16,ss18,ss20,ss20a,ss22,
                ss40,ss42,ss44,ss46,ss48,ss4a,ss4c,ss4e,
                ss74]

proportional = [ss51b,ss51bb,ss53b,ss53bb,
                ss51,ss51a,ss53,
                ss30c,ss30d,
                ss30b,ss30bb,
                ss30,ss30a,
                ss80c,ss80d,
                ss80b,ss80bb,ss82b,ss82bb,
                ss80,ss82]
                
counting  = [ss70,ss71,
                ss20,ss22,ss60b,
                ss20b,ss22b,ss20bb,ss22bb]


####################################################################
####################################################################


# Class encoding the plot(s) + test(s)


class ProporStatsCum:
   
    
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
        figname = "Base GQs  (by class)"
        figpath = plotting +'/'+ figname.replace(' ', '-') + '-stats.pdf'
        savpath = plotting +'/'+ figname.replace(' ', '-')
        
        # plotting
        MyPlot(self.stats,self.classstats,figname, "three",plotting,list) # per class (no regression)
        
        # generating report
        SaveStats(self.classstats,self.stats,figpath,savpath,plotting) # per class
        
        
    #############################################################
    #############################################################        
 
            
    # creating the classes
    def fileStats(self,path,fileids):
                
        # starting the title
        tit = "Base GQs (by class)"
        
        # stat classes
        C1 = MyClassStats2("ari",[],0,tit)
        C2 = MyClassStats2("cnt",[],0,tit)
        C3 = MyClassStats2("pro",[],0,tit)

        self.classstats = [C1,C2,C3]     
        
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
                        # class 1
                        c1.openSen(myline,c1.pats,c1.patts)
                        ####################################################################
                        # class 2    
                        c2.openSen(myline,c2.pats,c2.patts)
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


