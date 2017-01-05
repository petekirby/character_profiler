from printer import log
import gc
import sys
import collections
#
class NodeHandler(object):
    def __init__(self,parsehandler):
        self.parsehandler = parsehandler
        # One-item queue
        self.queue = []
        self.nodes = []
    
    # Check before appending to nodes
    def add(self,new,index):
        if new.char == new.key:
            self.nodes.append(new)
        else:
            if new.char == new.key[0] and index == 0:
                new.ignore = True
                self.queue.append(new)
            else:
                temp_queue = []
                while self.queue != []:
                    node = self.queue.pop()
                    if new.char == node.next_char() and node.ignore == False:
                        node.char += new.char
                        node.ignore = True
                        temp_queue.append(node)
                    elif node.ignore == True:
                        temp_queue.append(node)
                    else:
                        pass
                for node in temp_queue:
                    if node.char == node.key:
                        self.nodes.append(node)
                    else:
                        self.queue.append(node)


# All pertinent characters in a text are represented
# as nodes.
class Node(object):
    def __init__(self,char,cc,pos,key,sent=0):
        self.sentence = sent
        self.pos = pos
        self.cc = cc
        self.char = char
        self.key = key
        self.edge_count = {}
        self.id = self.key + "_" + str(self.pos)

    def next_char(self):
        i = len(self.char)
        if i < len(self.key):
            char = self.key[i]
            return char
        else:
            return None

    # Get right position for multi-character nodes
    def getRight(self):
        rpos = self.pos + len(self.char) - 1
        return rpos

    # Prints all of the good info about a node
    def printNode(self):
        log("\t#### Node ####")
        log("\tClass: " + self.cc.id)
        log("\tKey: " + self.key)


