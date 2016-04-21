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
from monoproporB import *
from monoproporcumB import *


# corpora root files and format
plotting      = '/home/camilo/wacky-corpus/wackypedia/plotting/'
path          = "/home/camilo/wacky-corpus/wackypedia/"

#fformat        = ".*test"

fformat        = ".*testa"

# listA          = ('mean','cumul','wacky','stut')
# listB          = ('wacky','stut')

listA          = ('mean','cumul','wackypedia')
listB          = ('wackypedia','')


# all GQs
ProporStatsE(path, fformat, listA, plotting)


# by GQ class
ProporStatsCumE(path, fformat, listB, plotting)