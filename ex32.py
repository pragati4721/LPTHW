tc = [1,2,3,4,5]
fr = ['apples','oranges','pears','apricots']
ch = [1,'pennies',2,'dimes',3,'quarters']
for num in tc:
    print "This is count %d"%num
for f in fr:
    print "A fruit of type: %s" % f
for i in ch:
    print "I got %r"% i
el = []
for i in range(0,6):
    print "Adding %d to the list."% i
    el.append(i)
for i in el:
    print "Elements was: %d" % i
