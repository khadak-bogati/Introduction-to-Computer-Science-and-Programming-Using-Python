eplsion = 0.01
y = 24
newguess = 0
guess = y/2.0

while abs(guess*guess -y )>= eplsion:
	newguess += 1
	guess = guess - (((guess**2) - y) /(2*guess))
print("newguess = " + str(newguess))
print("Square root of " + str(y) + 'is about ' + str(guess))

===========================================================
output
.......................
newguess = 4
Square root of 24is about 4.8989887432139305



======================================================================
from math import sqrt

print("Quadratic function: (a *x^2) +b*x +c" )
a = float(input("a: "))
b= float(input("b: "))
c = float(input("c: "))



r = b**2 - 4*a*c

if r > 0:
	num_roots = 2
	x1 = (((-b) + sqrt(r))/(2*a))
	x2 = (((-b) - sqrt(r))/ (2*a))
	print("There are 2 roots: %f and %f " %(x1, x2))
elif r == 0:
	num_roots = 1
	x = (-b) /2*a
	print("There is one root: ",x )
else:
	num_roots = 0
	print("No roots, discriminant < 0")
	exit()
