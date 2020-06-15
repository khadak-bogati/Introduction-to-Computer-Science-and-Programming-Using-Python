excercise :1 
x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <=x:
	if abs(guess**2 - x) < epsilon:
		break
	else:
		guess += step
if abs(guess**2 -x) >= epsilon:
	print("Faild")
else:
	print("succeded: ", str(guess))
  
  
  output:
  succeded:  4.999999999999998
  
  
  
  
  ------------------------------------------------------------------------------------------------------------------------
  excersie :2
  
  x = 25
epsilon = 0.01
step = 0.1
guess = 0.0


while abs(guess**2 -x) <= x:
	if guess <=x:
		guess += step
	else:
		break
if abs(guess**2 -x) >= epsilon:
	print("Faild")
else:
	print("Succeeded: " +str(guess))
  
  
  output
  =====================
  Faild
  
