print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explaination
\n\twhere there is none.
"""
print "-"*10
print poem
print "-"*10
five = 10 - 2 + 3 - 6
print "This should be five: %s"% five
def sf(a):
    jb = a*500
    ja = jb/1000
    cr = ja/100
    return jb,ja,cr
sp = 10000
bn,jr,ct = sf(sp)
print "With a stsrting point of %d"%sp
print "We'd have %d beans, %d jars, and %d crates."%(bn,jr,ct)
sp/=10
print "We can also do this way:"
print "We'd have %d beans, %d jars, and %d crates."%sf(sp)
