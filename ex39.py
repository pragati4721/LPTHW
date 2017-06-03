st = {'Oregon':'OR','Florida':'FL','California':'CA','New York':'NY','Michigan':'MI'}
ci = {'CA':'San Francisco','MI':'Detroit','FL':'Jacksonville'}
ci['NY'] = 'New York'
ci['OR'] = 'Portland'
print '-'*10
print "NY State has: ",ci['NY']
print "OR State has: ",ci['OR']
print '-'*10
print "Michigan's abbreviation is: ",st['Michigan']
print "Florida's abbreviation is: " ,st['Florida']
print '-'*10
print "Michigan has: ",ci[st['Michigan']]
print "Florida has: ",ci[st['Florida']]
print '-'*10
for s,ab in st.items():
    print "%s is abbreviated as %s"%(s,ab)
print '-'*10
for ab,c in ci.items():
    print "%s has the city %s"%(ab,c)
print '-'*10
for s,ab in st.items():
    print "%s state is abbreviated %s and has city %s"%(s,ab,ci[ab])
print '-'*10
s = st.get('Texas',None)
if not s:
    print "Sorry, no Texas."
c = ci.get('TX','Does not exist')
print "The city for the state 'TX' is %s"%c
