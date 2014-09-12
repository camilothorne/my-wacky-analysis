#!/usr/bin/python

'''
Created on Jul 29, 2014
@author: camilothorne
'''


#================#
#================#
#                                     #
#         Stats script        #
#         (init file)             #
#                                      #
#================#
#================#


# custom libraries
import sys
sys.path.append(u'../mynltk/')


# analysis functions
from propor import *


# corpora root files and format
plotting = '  foo '
path     = "  goo "
format   = "*.test"
list     = ('ukwack')


# all GQs
ProporStats(path, format, list, plotting)