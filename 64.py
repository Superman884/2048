primes=[2]
for i in range(3,1000000):
	run=True
	for j in primes[0:len(primes)//2]:
		if i%j==0:
			run=False
			break
	if run:
		primes.append(i)
print(primes)