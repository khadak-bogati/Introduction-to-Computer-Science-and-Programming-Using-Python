num = int(input("please inter your Number: "))
if num < 0:
	isNeg = True
	num = abs(num)
else:
	isNeg = False
	result = ''
if num > 0:
	result = '0'
while num > 0:
	result = str(num%2) + result
	num = num//2
if isNeg:
	result = '- ', + result
print(result)

===================================================================================




x = float(input('Enter a decimal number between 0 and 1: '))
p = 0
while ((2**p)*x)%1 !=0:
	print('Remainder = ' + str((2**p)*x - int((2**p)*x)))
	p += 1
num = int(x*(2**p))

result = ''
if num == 0:
	result = '0'
while num > 0:
	result = str(num%2)+ result
	num = num//2

for i in range(p - len(result)):
	result = '0' + result
result = result[0:-p] + '.' + result[-p:]
print("Then binary representation of the decimal" +str(x))
