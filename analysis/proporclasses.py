import string, re, array


from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import brown
from nltk.tag.util import str2tuple
from nltk.tag import pos_tag
from nltk import word_tokenize, sent_tokenize
from nltk.tag import DefaultTagger, UnigramTagger, BigramTagger
from nltk.tag.sequential import NgramTagger


# Class collecting stats
class MyClass2:


    #fileid:   filename
    #count :   feature occ frequency
    #freq  :   feature occ rel frequency
    #pats  :   set of regexps whose occ we want to check
    #patts :   set of regexps whose occ we want to rule out
    #tag   :   class name tag
    #typ   :   corpus type
    #tagger:   POS tagger for mining


    # object constructor
    def __init__(self,pats,patts,fileid,count,freq,tag,tagger):


        self.pats = pats
        self.patts = patts
        self.fileid = fileid
        self.count = count
        self.freq = freq
        self.tag = tag
        self.tagger = tagger


    # open file method
    def openFile(self,fileid,pats,patts):

        lcount = 0
        myfile = open(fileid,'r')
        my_tagger = self.tagger

        # case A (pos-tagged)
        if (re.search("brown",fileid) != None):
            try:
                text = myfile.read()
                lines = sent_tokenize(text)
                for line in lines:
                    pos = 0
                    #neg = 0
                    for pa in pats:
                        m = re.search(pa, line)
                        if (m != None):
                            pos = pos + 1
                        lcount = lcount + pos
            finally:
                self.count = lcount
                myfile.close()

        # case B (non-pos-tagged)
        if (re.search("brown",fileid) == None):
            try:
                text = myfile.read()
                lines = set(string.split(text,"\n"))
                for line in lines:
                    res2 = my_tagger.tag(line.split())
                    pos = 0
                    #neg = 0
                    for pa in pats:
                        m = re.search(pa, self.makestring(res2))
                        if m:
                            pos = pos + 1
                        lcount = lcount + pos
            finally:
                self.count = lcount
                myfile.close()

    # open file method (co-occurrence)
    def openFile2(self,fileid,pats,patts):

        lcount = 0
        myfile = open(fileid,'r')
        my_tagger = self.tagger

        # case A (pos-tagged)
        if (re.search("brown",fileid) != None):
            try:
                text = myfile.read()
                lines = sent_tokenize(text)
                for line in lines:
                    pos = 0
                    #neg = 0
                    for pa in pats:
                        m = re.search(pa, line)
                        if (m != None):
                            for paa in patts:
                                mm = re.search(paa, line)
                                if (mm != None):
                                    pos = pos + 1
                    lcount = lcount + pos
            finally:
                self.count = lcount
                myfile.close()

        # case B (non-pos-tagged)
        if (re.search("brown",fileid) == None):
            try:
                text = myfile.read()
                lines = set(string.split(text,"\n"))
                for line in lines:
                    res2 = my_tagger.tag(line.split())
                    pos = 0
                    #neg = 0
                    for pa in pats:
                        m = re.search(pa, self.makestring(res2))
                        if m:
                            for paa in patts:
                                mm = re.search(paa, self.makestring(res2))
                                if mm:
                                    pos = pos + 1
                    lcount = lcount + pos
            finally:
                self.count = lcount
                myfile.close()

    # convert pos-tagged words to pos-tagged text
    def makestring(self,tagged):
        res = ""
        for tup in tagged:
            res = res + tup[0].lower()+"/"+tup[1].lower()+" "
        return res

    # open file method-analysis (all patterns)
    def openFileAll(self,fileid,pats,patts):

        lcount = 0
        myfile = open(fileid,'r')
        my_tagger = self.tagger

        try:
                text = myfile.read()
                lines = set(string.split(text,"\n"))
                for line in lines:
                    res2 = my_tagger.tag(line.split())
                    pos = 0
                    #neg = 0
                    for pa in pats:
                        m = re.search(pa, self.makestring(res2))
                        if m:
                            for paa in patts:
                                mm = re.search(paa, self.makestring(res2))
                                if mm:
                                    pos = pos + 1
                    lcount = lcount + pos
        finally:
                self.count = lcount
                myfile.close()


####################################################################


# Class training POS taggers
class Tagger:


        #train     : traininig corpus
        #t0        : uniform tagger
        #t1        : unigram (MLE) tagger
        #t3        : bigram  (MLE) tagger


        # constructor
        def __init__(self):
            self.train = brown.tagged_sents(categories='news')
            #self.train = brown.tagged_sents()
            self.t0 = DefaultTagger('None')
            self.t1 = UnigramTagger(self.train,backoff=self.t0)
            self.t2 = BigramTagger(self.train,backoff=self.t1)
            self.t3 = NgramTagger(3,train=self.train,backoff=self.t2)


        # evaluate tagger accuracy
        def my_eval(self):
            self.gold = brown.tagged_sents(categories=['editorial','fiction'])
            acc0 = self.t2.evaluate(self.gold)
            acc1 = self.t2.evaluate(self.gold)
            acc2 = self.t3.evaluate(self.gold)
            print '1-gram (acc) = ' + `acc0`
            print '2-gram (acc) = ' + `acc1`
            print '3-gram (acc) = ' + `acc2`


####################################################################


# Class encapsulating lists of patterns
class MyPatts2:


        #P : list of regular expressions
        P = []


        # constructor
        def __init__(self,S):
            B = []
            for s in S:
                B.append(s)
            self.P = B


####################################################################


# Class encapsulating all the class stats
class MyClassStats2:


    #classes:    list of classes
    #avg:        average
    #tag:        class tag
    #typ:        corpus subset


    # constructor
    def __init__(self,tag,classes,avg,tit):
        self.tag = tag
        self.classes = classes
        self.avg = avg
        self.fre = 0
        self.tit = tit
