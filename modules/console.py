## console.py
## Author:   James Thiele
## Date:     27 April 2004
## Version:  1.0
## Location: http://www.eskimo.com/~jet/python/examples/cmd/
## Copyright (c) 2004, James Thiele
## Modified: Paul Bucci, Carson Logan 2014
## Modified: Peter Kirby 2016
## Purpose: Console framework for ease of use and debugging

import os
import cmd
import readline
from text import *
from node import *
from jobs import jobs
from printer import log
import collections
import sys

class ParseHandler(cmd.Cmd):
    def __init__(self,dirpath):
        cmd.Cmd.__init__(self)
        self.prompt = '=>> '
        self.intro  = 'Welcome to console!'  # defaults to None
        self.texts = []
        self.classes = []
        self.jobs = []
        self.loadAllClasses()
        self.ignore = self.getClass('ignore')
        self.costs = [50, 10, 5, 2, 1]
        self.maxcost = 50
        self.dirpath = dirpath
    
    # Creates a TextMeta object
    def loadText(self,textpath):
        t = TextHandler(textpath,self)
        self.texts.append(t)
    
    # Loads all texts in a directory
    def loadAllTexts(self):
        for file in os.listdir(self.dirpath):
            if file[0] != '.':
                log('Loading ' + file + '.')
                self.loadText(self.dirpath + '/' + file)
        for text in self.texts:
            text.nodify()
    
    # Returns a class from self.classes
    def getClass(self,id):
        for c in self.classes:
            if c.id == id:
                return c
        print('No class found for ' + id)
        return None
    
    # Sets the directory in which to look for texts
    def setTextDirectory(self,path):
        self.dirpath = str(path)
    
    # Loads classes from classes.py
    def loadAllClasses(self):
        from classes import classes
        for id,chars in classes.items():
            self.loadClass(id,chars)
    
    # Creates a character class
    # id    : string
    # chars : list of characters
    def loadClass(self,id,chars):
        c = CharacterClass(id,chars)
        self.classes.append(c)
    
    # Generates an Edge Profile for a set of terms
    def run_profile(self,focal,comparison,stopwords,delimiters,maxcost):
        log('Running profile: ' + focal + '_' + comparison + '_' + stopwords + '_' + delimiters)
        for t in self.texts:
            t.generateProfile(self.getClass(focal),
                              self.getClass(comparison),
                              self.getClass(stopwords),
                              self.getClass(delimiters),
                              maxcost)

    # Loads dictionary from jobs.py
    def loadAllJobs(self):
        for n,j in jobs.items():
            self.jobs.append(j)

    ###### Command definitions ######

    '''Prints the names of all loaded texts.'''
    def do_text_names(self,line):
        for t in self.texts:
            print(t.id)

    def do_count_all_nodes(self,line):
        '''Count all nodes in all texts'''
        count = 0
        for t in self.texts:
            t_count = len(t.nodes)
            print(t.id + ' ' + str(t_count))
            count = count + t_count
        print("Total node count: " + str(count))

    def do_classes(self,line):
        ''' Prints available classes.'''
        for c in self.classes:
            print(c.id)

    def do_count_all_focal_nodes(self,line):
        '''Counts all focal nodes in all texts.'''
        for t in self.texts:
            print(t.id)
            for p in t.profiles:
                print(p.id + " focal node count is " + str(p.countFocals))

    def do_count_all_focal_edges(self,line):
        '''For each focal node in each text, prints count of f.edges.'''
        for t in self.texts:
            for p in t.profiles:
                count = p.countFocalEdges()
                print(t.id + " edge count is " + str(count))

    def do_set(self,line):
        '''Set a profile property to run in this form:
            
            set,focal,ubc_words

        '''
        command = line.split(',')
        self.command[0] = command[1]
    
    def do_run_profile(self,line):
        ''' Parses a line to run a specific profile.
            example : run_profile,focal,compare,stop,delim,50
        '''
        s = line.split(',')
        self.run_profile(s[1],s[2],s[3],s[4],int(s[5]))
    
    def do_text_nodes(self,line):
        '''Prints all nodes in all texts.'''
        for t in self.texts:
            for n in t.nodes:
                n.printNode()

    def do_jobs(self,line):
        '''Quick command for do all in job_batch function.'''
        for j in self.jobs:
            self.run_profile(j[0], j[1], j[2], j[3], j[4])
        log('Done running job batch.')

    # print summary report
    def do_summary(self,line):
        '''Prints summary to console.'''
        for t in self.texts:
            print(t.id + " with " + str(len(t.profiles)) + " num of profiles")
            for p in t.profiles:
                print(p.id)
                categories = ['era', 'genre', 'node count', 'sentence count']
                categories.extend(['compare count', 'focal count', 'compare class', 'focal class'])
                categories.extend(['sentence'] + [str(x) for x in self.costs])
                for type in ['sentence'] + [str(x) for x in self.costs]:
                    categories.extend([type + ' ' + x for x in ['other pos', 'other neg', 'focal pos', 'focal neg']])
                print(','.join(x for x in categories))
                data = [t.era, t.genre, str(p.countNodes()), str(p.countSentences())]
                data.extend([str(p.compare_count), str(p.focal_count), p.compare.id, p.focal.id])
                data.append(str(p.countAllInSentence()))
                for cost in self.costs:
                    data.append(str(p.countColocations(cost)))
                data.extend([])
                data.extend([str(v) for k,v in sorted(p.contingency.items(), reverse=True)])
                print(','.join(x for x in data))

    # Print summary report
    def do_save_summary(self,line):
        '''Prints a summary to CSV.'''
        file = open(self.dirpath + 'summary.csv', 'w')
        categories = ['id', 'era', 'genre', 'node count', 'sentence count']
        categories.extend(['compare count', 'focal count', 'compare class', 'focal class'])
        categories.extend(['sentence'] + [str(x) for x in self.costs])
        for type in ['sentence'] + [str(x) for x in self.costs]:
            categories.extend([type + ' ' + x for x in ['other pos', 'other neg', 'focal pos', 'focal neg']])
        file.write(','.join(x for x in categories) + '\n')
        for t in self.texts:
            for p in t.profiles:
                data = [t.id + '_' + p.id]
                data.extend([t.era, t.genre, str(p.countNodes()), str(p.countSentences())])
                data.extend([str(p.compare_count), str(p.focal_count), p.compare.id, p.focal.id])
                data.append(str(p.countAllInSentence()))
                for cost in self.costs:
                    data.append(str(p.countColocations(cost)))
                data.extend([str(v) for k,v in sorted(p.contingency.items(), reverse=True)])
                file.write(','.join(x for x in data) + '\n')
        file.close()
                
    # Prints profile to console
    def do_profiles(self,line):
        '''Prints all profiles.'''
        for t in self.texts:
            print(t.id)
            for p in t.profiles:
                p.printProfile()

    def do_load(self,line):
        ''' Loads all texts in a directory.'''
        log('Loading texts and jobs. Might take a minute.')
        del self.texts[:]
        del self.jobs[:]
        self.loadAllJobs()
        self.loadAllTexts()
    
    def do_set_dirpath(self,line):
        '''Sets the path to the text directory.'''
        self.dirpath = line
        print('Text path set to ' + line)
    
    def do_dirpath(self,line):
        '''Prints the current text directory.'''
        print(self.dirpath)
    
    def do_set_max(self,line):
        '''Sets the max cost for edges. Makes parsing faster the smaller it is.'''
        self.maxcost = line
        self.costs[0] = self.maxcost
        print('Max cost set to ' + line)

    def do_hist(self, args):
        '''print(a list of commands that have been entered'''
        print(self._hist)
    
    def do_exit(self, args):
        '''Exits from the console'''
        return -1
    
    ## Command definitions to support Cmd object functionality ##
    def do_EOF(self, args):
        '''Exit on system end of file character'''
        return self.do_exit(args)
    
    def do_shell(self, args):
        '''Pass command to a system shell when line begins with "!"'''
        os.system(args)
    
    def do_help(self, args):
        '''Get help on commands
            'help' or '?' with no arguments prints a list of commands for which help is available
            'help <command>' or '? <command>' gives help on <command>
            '''
        ## The only reason to define this method is for the help text in the doc string
        cmd.Cmd.do_help(self, args)
    
    ## Override methods in Cmd object ##
    def preloop(self):
        '''Initialization before prompting user for commands.
            Despite the claims in the Cmd documentaion, Cmd.preloop() is not a stub.
            '''
        cmd.Cmd.preloop(self)   ## sets up command completion
        self._hist    = []      ## No history yet
        self._locals  = {}      ## Initialize execution namespace for user
        self._globals = {}
    
    def postloop(self):
        '''Take care of any unfinished business.
            Despite the claims in the Cmd documentaion, Cmd.postloop() is not a stub.
            '''
        cmd.Cmd.postloop(self)   ## Clean up command completion
        print('Exiting...')
    
    def precmd(self, line):
        ''' This method is called after the line has been input but before
            it has been interpreted. If you want to modifdy the input line
            before execution (for example, variable substitution) do it here.
            '''
        self._hist += [ line.strip() ]
        return line
    
    def postcmd(self, stop, line):
        '''If you want to stop the console, return something that evaluates to true.
            If you want to do some post command processing, do it here.
            '''
        return stop
    
    def emptyline(self):
        '''Do nothing on empty input line'''
        pass
    
    def default(self, line):
        '''Called on an input line when the command prefix is not recognized.
            In that case we execute the line as Python code.
            '''
        try:
            exec(line) in self._locals, self._globals
        except Exception as e:
            print(e.__class__, ':', e)

if __name__ == '__main__':
    console = ParseHandler('/mnt/c/Users/Peter/Desktop/character_profiler/texts')
    console.cmdloop()

