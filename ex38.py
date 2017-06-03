tt = "Apples Oranges Crows Telephone Light Sugar"
print "Wait thre's not 10 things in that list ,let's fix that."
st = tt.split(' ')
ms=["Day","Night","Song","Frisbee","Corn","Banana","Girl","Boy"]
while len(st) !=10:
    no = ms.pop()
    print "Adding: ",no
    st.append(no)
    print "There is %d items now."%len(st)
print "There we go: " , st
print "Let's do some things with stuff."
print st[1]
print st[-1]
print st.pop()
print ' '.join(st)
print '#'.join(st[3:5])
