#!/usr/bin/python


# custom libraries


import sys


sys.path.append(u'../mynltk/')


#================#
#================#
#                #
#  Stats script  #
# (init file)    #
#                #
#================#
#================#


from proporrecipB import *


# Corpora root files and format


# N.B. Some corpora are stored in /usr/lib/nltk_lite/
# while custom corpora are stored elsewhere


# original + wacky 1M subset


plotting = '/home/professors/cathorne/Desktop/quantifiers/wacky-script/plotting-class'
path     = "/home/professors/cathorne/Desktop/quantifiers/wacky-script/corpus-medium/"
format   = ".*test"
list     = ('brown','ukwack')


# Ramsey GQs by class (Jakub)


ProporRamsey(path, format, list, plotting)
