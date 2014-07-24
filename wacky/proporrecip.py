#===================#
#===================#
#                   #
# Class likelihoods #
#                   #
#===================#
#===================#


# python
from __future__ import division
from operator import attrgetter
from math import ceil


# my plotting + test classes
from corpuspkg.statsplot import MyPlot
from corpuspkg.statstests import STest


# nltk
from nltk.corpus import PlaintextCorpusReader


# my classes
from wacky.proporclasses import MyClass2, Tagger, MyPatts2, MyClassStats2
from wacky.savestats import SaveStats 


####################################################################
#################################################################### 

s0 = ".*"        # anything!

####################################################################
####################################################################
# A. simple classes
####################################################################
####################################################################

# 1. exists

s10 = "someone/pn"
s11 = "Someone/pn"

s12 = "somebody/pn"
s13 = "Somebody/pn"

s14 = "something/pn"
s15 = "Something/pn"

s16 = " some/dti"
s17 = " Some/dti"

s18 = " a/at"
s19 = " A/at"

s20 = " many/ap "
s21 = " Many/ap "

some = [s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20,s21]

####################################################################

# 4. all

s40 = " every/at "
s41 = " Every/at "

s42 = " all/abn "
s43 = " All/abn "

s44 = " the/at .*/nns "
s45 = " The/at ./nns "

s46 = " everything/pn "
s47 = " Everything/pn "

s48 = " everyone/pn " 
s49 = " Everyone/pn "

s4a = " everybody/pn " 
s4b = " Everybody/pn " 

s4c = " each/dt "
s4d = " Each/dt "

all = [s40,s41,s42,s43,s44,s45,s46,s47,s48,s49,s4a,s4b,s4c,s4d]

####################################################################

# 8.1 exactly one

s74 = " the/at "
s75 = " The/at "

the = [s74,s75]

####################################################################
####################################################################

# 6. at most k, less than k (k integer)

s60 = " at/in most/ap .*/cd "
s61 = " At/in most/ap .*/cd "

s20b = " less/ap than/in .*/cd "
s21b = " Less/ap than/in .*/cd "

s20bb = " fewer/ap than/in .*/at .*/cd "
s21bb = " Fewer/ap than/in .*/at .*/cd "

s22b = " less/ap than/in .*/at .*/cd "
s23b = " Less/ap than/in .*/at .*/cd "

s22bb = " fewer/ap than/in .*/at .*/cd "
s23bb = " Fewer/ap than/in .*/at .*/cd "

lessk = [s20b,s21b,s22b,s23b,s20bb,s21bb,s22bb,s23bb,s60,s61]

####################################################################

# 7. at least k, more than k (k integer)

s60b = " at/in least/ap .*/cd "
s61b = " At/in least/ap .*/cd "

s20 = " more/ap than/in .*/cd "
s21 = " More/ap than/in .*/cd "

s22 = " more/ap than/in .*/at .*/cd "
s23 = " More/ap than/in .*/at .*/cd "

morek = [s20,s21,s22,s23,s60b,s61b]

####################################################################

# 8. exactly k (k integer)

s70 = " .*/cd .*/nns "

s71 = " exactly/rb .*/cd "
s72 = " Exactly/rb .*/cd "

exactlyk = [s70,s71,s72]

####################################################################
####################################################################

# 9. more than p/k (p, q integers)

s80 = " more/ap than/in half/abn "
s81 = " More/ap than/in half/abn "

s82 = " more/ap than/in .*/cd .*/od "
s83 = " More/ap than/in .*/cd .*/od "

morethanpro = [s80,s81,s82,s83]

####################################################################

# 9.1 less than p/k (p, q integers)

s80b = " less/ap than/in half/abn "
s81b = " Less/ap than/in half/abn "

s80bb = " fewer/ap than/in half/abn "
s81bb = " Fewer/ap than/in half/abn "

s82b = " less/ap than/in .*/cd .*/od "
s83b = " Less/ap than/in .*/cd .*/od "

s82bb = " fewer/ap than/in half/abn "
s83bb = " Fewer/ap than/in half/abn "

