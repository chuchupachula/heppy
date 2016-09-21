
from ROOT import TRandom
#from heppy.utils.pdebug import pdebugger

rootrandom = TRandom()

def expovariate (a):
    x=rootrandom.Exp(1./a)
    #pdebugger.info( x)
    return x

def uniform (a, b):
    x=rootrandom.Uniform(a, b)
    #pdebugger.info( x)
    return x

def gauss (a, b):
    x= rootrandom.Gaus(a,b)
    #pdebugger.info( x)
    return x

def seed (s):
    global rootrandom
    rootrandom = TRandom(0xdeadbeef)
