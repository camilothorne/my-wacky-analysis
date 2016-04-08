#!/usr/bin/python


'''
Created on April 8, 2016
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


# analysis functions
from proporB import *
from proporcumB import *


# corpora root files and format
plotting      = '/home/camilo/wacky-corpus/wackypedia/plotting/'
path          = "/home/camilo/wacky-corpus/wackypedia/"
fformat        = ".*test"
listA          = ('mean','cumul','wacky','stut')
listB          = ('wacky','stut')


# all GQs
ProporStatsF(path, fformat, listA, plotting)


# by GQ class
ProporStatsCumF(path, fformat, listB, plotting)
