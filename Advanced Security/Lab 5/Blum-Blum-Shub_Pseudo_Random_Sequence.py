import random
from fractions import gcd as bltin_gcd
import math
import numpy

def main():
    length = int(raw_input("Enter how long of a sequence is required: "))

    primeSequence = primes_sieve(2000000)

    p, q = getPrimes(primeSequence)

    M = p * q

    seed = random.randint(2, M - 1)
    while (coprime2(M, seed) != True or seed == p or seed == q):
        seed = random.randint(2, M - 1)

    sequence = []
    n = 0
    while(n != length):
        #Appen least signicant byte of current seed to sequence
        sequence.append(seed & 0xFF)

        seed = (seed ** 2) % M
        n += 1

    print("The generated random sequence is: " + str(sequence))

    print("Running entropy tests\n")

    arithmeticMean(sequence)

    monobitTest(sequence)

def arithmeticMean(sequence):
   mean = numpy.mean(sequence)
   if (mean < 140 and mean > 120):
       print("The arithmetic mean of the sequence is; " + str(mean) + " indicating that the data is close to random")
   else:
       print("The arithmetic mean of the sequence is: " + str(mean) + " indicating that the data is not random")

def monobitTest(sequence):
    byteSum = ''

    for i in sequence:
        byteSum += bin(i)[2:]

    oneCount = 0
    zeroCount = 0

    for i in byteSum:
        if(i == '1'):
            oneCount += 1
        else:
            zeroCount += 1

    Sn = abs(zeroCount - oneCount)
    Sobs = Sn / (math.sqrt(len(byteSum)))
    Pvalue = math.erfc(Sobs / math.sqrt(2))

    print("PValue is: " + str(Pvalue))
    if Pvalue < 0.01:
        print('Monobit test indicates that the sequence is non-random')
    else:
        print('Monobit test indicates that the sequence is random')

def getPrimes(primeSequence):
    p = random.choice(primeSequence)
    q = random.choice(primeSequence)

    while(p == q):
        q = random.choice(primeSequence)

    while (p % 4 != 3):
        p = random.choice(primeSequence)
    while (q % 4 != 3):
        q = random.choice(primeSequence)
    return (p, q)

def coprime2(a, b):
    return bltin_gcd(a, b) == 1

def primes_sieve(limit):
    limitn = limit+1
    not_prime = set()
    primes = []

    for i in range(2, limitn):
        if i in not_prime:
            continue

        for f in range(i*2, limitn, i):
            not_prime.add(f)

        primes.append(i)

    return primes


if __name__ == "__main__":
    main()