lessthanpro = [s80b,s81b,s82b,s83b,s80bb,s81bb,s82bb,s83bb]

####################################################################

# 9.2 p/k (p, k integers)

s80c = " half/abn "
s81c = " .*/cd .*/od "

pro = [s80c,s81c]

####################################################################

# 3. more than k% (k a percentage)

s30 = " more/ap than/in .*/cd percent/nn "
s31 = " More/ap than/in .*/cd percent/nn "

morekper = [s30,s31]

####################################################################

# 3.1 less than k% (k a percentage)

s30b = " less/ap than/in .*/cd percent/nn "
s31b = " Less/ap than/in .*/cd percent/nn "

s30bb = " less/ap than/in .*/cd percent/nn "
s31bb = " Less/ap than/in .*/cd percent/nn "

lesskper = [s30b,s31b,s30bb,s31bb]

####################################################################

# 3.2 k% (k a percentage)

s30c = " ./cd percent/nn "

kper = [s30c]

####################################################################

# 5. most, more than half

s51 = " most/ap "
s52 = " Most/ap "

s53 = " more/ap than/in half/abn "
s54 = " More/ap than/in half/abn "

most = [s51,s52,s53,s54]

####################################################################

# 5.1 few, less than half, fewer than half

s51b = " few/ap "
s52b = " Few/ap "

s53b = " less/ap than/in half/abn "
s54b = " Less/ap than/in half/abn "

s53bb = " fewer/ap than/in half/abn "
s54bb = " Fewer/ap than/in half/abn "

few = [s51b,s52b,s53b,s54b,s53bb,s54bb]


####################################################################
####################################################################
# B. Reciprocal
####################################################################
####################################################################


ramsey = " each/dt other/ap "

eachother = [ramsey]


####################################################################
####################################################################


# Class encoding the plot(s) + test(s)


