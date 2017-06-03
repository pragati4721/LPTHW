from sys import argv
from os.path import exists
script, fro,tof =argv
print "Copying from %s to %s"%(fro,tof)
inf = open(fro)
indata = inf.read()
print "The input file is %d bytes long"%len(indata)
print "Does the output file exists? %r"%exists(tof)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()
ouf = open(tof,'w')
ouf.write(indata)
print "Alright, all done."
ouf.close()
inf.close()
