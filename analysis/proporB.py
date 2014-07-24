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
from analysis.proporclasses import MyClass2, Tagger, MyPatts2, MyClassStats2
from analysis.savestats import SaveStats


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
# B. superclasses
####################################################################
####################################################################


aristotelian = [s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20,s21,
                s40,s41,s42,s43,s44,s45,s46,s47,s48,s49,s4a,s4b,
                s4c,s4d,s74,s75]

proportional = [s80,s81,s82,s83,s80b,s81b,s82b,s83b,
                s51,s52,s53,s54,s51b,s52b,s53b,s54b,
                s30,s31,s30b,s31b,s80bb,s81bb,s82bb,s83bb,
                s30bb,s31bb,s53bb,s54bb,s30,s31,s30c]

counting     = [s60,s61,s60b,s61b,s20,s21,s22,s23,s70,s71,s72,
                s20b,s21b,s22b,s23b,s20bb,s21bb,s22bb,s23bb]


####################################################################
####################################################################


# Class encoding the plot(s) + test(s)


class ProporStats:


    # corpus           : path to corpora
    # format           : format of corpora (e.g. .txt files)
    # stats            : hash table with class stats of each corpus
    # classstats       : list with global stats (mean frequency)
    # statsCum         : hash table with class stats of each corpus X quantifier class
    # classstatsCum    : list with global stats (mean frequency) X quantifier class
    # list	       : list of legends in figure
    # plotting	       : directory of compiled report


    # object constructor
    def __init__(self,path,format,list,plotting):
        self.statsCum = {} # stats (cum)
        self.classstatsCum = [] # classes (cum)
        self.path = path # path of corpus
        self.format = format # format of file(s)
        self.occStats(path,format,list,plotting) # collects stats + plots them
        self.statTestB(self.classstatsCum) # runs the stat tests (by quantifier class)
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
        self.fileStatsCum(path,fileids)

        # plotting vars (2)
        fignameCum = "Base GQs"
        figpathCum = plotting +'/'+ fignameCum.replace(' ', '-') + '-stats.pdf'
        savpathCum = plotting +'/'+ fignameCum.replace(' ', '-')

        # plotting
        MyPlot(self.statsCum,self.classstatsCum,fignameCum, "three",plotting,list) # cum

        # generating report
        SaveStats(self.classstatsCum,self.statsCum,figpathCum,savpathCum,plotting) # cum


    #############################################################
    #############################################################


    # creating the cumulative classes
    def fileStatsCum(self,path,fileids):

        # starting the tagger
        my_tagger = Tagger().t3

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

            filestatsCum = []

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
            rest = []

            ####################################################################

            # class 1
            P1 = MyPatts2(aristotelian).P
            N1 = MyPatts2(rest).P
            #-------------------------------------------------------------------
            c1 = MyClass2(P1,N1,idf,0,0,"ari",my_tagger)
            print "---------------------------------------------------"
            print " Computing aristotelian"
            print "---------------------------------------------------"
            c1.openFile(path+"/"+idf,c1.pats,c1.patts)
            print "==> aristotelian : " + `c1.count` + " matches"

            ####################################################################

            # class 2
            P2 = MyPatts2(counting).P
            N2 = MyPatts2(rest).P
            #-------------------------------------------------------------------
            c2 = MyClass2(P2,N2,idf,0,0,"cnt",my_tagger)
            print "---------------------------------------------------"
            print " Computing counting"
            print "---------------------------------------------------"
            c2.openFile(path+"/"+idf,c2.pats,c2.patts)
            print "==> counting : " + `c2.count` + " matches"

            ####################################################################

            # class 3
            P3 = MyPatts2(proportional).P
            N3 = MyPatts2(rest).P
            #-------------------------------------------------------------------
            c3 = MyClass2(P3,N3,idf,0,0,"pro",my_tagger)
            print "---------------------------------------------------"
            print " Computing proportional"
            print "---------------------------------------------------"
            c3.openFile(path+"/"+idf,c3.pats,c3.patts)
            print "==> proportional : " + `c3.count` + " matches"

            ####################################################################

            # total cum count
            tot = (c1.count + c2.count + c3.count) +1

            print "==================================================="
            print tot, "total matches"

            #relative frequencies
            c1.freq  = round(c1.count/tot,2)
            c2.freq  = round(c2.count/tot,2)
            c3.freq  = round(c3.count/tot,2)

            ####################################################################

            filestatsCum = [c1,c2,c3]

            ####################################################################

            self.statsCum[idf] = filestatsCum

            ####################################################################

            for cla in self.classstatsCum:
                for thiscls in filestatsCum:
                    if (thiscls.tag == cla.tag):
                        cla.classes.append(thiscls)

            ####################################################################

        # updating the distribution (2)
        self.classAvg(self.classstatsCum)
        self.classAvg2(self.classstatsCum)
        sort = self.sortClass(self.classstatsCum)
        self.classstatsCum = sort
        print "###################################################"
        self.printClasses(self.classstatsCum)


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

