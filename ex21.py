def add(a,b):
    print "ADDING %d +%d" %(a,b)
    return a+b
def sub(a,b):
    print "SUBTRACTING %d - %d"%(a,b)
    return a-b
def mul(a,b):
    print "MULTIPLYING %d * %d"%(a,b)
    return a * b
def div(a,b):
    print "DIVIDING %d / %d"%(a,b)
    return a / b
print "Let's do some math with just functions!"
age = add(30,5)
height = sub(78,4)
weig = mul(90,2)
iq = div(100,2)
print "Age: %d, Height: %d, Weight: %d, IQ: %d"%(age,height,weig,iq)
print "Here's a puzzle."
what = add(age,sub(height,mul(weig,div(iq,2))))
print "That becomes: ",what,"Can you do it by hand?"
