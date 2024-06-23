# 200612
# Find the sum of all eleven primes that are both truncatable from left to right and right to left.

from math import ceil, sqrt

def getDigits(num):
	digits = []
	
	ten = 1
	while True:
		if(num/ten < 1):
			break
		ten = ten*10
		
	ten = ten/10
	while ten > 1e-1:
		digits.append(int(num/ten))
		num = num%ten
		ten = ten/10
		
	return digits


def getNum(digits):
	num = 0
	
	ten = 1
	for i in reversed(digits):
		num = num + ten*i
		ten = ten*10
		
	return num

def isPrime(num):
	for i in range(2, ceil(sqrt(num))):
		if(num%i == 0):
			return False
			
	if(sqrt(num) == int(sqrt(num))):
		return False
	return True

count = 0
n = 11
suma = 0

while count < 11:
	digits = getDigits(n)
	cond = True
	while digits:
		if(not(isPrime(getNum(digits)))):
			cond = False
			break
		dumb = digits.pop(0)
	
	digits = getDigits(n)
	while digits:
		if(not(isPrime(getNum(digits)))):
			cond = False
			break
		dumb = digits.pop(-1)
	
	if(cond):
		count = count + 1
		suma = suma + n
		print(count, n, suma)
	
	n = n + 2
