import math
class Vector(object):
    """docstring for Vector."""
    def __init__(self,arg):
        self.vec = arg
    def add(self,arg):
        if len(self.vec) != len(arg.vec):
            print "Not possible"
        else :
            self.total = []
            for i in range(0,len(self.vec)):
                self.total.append(self.vec[i] + arg.vec[i])
            print self.total
    def subtract(self,arg):
        if len(self.vec) != len(arg.vec):
            print "Not possible"
        else :
            self.total = []
            for i in range(0,len(self.vec)):
                self.total.append(self.vec[i] - arg.vec[i])
            print self.total
    def norm(self):
        self.total = 0
        for i in range(0,len(self.vec)):
            self.total+=self.vec[i]**2
        print math.sqrt(self.total)
    def dot(self,arg):
        if len(self.vec) != len(arg.vec):
            print "Not possible"
        else :
            self.total = 0
            for i in range(0,len(self.vec)):
                self.total+=(self.vec[i]*arg.vec[i])
            print self.total
a = Vector([7,5,3])
b = Vector([4,5,6])
c = a.add(b)
b.norm()
d = a.subtract(b)
e = a.dot(b)
