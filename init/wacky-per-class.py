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


from proporrecipC import *


# Corpora root files and format


# N.B. Some corpora are stored in /nltk_lite/
# while custom corpora are stored elsewhere


# brown + wacky 100M subset


path 	 = "/home/professors/cathorne/Desktop/quantifiers/wacky-script/corpus-medium/"
format 	 = ".*test"
list   	 = ('avg','cumul','brown','ukwack')
plotting = '/home/professors/cathorne/Desktop/quantifiers/wacky-script/plotting-extra'


# GQs (Jakub)


ProporRamseyAll(path, format, list, plotting)


# N.B. By quantifier
