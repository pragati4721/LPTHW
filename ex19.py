def candc(ccnt,boc):
    print "You have %d cheese!" % ccnt
    print "You have %d boxes of crackers!" % boc
    print "Man that's enough for a party!"
    print "Get a blanket.\n"
print "We can just give the function numbers directly:"
candc(20,30)
print "OR, we can use variables from our script:"
aoc =10
aocr=50
candc(aoc,aocr)
print "We can do math inside too:"
candc(10+20,5+6)
print "And we can combine the two, variables and math:"
candc(aoc+100,aocr+1000)
