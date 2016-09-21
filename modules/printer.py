import time
import datetime
# Decorator class for print statements
class log(object):
    def __init__(self,args):
        '''Comment out the next three lines to stop logging'''
        ts = time.time()
        print(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'), end='\t')
        print(args)