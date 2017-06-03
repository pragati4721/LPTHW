def printwo(*args):
    arg1,arg2 = args
    print "arg1: %r,arg2: %r"%(arg1,arg2)
def printwoag(arg1,arg2):
    print "arg1: %r,arg2: %r"%(arg1,arg2)
def printone(arg1):
    print "arg1: %r"%arg1
def printnon():
    print "I got nothin'."
printwo("Pragati","Singh")
printwoag("Pragati","Singh")
printone("Boom!")
printnon()
