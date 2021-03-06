'''
Created on Nov 14, 2014
@author: camilo
'''

#===================#
#===================#
#
# Class likelihoods
#   (ENG + DEU)
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
from proporclasses import MyClass2, MyPatts2, MyClassStats2
from savestats import SaveStats
from buildsen import *


####################################################################
#################################################################### 

s0 = ".*"        # anything!

####################################################################
####################################################################
# A. simple classes
####################################################################
####################################################################

# exists

s10 = " someone/nn"
s12 = " somebody/nn"
s12a = " anybody/nn"
s14 = " something/nn"
s16 = " some/dt"
# s18 = " a/dt"
s20 = " many/dt "
s21 = " many/jj */nns"
# s22 = " there/ex"

ds10 = " pis/jemand "
ds14 = " pis/etwas "
ds15 = " piat/etwas "
# ds16 = " ne/irgendetwas "
# ds17 = " art/ein "
# ds18 = " pper/es vvfnn/gibt "
ds20 = " pis/manch "
ds21 = " piat/manch "
ds22 = " piat/viel "

some = [s10,s12,s12a,s14,s16,s20,s21,
        ds10,ds14,ds15,ds20,ds21,ds22]

####################################################################

# all

s40 = " every/dt "
s42 = " all/dt "
# s44 = " the/dt .*/nns "
s46 = " everything/nn "
s48 = " everyone/nn " 
s4a = " everybody/nn " 
s4c = " each/dt "
s4e = " no/dt "

ds40 = " piat/alle "
ds41 = " pis/alle "
ds42 = " piat/kein "
ds46 = " piat/jed "

aall = [s40,s42,s46,s48,s4a,s4c,s4e,
       ds40,ds41,ds42,ds46]

####################################################################

# # exactly one
# 
# s74 = " the/dt "
# 
# ds74 = " art/d "
# 
# the = [s74,
#        ds74]

####################################################################
####################################################################

# at most k, less than k (k integer)

s60 = " at/in most/jjs .*/cd "
s20b = " less/jjr than/in .*/cd "
s20bb = " fewer/jjr than/in .*/at .*/cd "
s22b = " less/jjr than/in .*/at .*/cd "
s22bb = " fewer/jjr than/in .*/at .*/cd "

ds60 = " adv/h\p{L}chstens card/@card@ "
ds20b = " piat/weniger kokom/als card/@card@ "

lessk = [s20b,s22b,s20bb,s22bb,
         ds60,ds20b]

####################################################################

# at least k, more than k (k integer)

s60b = " at/in least/jjs .*/cd "
s20 = " more/jjr than/in .*/cd "
s22 = " more/jjr than/in .*/at .*/cd "

ds60b = " adv/mindestens card/@card@ "
ds20 = " piat/mehr kokom/als card/@card@ "

morek = [s20,s22,s60b,
         ds60b,ds20]

####################################################################

# exactly k (k integer)

s70 = " .*/cd .*/nns "
s71 = " exactly/rb .*/cd "

ds70 = " card/@card@ nn/.* "

exactlyk = [s70,s71,
            ds70]

####################################################################
####################################################################

# more than p/k (p, k integers)

s80 = " more/ap than/in half/abn "
s82 = " more/ap than/in .*/cd of/in "

ds80 = " piat/mehr kokom/als adjd/halb "
ds80a = " piat/mehr kokom/als card/@card@ appr/von"

morethanpro = [s80,s82,
               ds80,ds80a]

####################################################################

# less than p/k (p, k integers)

s80b = " less/jjr than/in half/nn "
s80bb = " fewer/jjr than/in half/nn "
s82b = " less/jjr than/in .*/cd of/in "
s82bb = " fewer/jjr than/in .*/cd of/in "

ds80b = " piat/weniger kokom/als adjd/halb "
ds80bb = " piat/weniger kokom/als card/@card@ appr/von "

lessthanpro = [s80b,s80bb,s82b,s82bb,
               ds80b,ds80bb]

####################################################################

# p/k (p, k integers)

s80c = " half/dt "
s80d = " half/pdt "
s80c = " half/nn of/in"
s81c = " .*/nns of/in "
s81d = " .*/nn of/in "

ds80c = " adja/halb "
ds80d = " adja/halb appr/von "
ds80e = " card/@card@ appr/von "

pro = [s80c,s80d,
       ds80c,ds80d,ds80e]

####################################################################

# more than k% (k a percentage)

s30 = " more/jjr than/in .*/cd percent/nn "
s30a = " more/jjr than/in %/cd "

ds30a = " piat/mehr kokom/als card/@card@ nn/% "

morekper = [s30,s30a,
            ds30a]

####################################################################

# less than k% (k a percentage)

s30b = " less/jjr than/in .*/cd percent/nn "
s30bb = " less/jjr than/in %/cd "

ds30bb = " piat/weniger kokom/als card/@card@ nn/% "

lesskper = [s30b,s30bb,
            ds30bb]

