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

    def is_not_focal(self, pos, focal, lo=0, hi=None):
        if hi is None:
            hi = len(self.nodes)
        while lo < hi:
            mid = (lo + hi) // 2
            if (self.nodes[mid].pos < pos):
                lo = mid + 1
            else:
                hi = mid
        while lo < len(self.nodes) and self.nodes[lo].pos == pos:
            if self.nodes[lo].cc == focal:
                return False
            lo += 1
        return True

    def generateProfile(self,focal,compare,stopword,delim,maxcost=120):
        focals = []
        compares = []
        delims = []
        sentence = 0
        stops = 0
        blocked_positions = []
        # Determine the blocked positions (not focal/compare) from the 'stopwords'
        for n in self.nodes[:]:
            if n.cc == stopword:
                for position in range(n.pos, n.getRight() + 1):
                    blocked_positions.append(position)
        blocked_position_set = frozenset(blocked_positions)
        # Sort the nodes into their correct categories
        for n in self.nodes[:]:
            if n.cc == focal:
                if n.pos not in blocked_position_set and n.getRight() not in blocked_position_set:
                    focals.append(Node(n.char,n.cc,n.pos - stops,n.key,sentence))
            # elif n.cc == stopword:
            #   decided not to consider 'stopwords' for this purpose
            #   'stopwords' act as a mechanism for blocking words from being focal/compare words
            #   stops += 1
            elif n.cc == delim:
                stops += 1
                delims.append(Node(n.char,n.cc,n.pos - stops,n.key,sentence))
                sentence += 1
            elif n.cc == compare:
                if n.pos not in blocked_position_set and n.getRight() not in blocked_position_set:
                    if self.is_not_focal(n.pos, focal):
                        compares.append(Node(n.char,n.cc,n.pos - stops,n.key,sentence))
        n = self.nodes[-1]
        if (delims[-1].pos < n.pos - stops):
            delims.append(Node(n.char,n.cc,n.pos - stops,n.key,sentence))
        p = NodeProfile(focals,compares,delims,focal,compare,stopword,delim,maxcost)
        self.profiles.append(p)     
