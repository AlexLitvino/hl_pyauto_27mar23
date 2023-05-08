"""
Object
  R
D   E
B   C
  A
"""

class R:
    def m(self):
        print("In R")


class D(R):
    def m(self):
        print("In D")


class E(R):
    def m(self):
        print("In E")

class B(D):
    def m(self):
        print("In B")

class C(E):
    def m(self):
        print("In C")

class A(B, C):
    def m(self):
        print("In A")

a = A()
a.m()

print(A.__mro__)

"""
MRO = A + merge(L(B), L(C), B, C) = A + merge(BDRO, CERO, B, C) = AB + merge(DRO, CERO, C) = ABD + merge(RO, CERO, C) = ABDC + merge(RO, ERO) = ABDCERO
L(B) = B + merge(L(D), D) = B + merge(DRO, D) = BD + merge(RO) = BDRO 
L(C) = C + merge(L(E), E) = C + merge(ERO, E) = CERO

L(D) = D + merge(L(R), R) = DRO
L(E) = E + merge(L(R), R) = ERO
"""

"""

D E
B C
A
"""
# class D: pass
# class E: pass
# class B(D, E): pass
# class C(E, D): pass
# class A(B, C): pass
#a = A()  # error

# o = object()
# print(dir(o))