####################################################################

# k% (k a percentage)

s30c = " ./cd percent/nn "
s30d = " %/cd "

ds30d = " nn/% "

kper = [s30c,s30d,ds30d,
        ds30d]

####################################################################

# most, more than half

s51 = " most/jjs "
s51a = " most/dt "
s53 = " more/jjr than/in half/nn "

ds51 = " adv/fast piat/jed "
ds51a = " piat/mehr kokom/als adjd/halb "

most = [s51,s51a,s53,
        ds51,ds51a]

####################################################################

# few, less than half, fewer than half

s51b = " few/jj "
s51bb = " few/dt "
s53b = " less/jj than/in half/nn "
s53bb = " fewer/jj than/in half/nn "

ds51b = " piat/wenig "
ds53b = " piat/wenig kokom/als adjd/halb "

few = [s51b,s51bb,s53b,s53bb,
       ds51b,ds53b]


####################################################################
####################################################################


# Class encoding the plot(s) + test(s)


class ProporStatsF:
   
    
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
        self.list = mylist        
        self.occStats(path,myformat,self.list,plotting) # collects stats + plots them
        self.statTestB(self.classstats) # runs the stat tests
        self.plotting = plotting    

    
    #############################################################
    #############################################################
        
    
    # collecting statistics
    def occStats(self,path,formatt,llist,plotting):
        wordlists = PlaintextCorpusReader(path,formatt)
        fileids = wordlists.fileids()
        #k = len(fileids)
        
        # computing rel frequencies
        self.fileStats(path,fileids)
        
        # plotting vars
        figname = "Base GQs"
        figpath = plotting +'/'+ figname.replace(' ', '-') + '-stats.pdf'
        savpath = plotting +'/'+ figname.replace(' ', '-')
        
        # plotting
        MyPlot(self.stats,self.classstats,figname, "one",plotting,llist) # all
        
        # generating report
        SaveStats(self.classstats,self.stats,figpath,savpath,plotting) # all
        
        
    #############################################################
    #############################################################        
 
            
    # creating the classes
    def fileStats(self,path,fileids):
                
        # starting the title
        tit = "GQs"
        
        # stat classes
        
        C1  =   MyClassStats2("all",[],0,tit)
        C2  =   MyClassStats2("some",[],0,tit)
        
        C4 =    MyClassStats2(">k",[],0,tit)
        C5 =    MyClassStats2("<k",[],0,tit)
        C6 =    MyClassStats2("k",[],0,tit)
        
        C7 =    MyClassStats2("most",[],0,tit)
        C8 =    MyClassStats2("few",[],0,tit)
        C9 =    MyClassStats2(">p/k",[],0,tit)             
        C10 =   MyClassStats2("<p/k",[],0,tit)
        C13 =   MyClassStats2("p/k",[],0,tit)
        C11 =   MyClassStats2(">k/100",[],0,tit)
        C12 =   MyClassStats2("<k/100",[],0,tit)
        C14 =   MyClassStats2("k/100",[],0,tit)
        
        self.classstats = [C1,C2,C4,C5,C6,C7,C8,C9,
                           C10,C13,C11,C12,C14]        
        
        print "###################################################"
        print "GQ STATS"
        print "###################################################"
        
        # computing the stats
        for idf in fileids:
                        
            ####################################################################
            
            filestats = []
            mydata = OpenFile(path+'/'+idf)
            mydata.lines = mydata.myread()
            
            ####################################################################
            
            print "==================================================="
            print idf
            print "==================================================="
            
            ####################################################################
 
            # patterns
            rest = []  
            
            # corpus
            corpus = MyClass2([".*"],[],idf,0,0,"corpus")
            
            ####################################################################  
            
            # some
            P1 = MyPatts2(some).P
            N1 = MyPatts2(rest).P
            c1 = MyClass2(P1,N1,idf,0,0,"some")
            
            # all
            P2 = MyPatts2(aall).P
            N2 = MyPatts2(rest).P           
            c2 = MyClass2(P2,N2,idf,0,0,"all")           
            
            ####################################################################  
    
            # the
