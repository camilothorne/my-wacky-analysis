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
sys.path.append(u'../mynltk/')


# analysis functions
from proporB import *
from proporcumB import *


# corpora root files and format
plotting      = '/home/camilothorne/wacky-corpus/plotting-deu/'
path          = "/home/camilothorne/wacky-corpus/wackypedia/"
format        = ".*test"
list          = ('wacky','stut')


# all GQs
ProporStatsF(path, format, list, plotting)
# by GQ class
ProporStatsCumF(path, format, list, plotting)