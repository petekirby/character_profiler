# -*- coding: utf-8 -*-
import os
import threading
import codecs
import sys
import copy
import cmd
from node import *

##############################################
# A set of characters with a unique identifier
class CharacterClass(object):
    def __init__(self,id,chars):
        # a string identifier such as "gods" or "delimiters"
        self.id = id
        # the list of Characters
        self.chars = chars

##############################################
# Text information for easy classification
class TextMeta(object):
    def __init__(self,textpath,ph,*maxcost):
        # The handler
        self.parsehandler = ph
        # Parse the file path
        self.pathcopy = copy.copy(textpath)
        self.id = self.pathcopy.split("/").pop().split(".").pop(0)
        splittext = textpath.split("/").pop().split("_")
        # Fields that parse for organization
        self.path = textpath
        self.genre = int(splittext[0][1])
        self.school = splittext[1]
        self.genreNum = int(splittext[2])
        self.name = splittext[3]
        self.seg = splittext[4]
        self.punc = splittext[5].split(".")[0]
        # The text file itself
        self.file = codecs.open(self.path,encoding='utf-8')
        # The analyses
        self.profiles = []
        if len(maxcost) == 1:
            self.maxcost = maxcost[0]
        else:
            self.maxcost = sys.maxint

    # A function that generates a profile for comparing two or more
    # classes. The profile can be seen as a directed weighted graph
    # focalClass        : CharacterClass
    # comparisonClass   : list of CharacterClass
    def generateCorrelationProfile(self, focalClass, comparisonClasses):
        profile = CorrelationProfile(focalClass, comparisonClasses, self)
        self.profiles.append(profile)

##############################################
# A profile of character sets interactions
# metadata about a particular text
class CorrelationProfile(object):
    def __init__(self,focalClass,comparisonClasses,textmeta):
        self.id = textmeta.id + focalClass.id + "_" + comparisonClasses[0].id
        self.textmeta = textmeta
        self.focalClass = focalClass
        self.comparisonClasses = comparisonClasses
        # Match lists
        self.focalMatches = []
        self.comparisonMatches = []
        # Nodes are directed
        self.nodes = []

        print "Generating correlation profile for " + self.textmeta.id
        self.generateMatches()
        self.generateNodesAndEdges()
        self.gexfGraph()

    # Parses the input file character by character to
    # find matches.
    def generateMatches(self):
        print "Generating matches for " + self.textmeta.id
        # Position in file
        pos = 0
        while True:
            # we read the entire file one character at at time
            str = self.textmeta.file.read(1)
            c = str.encode('utf-8')
            # If not c, we've hit the end of the file
            if not c:
                break
            # only continue (i.e., increment the count, etc)
            # if we aren't ignoring this character
            if (c in self.textmeta.parsehandler.ignore.chars):
                continue
            pos = pos + 1
            # If c is a focal character, add it to the match list
            if (c in self.focalClass.chars):
                m = Match(c,pos,self.focalClass)
                self.focalMatches.append(m)
                continue
            # If c is a comparison class character, add it to the comparison match list
            for cc in self.comparisonClasses:
                if (c in cc.chars):
                    m = Match(c,pos,cc)
                    self.comparisonMatches.append(m)

    # Calculates edges between match nodes and generates
    # a directed edge object
    def generateNodesAndEdges(self):
        print "Generating nodes and edges for " + self.textmeta.id + " within " + str(self.textmeta.maxcost)
        for f in self.focalMatches:
            n = Node(f,f.pos)
            for c in self.comparisonMatches:
                cost = c.pos - f.pos
                e = Edge(c,cost)
                if e.abscost <= self.textmeta.maxcost:
                    n.add(e)
            self.nodes.append(n)

    # Prints pertainent information from all nodes
    def printNodes(self):
        for n in self.nodes:
            n.printNode()

    # Counts all matches within a certain distance for all
    # focal characters matches, allows double-counting for
    # places where two focal characters are in proximity <= 2*cost
    def countWithin(self,cost):
        count = 0
        for n in self.nodes:
            count = count + n.countWithin(cost)
        return count
    
    # Count character occurence in a text
    def countCharInText(self,char):
        count = 0
        for f in self.focalMatches:
            if f.char == char:
                count = count + 1
        for c in self.comparisonMatches:
            if c.char == char:
                count = count + 1
        return count

    # Counts totals for specific occurance of a character
    # with absolute distance <= cost
    def countMatchesForCharacterWithin(char,cost):
        return len(self.getMatchesForCharacterWithin(char,cost))
    
    # Gets all matches in node list with char as focal
    # and absolute distance <= cost
    def getMatchesForCharacterWithin(self,char,cost):
        list = []
        for n in self.nodes:
            nodelist = n.getWithin(cost)
            for nl in nodelist:
                if nl.focal == char:
                    list.append(nl)
        return list

    # Get matches between class within cost
    def getMatchesInSentenceWithinCost(self,cost,cc):
        list = []
        for n in self.nodes:
            list = list + n.getMatchesBetween(cc,n.getWithin(cost))
        return list

    # Count matches between class within cost
    def countMatchesInSentenceWithinCost(self,cost,cc):
        count = len(self.getMatchesInSentenceWithinCost(cost,cc))
        return count

    def gexfGraph(self):
        print "Printing GEXF"
        file = open(self.textmeta.parsehandler.dirpath + '/.graphs/' + self.id + '_graph.gexf', 'w')
        file.write('<?xml version="1.0" encoding="UTF-8"?>\n<gexf xmlns="http://www.gexf.net/1.2draft" version="1.2">\n<graph mode="static" defaultedgetype="directed">\n<attribute id="0" title="cost" type="integer"/>\n<nodes>')
        for n in self.nodes:
            file.write('<node id="' + str(n.id) + '" label="' + str(n.focal.pos) + '"></node>\n')
            for e in n.edgelist:
                file.write('<node id="' + str(e.to.pos) + '" label="' + str(n.focal.pos) + '">\n')
                file.write('<attvalue for="0" value="' + str(e.abscost) + '"/>')
        file.write('</nodes>\n<edges>')
        for n in self.nodes:
            for e in n.edgelist:
                file.write('<edge id="' + str(e.to.pos) + '" source="' + str(n.id) + '" target="' + str(e.to.pos) + '"/>')
        file.write('</edges>\n</graph>\n</gexf>')
        file.close()