#             P3 = MyPatts2(the).P
#             N3 = MyPatts2(rest).P
#             c3 = MyClass2(P3,N3,idf,0,0,"the")                      
            
            # >k
            P4 = MyPatts2(morek).P
            N4 = MyPatts2(rest).P
            c4 = MyClass2(P4,N4,idf,0,0,">k")                      
            
            # <k
            P5 = MyPatts2(lessk).P
            N5 = MyPatts2(rest).P
            c5 = MyClass2(P5,N5,idf,0,0,"<k")

            # k
            P6 = MyPatts2(exactlyk).P
            N6 = MyPatts2(rest).P
            c6 = MyClass2(P6,N6,idf,0,0,"k")
            
            ####################################################################
            
            # most
            P7 = MyPatts2(most).P
            N7 = MyPatts2(rest).P
            c7 = MyClass2(P7,N7,idf,0,0,"most")
                 
            # few
            P8 = MyPatts2(few).P
            N8 = MyPatts2(rest).P
            #few
            c8 = MyClass2(P8,N8,idf,0,0,"few")
                
            # >k/100
            P9 = MyPatts2(morekper).P
            N9 = MyPatts2(rest).P
            c9 = MyClass2(P9,N9,idf,0,0,">k/100")
    
            # <k/100
            P10 = MyPatts2(lesskper).P
            N10 = MyPatts2(rest).P
            c10 = MyClass2(P10,N10,idf,0,0,"<k/100")
                
            # k/100
            P13 = MyPatts2(kper).P
            N13 = MyPatts2(rest).P
            c13 = MyClass2(P13,N13,idf,0,0,"k/100")
                
            # >p/k
            P11 = MyPatts2(morethanpro).P
            N11 = MyPatts2(rest).P
            c11 = MyClass2(P11,N11,idf,0,0,">p/k")                    
            
            # <p/k
            P12 = MyPatts2(lessthanpro).P
            N12 = MyPatts2(rest).P
            c12 = MyClass2(P12,N12,idf,0,0,"<p/k")
            
            # p/k
            P14 = MyPatts2(pro).P
            N14 = MyPatts2(rest).P
            c14 = MyClass2(P14,N14,idf,0,0,"p/k")                      
            
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
                    #line = mydata.lines[i]
                    
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
                        
                        # some
                        c1.openSen(myline,c1.pats,c1.patts)
                        
                        ####################################################################
                        
                        # all      
                        c2.openSen(myline,c2.pats,c2.patts)
                        
                        ####################################################################
                        ####################################################################
             
                        # the   
                        #c3.openSen(myline,c3.pats,c3.patts)    
                                    
                        ####################################################################
                        
                        # >k
                        c4.openSen(myline,c4.pats,c4.patts)
                        
                        ####################################################################
                        
                        # <k
                        c5.openSen(myline,c5.pats,c5.patts)
                        
                        ####################################################################
                        
                        # k
                        c6.openSen(myline,c6.pats,c6.patts)
                        
                        ####################################################################
                        ####################################################################
              
                        # most
                        c7.openSen(myline,c7.pats,c7.patts)
                        
                        ####################################################################
                        
                        #few
                        c8.openSen(myline,c8.pats,c8.patts)
                        
                        ####################################################################            
                                  
                        #>k/100
                        c9.openSen(myline,c9.pats,c9.patts)
                        
                        ####################################################################
            
                        #<k100
                        c10.openSen(myline,c10.pats,c10.patts)
                        
                        ####################################################################
                        
                        # k/100
                        c13.openSen(myline,c13.pats,c13.patts)
              
                        ####################################################################
                        
                        # >p/k
                        c11.openSen(myline,c11.pats,c11.patts)
                        
                        ####################################################################
                        
                        # <p/k
                        c12.openSen(myline,c12.pats,c12.patts)
            
                        ####################################################################
                        
                        # p/k
                        c14.openSen(myline,c14.pats,c14.patts)
                
                        ####################################################################
                    
                    # if a sentence is found, skip the lines it
                    # covers in the loop, otherwise move to the
                    # next line
                    if sen.len > 0:
                        i = i + sen.len
                        # print 'senlen=', sen.len, '\n'
                        #print 'sen= ', sen.sen, '\n'
                    else:    
                        i = i + 1
                    # print 'explore at line= ', i, '\n'
                
                # move to new chunk
                mydata.lines = mydata.myread()
            
            ####################################################################
            ####################################################################
                       
            # total cum count
            tot = (c1.count + c2.count + c4.count + c5.count +
                    + c6.count + c7.count + c8.count + c9.count
                    + c10.count + c11.count + c12.count + c13.count 
                    + c14.count) + 1
    
            print "corpus size : " + `corpus.count` + " sentences"        
            print "==================================================="
            print "total matches: " + `tot` + " GQs"
            
            #relative frequencies
            c1.freq  = round(c1.count/tot,2)
            c2.freq  = round(c2.count/tot,2)
            #c3.freq  = round(c3.count/tot,2)
            c4.freq  = round(c4.count/tot,2)
            c5.freq  = round(c5.count/tot,2)
            c6.freq  = round(c6.count/tot,2)            
            c7.freq  = round(c7.count/tot,2)
            c8.freq  = round(c8.count/tot,2)
            c9.freq  = round(c9.count/tot,2)
            c10.freq = round(c10.count/tot,2)
            c11.freq = round(c11.count/tot,2)
            c12.freq = round(c12.count/tot,2)
            c13.freq = round(c13.count/tot,2)
            c14.freq = round(c14.count/tot,2)
            
            ####################################################################            
            
            filestats = [c1,c2,c4,c5,c6,c7,c8,c9,c10,c13,c11,c12,c14]
            
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
        #self.printClasses(self.classstats)
    

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

