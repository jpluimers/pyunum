import sys
import unum_config
unum_config.e = 0
unum_config.f = 0
from unum import *
#import unum
print e
f = 0
print e
print u2g(5)
print view(x2u(5))
five = x2u(34.2)
print view(five)
def print_unum(u):
    print sign(u), expovalue(u), hidden(u), Fraction(frac(u), 2**fsize(u))
print_unum(five)
print frac(five), fsize(five)
print "numbits", numbits(five), "of", maxubits, fsize(five), "of", fsizemax, esize(five), "of", esizemax
print u2f(five)
print x2u(5)
print u2g(x2u(9005))
print plusg(u2g(x2u(34.2)), u2g(x2u(0)))
print 'times', u2f(x2u(34.2)), u2f(x2u(1))
print 'times', timesg(u2g(x2u(34.2)), u2g(x2u(1)))
print 'result', plusu(x2u(34.2), x2u(0))
print x2u(34.2), timesu(x2u(34.2), x2u(2))
print u2g(x2u(34.2)), u2g(timesu(divideu(x2u(34.2), x2u(2)), x2u(2)))
print u2g(squareu(x2u(-5)))
for i in range(0, 16):
    assert view(i) == view(g2u(u2g(i)))

for i in range(0,16):
    print bin(i), view(i)

for i in range(0,16):
    for j in range(0, 16):
        #print u2g(i), u2g(j)
        #print view(g2u(u2g(j)))
        print view(i) + " * " + view(j) + " = " + view(timesu(i, j))

for i in range(0,16):
    for j in range(0, 16):
        #print u2g(i), u2g(j)
        #print view(g2u(u2g(j)))
        print view(i) + " + " + view(j) + " = " + view(timesu(i, j))

for i in range(0,16):
    for j in range(0, 16):
        #print u2g(i), u2g(j)
        #print view(g2u(u2g(j)))
        print view(i) + " / " + view(j) + " = " + view(divideu(i, j))
