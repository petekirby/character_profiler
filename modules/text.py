import threading
import codecs
from printer import log
from node import *
import gc

## TextHandler handles all text metadata ##
class TextHandler(object):
    def __init__(self,path,parsehandler):
        self.parsehandler = parsehandler
        self.path = path
        self.id = path.split("/").pop().split(".")[0]
        splittext = path.split("/").pop().split("_")
        # Fields that parse for organization
        self.era = splittext[0]
        self.genre = splittext[1]
        self.genreNum = int(splittext[2])
        self.name = splittext[3]
        self.file = None
        self.charnum = 0
        # Nodes
        self.nodes = []
        # Profiles
        self.profiles = []
    
    # Makes each non-ignore character-phrase into a node
    # For example, a three-character phrase is one node
    def nodify(self):
        ignores = self.parsehandler.ignore.chars
        classes = self.parsehandler.classes
        file = codecs.open(self.path,encoding='utf-8')
        log("Generating nodes for " + self.id)
        # Position in file
        pos = 0
        node_handler = NodeHandler(self.parsehandler)
        # Disable garbage collector while looping
        gc.disable()
        while True:
            # we read the entire file one character at at time
            s = file.read(1)
            current = s
            # If not current, we've hit the end of the file
            if not current:
                break
            # only continue (i.e., increment the count, etc)
            # if we aren't ignoring this character
            if (current in ignores):
                continue
            pos = pos + 1
            not_found = True
            for node in node_handler.queue:
                node.ignore = False
            for cc in classes:
                for key in cc.chars:
                    index = 0
                    for char in key:
                        if current == char:
                            not_found = False
                            node_handler.add(Node(current,cc,pos,key),index)
                        index += 1
            if not_found:
                node_handler.queue = []
        self.nodes = node_handler.nodes[:]
        file.close()
        self.charnum = pos
        gc.enable()
        log("\tThere were " + str(self.charnum) +
              " characters, and " + str(len(self.nodes)) + " nodes.")

    def generateProfile(self,focal,compare,stopword,delim,maxcost=120):
        focals = []
        compares = []
        delims = []
        sentence = 0
        stops = 0
        sentence_length = 0
        # Sort the nodes into their correct categories
        for n in self.nodes[:]:
            if n.cc == focal:
                focals.append(Node(n.char,n.cc,n.pos - stops,n.key,sentence))
            elif n.cc == stopword:
                stops += 1
            elif n.cc == delim:
                stops += 1
                delims.append(Node(n.char,n.cc,n.pos - stops,n.key,sentence))
                sentence += 1
            elif n.cc == compare:
                compares.append(Node(n.char,n.cc,n.pos - stops,n.key,sentence))
        n = self.nodes[-1]
        if (delims[-1].pos < n.pos - stops):
            delims.append(Node(n.char,n.cc,n.pos - stops,n.key,sentence))
        p = NodeProfile(focals,compares,delims,focal,compare,stopword,delim,maxcost)
        self.profiles.append(p)     