##############################################
# A focal character and an ordered list of
# edges to comparision characters
class Node(object):
    def __init__(self,fc,id):
        # Focal character
        self.focal = fc
        # Ordered list of edges from
        # nearest to farthest
        self.edgelist = []
        self.id = id
    
    # Adds an edge, maintains edge order
    # in terms of absolute distance
    def add(self,e):
        if len(self.edgelist) == 0:
            self.edgelist.append(e)
        else:
            i = 0
            for edge in self.edgelist:
                if e.abscost < edge.abscost:
                    self.edgelist.insert(i,e)
                    break
                i = i + 1
            self.edgelist.append(e)
    
    # Match count <= cost
    def countWithin(self,cost):
        count = len(getWithin(cost))
        return count
    
    # Get all edges <= cost
    # edges is a filtered list of edges, defaults to full list
    def getWithin(self,cost):
        list = []
        for e in self.edgelist:
            if e.abscost <= cost:
                list.append(e)
        return list
    # else break
    
    # Get all matches between two of a class of character
    def getMatchesBetween(self,charClass,*edges):
        right = None
        left = None
        list = []
        if len(edges) == 0:
            edges = self.edgelist
        else:
            edges = edges[0]
        for e in edges:
            if (right is None or left is None):
                if e.to.type is charClass:
                    if e.cost >= 0:
                        right = e
                    else:
                        left = e
                else:
                    list.append(e)
        return list
    
    # Gets an ordered list of closest n edges
    def getNClosestMatches(self,n):
        return self.edgelist[:n]
    
    # Gets an ordered list of closest 1 edge
    def getClosestMatch(self):
        return self.edgelist[:1]
    
    # Print function for visualization
    def printNode(self):
        print "Character: " + self.focal.name
        print "Type: " + self.focal.typeId
        self.printEdges()
        print "\n"
    
    # Print function for visualization
    def printEdges(self):
        for e in self.edgelist:
            e.printEdge()

##############################################
# A directed edge to a comparison class match
class Edge(object):
    def __init__(self,t,cost):
        self.to = t
        self.cost = cost
        self.abscost = abs(cost)
    
    # Prints all pertainent edge information
    def printEdge(self):
        print "Edge to: " + self.to.name
        print "Cost: " + str(self.cost)

##############################################
# An instance of a matched character
class Match(object):
    def __init__(self,character,pos,type):
        # Unique identifier
        self.name = character + "-" + str(pos)
        # Character
        self.char = character
        # Character class
        self.type = type
        # Character class unique id
        self.typeId = type.id
        # Integer
        self.pos = pos
