def reverseDigits(num) :
	rev = 0
	while (num > 0) :
		rev = rev * 10 + num % 10
		num //= 10
		
	return rev

# To square number
def square(num) :
	return (num * num)
	
# To check Adam Number
def checkAdamNumber(num) :
	a = square(num)
	b = square(reverseDigits(num))
	if (a == reverseDigits(b)) :
		return True
	else :
		return False

num=int(input())
if (checkAdamNumber(num)) :
	print ("True")
else :
	print ("False")
	