#!/usr/bin/python


# (testing)


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


# N.B. 1. Some corpora are stored in /usr/lib/nltk_lite/
# while custom corpora are stored elsewhere


# original + wacky 1M subset


plotting = '/home/professors/cathorne/Desktop/quantifiers/wacky-script/plotting-test'
path     = "/home/professors/cathorne/Desktop/quantifiers/wacky-script/corpus-small/"
format   = ".*test"
list     = ('brown','clinical','geo','trec','ukwack')


# Ramsey GQs (Jakub)


ProporRamsey(path, format, list, plotting)
