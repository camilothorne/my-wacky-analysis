#import re, string, array
from subprocess import call, Popen


class SaveStats:


    # path         : path to report file
    # classstats   : class stats
    # stats        : filestats
    # plotfile     : path to the plot
    # report	   : path to output directory


    # constructor
    def __init__(self,classstats,stats,plotfile,path,report):
        self.classstats = classstats
        self.path = path + ".tex"
        self.plotfile = plotfile
        self.stats = stats
        # building the report
        res = self.makeRes(self.classstats, self.stats, self.plotfile)
        # saving the report
        print "###################################################"
        print "\n\npreparing report...\n\n"
        self.compileFile(self.path, res, report)
        self.fileSave(path + ".txt", res)


    # make contingency table
    def makeRes(self,classstats,stats,plotfile):

        # init frequencies
        freqs = {}

        # begin table
        table = r'\begin{sidewaystable}[p]' + "\n"
        table = table + r'\tiny{\begin{tabular}{|c|'
        for cla in classstats:
            table = table + "c|"
        table = table + "}" +"\n"

        # print class names
        for cla in classstats:
            table = table + " & " + r''+cla.tag
            freqs[cla.tag] = [[],0]
        table = table + r'\\' + "\n"
        table = table + r'\hline' + "\n"

        # print freqs
        for idf in stats.keys():
            table = table + idf[:6]
            for cla1 in classstats:
                for cla2 in stats[idf]:
                    if cla1.tag == cla2.tag:
                        table = table + " & " + `cla2.count`
            table = table + r'\\' + "\n"
        table = table + r'\hline' + "\n"

        # compute totals
        for idf in stats.keys():
            for cla1 in stats[idf]:
                for cla2 in classstats:
                    if cla1.tag == cla2.tag:
                        freqs[cla1.tag][0].append(cla1.count)
                for cla in classstats:
                    freqs[cla.tag][1] = sum(freqs[cla.tag][0])

        # print totals
        table = table + "total"
        for cla in classstats:
            table = table + " & " + `freqs[cla.tag][1]`
        table = table + "\n\end{tabular}}\n"
        table = table + "\end{sidewaystable}\n\n"


        # complete and return table
        fig = r'\begin{center}' + "\n\includegraphics[scale=0.5]{" + plotfile + "}\n\end{center}"
        res = table + "\n\n" + r'\vspace{0.2cm}' + "\n\n" + fig
        return res


    # save the table in a .tex file
    def fileSave(self,path,res):
        myfile = open(path,'w')
        myfile.write(res)
        myfile.close()


    # compile with pdflatex
    def compileFile(self,path,res,report):
        myfile = open(path,'w')
        myfile.write("\documentclass[a4,10pt]{article}")
        myfile.write("\n\n")
        myfile.write("\usepackage{graphicx}\n")
        myfile.write("\usepackage{epstopdf}\n")
        myfile.write("\usepackage{times}\n")
        myfile.write("\usepackage{rotating}\n")
        myfile.write("\n\n")
        myfile.write(r'\begin{document}')
        myfile.write("\n\n")
        myfile.write(res)
        myfile.write("\n\n")
        myfile.write("\end{document}")
        myfile.close()
        call(['/usr/bin/pdflatex','-output-directory='+report,path],shell=False)
