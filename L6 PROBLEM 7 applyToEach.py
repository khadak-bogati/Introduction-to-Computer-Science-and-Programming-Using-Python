testList = [1, -4, 8, -9]
def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
    return L

print(applyToEach(testList, abs))

def addOne(s):
	return s + 1
print(applyToEach(testList, addOne))


def square(s):
	return s**2
print(applyToEach(testList, square))
