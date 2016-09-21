#import unittest
#from text import *
#from console import *
#
#class Tester(unittest.TestCase):
#    def setUp(self):
#        self.p = ParseHandler()
#        self.p.setTextDirectory("/Users/bucci/dev/CorrelationProfiler/texts/")
#        self.p.loadAllTexts()
#
#    def test_classes(self):
#        self.assertEquals(len(self.p.classes), 14)

#    def test_nodes(self):
#        nodes = self.p.texts[0].nodes
#        for n in nodes:
#            print n.char

#        self.assertEquals(nodes[0].cc.id, "t_consonants" )
#        self.assertEquals(nodes[1].char, "stop")
#
#def sort(list):
#    if len(list) < 2:
#        return list
#    else:
#        sort(list[min:mid])
#        sort(list[)
#

#if __name__ == '__main__':
#    sort((1,6,7,2,130,22,1,5,5,228,12,91,400))
#    unittest.main()