class ProporRamsey:
   
    
    # corpus            : path to corpora
    # format            : format of corpora (e.g. .txt files)
    # stats             : hash table with class stats of each corpus
    # classstats        : list with global stats (mean frequency) 
    # list              : list of legends in figure
    # plotting          : directory of compiled report

    
    # object constructor
    def __init__(self,path,format,list,plotting):
        self.stats = {} # stats
        self.classstats = [] # classes
        self.path = path # path of corpus
        self.format = format # format of file(s)
        self.occStats(path,format,list,plotting) # collects stats + plots them
        self.statTestB(self.classstats) # runs the stat tests
        self.list = list
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
        figname = "Ramsey GQs"
        figpath = plotting +'/'+ figname.replace(' ', '-') + '-stats.pdf'
        savpath = plotting +'/'+ figname.replace(' ', '-')
        
        # plotting
        MyPlot(self.stats,self.classstats,figname, "one",plotting,list) # all
        
        # generating report
        SaveStats(self.classstats,self.stats,figpath,savpath,plotting) # all
        
        
    #############################################################
    #############################################################        
 
            
    # creating the classes
    def fileStats(self,path,fileids):
        
        # starting the tagger
        my_tagger = Tagger().t3
        
        # starting the title
        tit = "Ramsey GQs"
        
        # stat classes
        
        C1  = MyClassStats2("Qall",[],0,tit)
        C2  = MyClassStats2("Qsome",[],0,tit)
        
        C4  = MyClassStats2("Q>k",[],0,tit)
        C5  = MyClassStats2("Q<k",[],0,tit)
        C6  = MyClassStats2("Qk",[],0,tit)
        
        C7  = MyClassStats2("Qmost",[],0,tit)
        C8  = MyClassStats2("Qfew",[],0,tit)
        C9  = MyClassStats2("Q>p/k",[],0,tit)             
        C10 = MyClassStats2("Q<p/k",[],0,tit)
        C13 = MyClassStats2("Qp/k",[],0,tit)
        
        C11 = MyClassStats2("Q>k/100",[],0,tit)
        C12 = MyClassStats2("Q<k/100",[],0,tit)
        C14 = MyClassStats2("Qk/100",[],0,tit)
        
        self.classstats = [C1,C2,C4,C5,C6,C7,C8,C9,
                           C10,C13,C11,C12,C14]        
        
        print "###################################################"
        print "GQ STATS"
        print "###################################################"
        
        # computing the stats
        for idf in fileids:
            
            ####################################################################
            
            filestats = []
            
            ####################################################################
            
            print "==================================================="
            print idf
            print "==================================================="
            # corpus
            #-------------------------------------------------------------------
            corpus = MyClass2([".*"],[],idf,0,0,"corpus",my_tagger)
            print "---------------------------------------------------"
            print " Computing corpus size"
            print "---------------------------------------------------"
            corpus.openFile(path+"/"+idf,corpus.pats,corpus.patts)        
            print "==> " + idf + " is of size : " + `corpus.count` + " sentences"
            
            ####################################################################            
            
            # patterns
            rest = eachother  
                    
            ####################################################################
            
            # class 1
            P1 = MyPatts2(some).P
            N1 = MyPatts2(rest).P
            #-------------------------------------------------------------------
            c1 = MyClass2(P1,N1,idf,0,0,"Qsome",my_tagger)
            print "---------------------------------------------------"
            print " Computing some + recip"
            print "---------------------------------------------------"
            c1.openFile2(path+"/"+idf,c1.pats,c1.patts)
            print "==> some + recip : " + `c1.count` + " matches"
            
            ####################################################################
            
            # class 2
            P2 = MyPatts2(all).P
            N2 = MyPatts2(rest).P
            #-------------------------------------------------------------------       
            c2 = MyClass2(P2,N2,idf,0,0,"Qall",my_tagger)
            print "---------------------------------------------------"
            print " Computing all + recip"
            print "---------------------------------------------------"
            c2.openFile2(path+"/"+idf,c2.pats,c2.patts)
            print "==> all + recip : " + `c2.count` + " matches"
        
            ####################################################################
            ####################################################################
            
            # class 4
            P4 = MyPatts2(morek).P
            N4 = MyPatts2(rest).P
            #-------------------------------------------------------------------
            c4 = MyClass2(P4,N4,idf,0,0,"Q>k",my_tagger)
            print "---------------------------------------------------"
            print " Computing at least k + recip"
            print "---------------------------------------------------"
            c4.openFile2(path+"/"+idf,c4.pats,c4.patts)
            print "==> at least k + recip: " + `c4.count` + " matches"
            
            ####################################################################
            
            # class 5
            P5 = MyPatts2(lessk).P
            N5 = MyPatts2(rest).P
            #-------------------------------------------------------------------
            c5 = MyClass2(P5,N5,idf,0,0,"Q<k",my_tagger)
            print "---------------------------------------------------"
            print " Computing at most k + recip"
            print "---------------------------------------------------"
            c5.openFile2(path+"/"+idf,c5.pats,c5.patts)
            print "==> at most k + recip: " + `c5.count` + " matches"
            
            ####################################################################
            
            # class 6
            P6 = MyPatts2(exactlyk).P
            N6 = MyPatts2(rest).P
            #-------------------------------------------------------------------
            c6 = MyClass2(P6,N6,idf,0,0,"Qk",my_tagger)
            print "---------------------------------------------------"
            print " Computing exactly k + recip"
            print "---------------------------------------------------"
            c6.openFile2(path+"/"+idf,c6.pats,c6.patts)
            print "==> exactly k + recip : " + `c6.count` + " matches"
            
            ####################################################################
            ####################################################################
  
            # class 7
            P7 = MyPatts2(most).P
            N7 = MyPatts2(rest).P
            #-------------------------------------------------------------------
            c7 = MyClass2(P7,N7,idf,0,0,"Qmost",my_tagger)
            print "---------------------------------------------------"
            print " Computing most + recip"
            print "---------------------------------------------------"
            c7.openFile2(path+"/"+idf,c7.pats,c7.patts)
            print "==> most + recip : " + `c7.count` + " matches"
            
            ####################################################################
            
            # class 8
            P8 = MyPatts2(few).P
            N8 = MyPatts2(rest).P
            #-------------------------------------------------------------------
            c8 = MyClass2(P8,N8,idf,0,0,"Qfew",my_tagger)
            print "---------------------------------------------------"
            print " Computing few + recip"
            print "---------------------------------------------------"
            c8.openFile2(path+"/"+idf,c8.pats,c8.patts)
            print "==> few + recip : " + `c8.count` + " matches"
            
            ####################################################################            
                      
            # class 9
            P9 = MyPatts2(morekper).P
            N9 = MyPatts2(rest).P
            #-------------------------------------------------------------------
            c9 = MyClass2(P9,N9,idf,0,0,"Q>k/100",my_tagger)
            print "---------------------------------------------------"
            print " Computing more than k%"
            print "---------------------------------------------------"
            c9.openFile2(path+"/"+idf,c9.pats,c9.patts)
            print "==> more than k% + recip : " + `c9.count` + " matches"
            
            ####################################################################

            # class 10
            P10 = MyPatts2(lesskper).P
            N10 = MyPatts2(rest).P
            #-------------------------------------------------------------------
            c10 = MyClass2(P10,N10,idf,0,0,"Q<k/100",my_tagger)
            print "---------------------------------------------------"
            print " Computing less than k% + recip"
            print "---------------------------------------------------"
            c10.openFile2(path+"/"+idf,c10.pats,c10.patts)
            print "==> less than k% + recip : " + `c10.count` + " matches"

            ####################################################################
            
            # class 13
            P13 = MyPatts2(kper).P
            N13 = MyPatts2(rest).P
            #-------------------------------------------------------------------
            c13 = MyClass2(P10,N10,idf,0,0,"Qk/100",my_tagger)
            print "---------------------------------------------------"
            print " Computing k% + recip"
            print "---------------------------------------------------"
            c13.openFile2(path+"/"+idf,c13.pats,c13.patts)
            print "==> k% + recip : " + `c13.count` + " matches"
            
            ####################################################################
            
            # class 11
            P11 = MyPatts2(morethanpro).P
            N11 = MyPatts2(rest).P
            #-------------------------------------------------------------------
            c11 = MyClass2(P11,N11,idf,0,0,"Q>p/k",my_tagger)
            print "---------------------------------------------------"
            print " Computing more than p/k + recip"
            print "---------------------------------------------------"
            c11.openFile2(path+"/"+idf,c11.pats,c11.patts)
            print "==> more than p/k + recip : " + `c11.count` + " matches"
            
            ####################################################################
 
            # class 12
            P12 = MyPatts2(lessthanpro).P
            N12 = MyPatts2(rest).P
            #-------------------------------------------------------------------
            c12 = MyClass2(P12,N12,idf,0,0,"Q<p/k",my_tagger)
            print "---------------------------------------------------"
            print " Computing less than p/k + recip"
            print "---------------------------------------------------"
            c12.openFile2(path+"/"+idf,c12.pats,c12.patts)
            print "==> less than p/k + recip : " + `c12.count` + " matches"   

            ####################################################################
            
            # class 14
            P14 = MyPatts2(pro).P
            N14 = MyPatts2(rest).P
            #-------------------------------------------------------------------
            c14 = MyClass2(P14,N14,idf,0,0,"Qp/k",my_tagger)
            print "---------------------------------------------------"
            print " Computing p/k + recip"
            print "---------------------------------------------------"
            c14.openFile2(path+"/"+idf,c14.pats,c14.patts)
            print "==> p/k + recip : " + `c14.count` + " matches" 
            
            ####################################################################
            ####################################################################
                        
            # total cum count
            tot = (c1.count + c2.count + c4.count + c5.count +
                    + c6.count + c7.count + c8.count + c9.count
                    + c10.count + c11.count + c12.count
                    + c13.count + c14.count) + 1
            
            print "==================================================="
            print tot, "total matches"
            
            #relative frequencies
            c1.freq  = round(c1.count/tot,2)
            c2.freq  = round(c2.count/tot,2)
            c4.freq  = round(c4.count/tot,2)
            c5.freq  = round(c5.count/tot,2)
            c6.freq  = round(c6.count/tot,2)            
            c7.freq  = round(c7.count/tot,2)
            c8.freq  = round(c8.count/tot,2)
            c9.freq  = round(c9.count/tot,2)
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

