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
#sys.path.append(u'../quan-nltk/')


# analysis functions
from proporB import *
from proporcumB import *


# corpora root files and format
plotting      = '/home/camilo/wacky-corpus/wackypedia/plotting/'
path          = "/home/camilo/wacky-corpus/wackypedia/"
format        = ".*test"
listA          = ('mean','cumul','wacky','stut')
listB          = ('wacky','stut')

# all GQs
ProporStatsF(path, format, listA, plotting)
# by GQ class
ProporStatsCumF(path, format, listB, plotting)
