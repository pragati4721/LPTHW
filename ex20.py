from sys import argv
script,ifl = argv
def pntal(f):
    print f.read()
def rewind(f):
    f.seek(0)
def pal(lc,f):
    print lc,f.readline()
cf = open(ifl)
print "First let's print the whole file:\n"
pntal(cf)
print "Now let's rewind, kind of like a tape."
rewind(cf)
print "Let's print three lines"
cl = 1
pal(cl,cf)
cl+=1
pal(cl,cf)
cl+=1
pal(cl,cf)
