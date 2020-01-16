from math import sqrt
import sys
import time

def roundBytes(numIn, sigFigs = 0):
	num = numIn
	suffixes = ["B", "KiB", "MiB", "GiB", "TiB"]
	index = 0
	while num > 1024 and index < 4:
		num /= 1024
		index += 1
	return str(round(num, sigFigs)) + " " + suffixes[index]


primes = [2]
isPrime = True
maxNum = 10000000
print("Generating primes between 1 and " + str(maxNum) + "...")
startTime = time.perf_counter()
for i in range(3, maxNum, 2):
	sqrtI = sqrt(i)
	for j in primes:
		if i % j == 0:
			isPrime = False
			break
		elif j >= sqrtI:
			break
	if(isPrime):
		#print(i)
		primes.append(i)
	isPrime = True
endTime = time.perf_counter() - startTime
print("\n" + str(len(primes)) + " Primes between 1 and " + str(maxNum))
print("Size of List: " + roundBytes(sys.getsizeof(primes), 2))
print("Elapsed time: " + str(round(endTime,2)) + " seconds")
#f = open("primes.txt", "w")
#f.write(str(primes))
input()