class NodeProfile(object):
    def __init__(self,focals,compares,delims,focal,compare,stopword,delim,maxcost):
        self.focals = focals
        self.compares = compares
        self.delims = delims
        self.focal = focal
        self.compare = compare
        self.stopword = stopword
        self.delim = delim
        self.maxcost = maxcost
        self.costs = [maxcost, 10, 5, 2, 1]
        self.edge_count = {}
        self.contingency = {}
        self.id = (focal.id + "_" + compare.id + "_" +
                   stopword.id + "_" + delim.id + "_" + str(maxcost))
        gc.disable()
        self.generate_edges()
        self.generate_contingency_table()
        gc.enable()
        self.compare_count = len(compares)
        self.focal_count = len(focals)
        self.node_count = self.delims[-1].pos + 1
        self.sentence_count = len(self.delims)
        self.focals = []
        self.compares = []
        self.delims = []

    def search_after_position(self,nodes,needle,lo=0,hi=None):
        if hi is None:
            hi = len(nodes)
        while lo < hi:
            mid = (lo + hi) // 2
            if (nodes[mid].pos < needle):
                lo = mid + 1
            else:
                hi = mid
        return lo

    def search_after_sentence(self,nodes,needle,lo=0,hi=None):
        if hi is None:
            hi = len(nodes)
        while lo < hi:
            mid = (lo + hi) // 2
            if (nodes[mid].sentence < needle):
                lo = mid + 1
            else:
                hi = mid
        return lo

    def generate_edges(self):
        for f in self.focals:
            # find all comparisons within certain distance, add to edge count for distance
            start_pos_value = f.pos - self.maxcost
            # print('working on start_pos_value ' + str(start_pos_value))
            i = self.search_after_position(self.compares,start_pos_value)
            while i < len(self.compares):
                dist = abs(f.pos - self.compares[i].pos)
                i += 1
                # print('comparing at dist ' + str(dist))
                if dist > self.maxcost:
                    break
                if dist == 0:
                    continue
                f.edge_count[str(self.maxcost)] = f.edge_count.get(str(self.maxcost), 0) + 1
                for cost in self.costs[1:]:
                    if dist <= cost:
                        f.edge_count[str(cost)] = f.edge_count.get(str(cost), 0) + 1
            # find all comparisons in same sentence, add to edge count for sentence
            i = self.search_after_sentence(self.compares,f.sentence)
            while i < len(self.compares) and self.compares[i].sentence == f.sentence:
                if f.pos != self.compares[i].pos:
                    f.edge_count["sentence"] = f.edge_count.get("sentence", 0) + 1
                i += 1
            # update edge count totals
            for cost in self.costs:
                self.edge_count[str(cost)] = self.edge_count.get(str(cost), 0) + f.edge_count.get(str(cost), 0)
            self.edge_count['sentence'] = self.edge_count.get('sentence', 0) + f.edge_count.get('sentence', 0)

    def generate_contingency_table(self):
        # we want to calculate the total number of words that are within distance of the compares
        # we can subtract the numbers for the focals to get the nubmers for the rest
        total_pos = {}
        total_neg = {}
        focal_pos = {}
        focal_neg = {}
        last_position = self.delims[-1].pos
        pos = self.compares[0].pos if len(self.compares) > 0 else -1
        for c in self.compares[1:]:
            dist = c.pos - pos - 1
            for cost in self.costs:
                if dist <= 2 * cost:
                    total_pos[str(cost)] = total_pos.get(str(cost), 0) + dist
                else:
                    total_pos[str(cost)] = total_pos.get(str(cost), 0) + 2 * cost
                    total_neg[str(cost)] = total_neg.get(str(cost), 0) + dist - 2 * cost
            pos = c.pos
        # adjust for the beginnings and ends
        for cost in self.costs:
            if len(self.compares) >= 1:
                start_end_distances = [self.compares[0].pos, last_position - self.compares[-1].pos]
                for dist in start_end_distances:
                    if dist <= cost:
                        total_pos[str(cost)] = total_pos.get(str(cost), 0) + dist
                    else:
                        total_pos[str(cost)] = total_pos.get(str(cost), 0) + cost
                        total_neg[str(cost)] = total_neg.get(str(cost), 0) + dist - cost
            else:
                total_neg[str(cost)] = last_position + 1
        # get sentence totals
        pos = -1
        i = 0
        for d in self.delims:
            if i < len(self.compares) and self.compares[i].sentence == d.sentence:
                total_pos['sentence'] = total_pos.get('sentence', 0) + d.pos - pos
            else:
                total_neg['sentence'] = total_neg.get('sentence', 0) + d.pos - pos
            while i < len(self.compares) and self.compares[i].sentence == d.sentence:
                total_pos['sentence'] -= 1
                i += 1
            pos = d.pos
        # get the numbers for the focal words
        for f in self.focals:
            for cost in self.costs:
                focal_pos[str(cost)] = focal_pos.get(str(cost), 0) + (1 if f.edge_count.get(str(cost), 0) > 0 else 0)
                focal_neg[str(cost)] = focal_neg.get(str(cost), 0) + (1 if f.edge_count.get(str(cost), 0) == 0 else 0)
            focal_pos["sentence"] = focal_pos.get("sentence", 0) + (1 if f.edge_count.get("sentence", 0) > 0 else 0)
            focal_neg["sentence"] = focal_neg.get("sentence", 0) + (1 if f.edge_count.get("sentence", 0) == 0 else 0)
        # store the contingency table
        for cost in self.costs:
            self.contingency["{:02}".format(cost) + '_other_pos'] = total_pos.get(str(cost), 0) - focal_pos.get(str(cost), 0)
            self.contingency["{:02}".format(cost) + '_other_neg'] = total_neg.get(str(cost), 0) - focal_neg.get(str(cost), 0)
            self.contingency["{:02}".format(cost) + '_focal_pos'] = focal_pos.get(str(cost), 0)
            self.contingency["{:02}".format(cost) + '_focal_neg'] = focal_neg.get(str(cost), 0)
        self.contingency['sentence_other_pos'] = total_pos.get('sentence', 0) - focal_pos.get('sentence', 0)
        self.contingency['sentence_other_neg'] = total_neg.get('sentence', 0) - focal_neg.get('sentence', 0)
        self.contingency['sentence_focal_pos'] = focal_pos.get('sentence', 0)
        self.contingency['sentence_focal_neg'] = focal_neg.get('sentence', 0)

    def printProfile(self):
        log("\n#### Profile ####")
        log("Focals: " + self.focal.id)
        log("Compares: " + self.compare.id)
        for k,v in self.edge_count.items():
            print('Edge count (' + str(k) + '): ' + str(v))
        for k,v in self.contingency.items():
            print('Contingency table (' + str(k) + '): ' + str(v))

    def countColocations(self, abscost):
        return self.edge_count.get(str(abscost), 0)

    def countAllInSentence(self):
        return self.edge_count.get('sentence', 0)

    def countNodes(self):
        return self.node_count

    def countSentences(self):
        return self.sentence_count

    def getAverageSentence(self):
        return countNodes() / countSentences()

    def countFocalEdges(self):
        return self.edge_count.get(str(self.maxcost), 0)


# A set of characters with a unique identifier
class CharacterClass(object):
    def __init__(self,id,chars):
        # a string identifier such as "gods" or "delimiters"
        self.id = id
        # A list of character-phrases
        # Each with one or more character
        self.chars = chars
