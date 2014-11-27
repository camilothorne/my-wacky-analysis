#!/usr/bin/python


'''
Created on Jul 29, 2014
@author: camilothorne
'''


#================#
#================#
#
#  Stats script
#  (init file)   
#
#================#
#================#


# custom libraries
import sys
sys.path.append(u'../../quan-nltk/')


# analysis functions
from proporB import *
from proporcumB import *


# corpora root files and format
plotting      = '/home/camilothorne/wacky-corpus/plotting-huge/'
path          = "/home/camilothorne/wacky-corpus/wacky-huge/"
format        = ".*tagged"
listA          = ('mean','cumul','stut','wacky')
listB          = ('stut','wacky')

# all GQs
ProporStatsF(path, format, listA, plotting)
# by GQ class
ProporStatsCumF(path, format, listB, plotting)
