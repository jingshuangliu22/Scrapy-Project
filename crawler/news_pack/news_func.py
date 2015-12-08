import time

def ListCombiner(lst):
    string = ''
    for e in lst:
        string += e
    return string

def GetDate():
    string = time.strftime('%Y%m%d',time.localtime(time.time()))
    return string
