## console.py
## Author:   James Thiele
## Date:     27 April 2004
## Version:  1.0
## Location: http://www.eskimo.com/~jet/python/examples/cmd/
## Copyright (c) 2004, James Thiele
## Modified: Paul Bucci 2014
## Purpose: Console framework for ease of use and debugging
## Website: PaulBucci.ca

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
        self.intro  = 'Welcome to console!'  ## defaults to None
        self.texts = []
        self.classes = []
        self.jobs = []
        self.loadAllClasses()
        self.ignore = self.getClass('ignore')
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
                count = len(p.focals)
                print(p.id + " focal node count is " + str(count))

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
                print(str(self.maxcost) + ",10,5,2,1,sentence")
                one_twenty = p.countColocations(self.maxcost)
                ten = p.countColocations(10)
                five = p.countColocations(5)
                two = p.countColocations(2)
                one = p.countColocations(1)
                sentence = p.countAllInSentence()
                print(str(one_twenty) + ',' + str(ten) + ',' + str(five) + ',' + str(two) + ',' + str(one) + ',' + str(sentence))

    # Print summary report
    def do_save_summary(self,line):
        '''Prints a summary to CSV.'''
        file = open(self.dirpath + 'summary.csv', 'w')
        file.write('id,' + str(self.maxcost) + ',10,5,2,1,sentence\n')
        for t in self.texts:
            for p in t.profiles:
                file.write(t.id + '_' + p.id + '_,')
                one_twenty = p.countColocations(self.maxcost)
                ten = p.countColocations(10)
                five = p.countColocations(5)
                two = p.countColocations(2)
                one = p.countColocations(1)
                sentence = p.countAllInSentence()
                file.write(str(one_twenty) + ',' + str(ten) + ',' + str(five) + ',' + str(two) + ',' + str(one) + ',' + str(sentence) + '\n')
        file.close()
                
    # Prints profile to console
    def do_profiles(self,line):
        '''Prints all profiles.'''
        for t in self.texts:
            print(t.id)
            for p in t.profiles:
                p.printProfile()

    # Print a per-character count to CSV
    def do_spcc(self,line):
        '''Prints a summary to CSV.'''
        for t in self.texts:
            for p in t.profiles:
                file = open(self.dirpath + "_" + p.id + "_per_char_count.csv", 'w')
                dict = p.focal_by_compare_by_edges()
                file.write(p.compare.id + ",")
                for c in p.compare.chars:
                    file.write(c + "," + str(self.maxcost) + ",10,5,1,sentence,")
                file.write("\n")
                for f,chars in dict.items():
                    file.write(f + ",")
                    for char,count in chars.items():
                        file.write(",")
                        for k,v in count.items():
                            file.write(str(v) + ",")
                    file.write("\n")
                file.close()

    def do_load(self,line):
        ''' Loads all texts in a directory.'''
        log('Loading texts and jobs. Might take a minute.')
        del self.texts[:]
        del self.jobs[:]
        self.loadAllJobs()
        self.loadAllTexts()
    
    def do_hz(self,line):
        '''Browse node profiles to get focal character frequencies'''
        i = input("Please type the list of characters and focal class for which you wish to search.\nFor example, to search for the X character within the Capitals focal class, type:\n\t=>> Capitals,X\n" + self.prompt)
        s = i.split(',')
        cl = self.getClass(s[0])
        chars = s[1:]
        print('Class is ' + cl.id + ' and Characters are : ' + str(chars))
        self.saveFrequency(cl,chars)

    # Chars is list of characters
    def saveFrequency(self,clazz,char_set):
        file = open(self.dirpath + "_" + clazz.id + "_char_frequency.csv", 'w')
        file.write('text_name,')
        for c in char_set:
            file.write(c + ',')
        file.write('\n')
        for text in self.texts:
            file.write(text.id + ',')
            for node_profile in text.profiles:
                if (node_profile.focal == clazz):
                    new_dict = collections.OrderedDict()
                    dict = node_profile.focalCountDict()
                    for c in char_set:
                        new_dict[c] = dict[c]
                    for key,value in new_dict.items():
                        file.write(str(value) + ',')
                    file.write('\n')
                    break
        file.close()

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
    console = ParseHandler('/Users/carsonklogan/Desktop/collocation_profiler/texts')
    console.cmdloop()
