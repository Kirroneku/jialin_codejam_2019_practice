import time

def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

def decrypt_cryptopangram( values ):
    primes = []
    primeListSize = 1

    messageEncrypted = []
    messageUnencrypted = []

    # We need to skip to one that doesnt repeat...
    # get first in between gcd to find the 2nd prime
    between = gcd(values[0], values[1])
    # first prime
    messageEncrypted.append(values[0]//between)
    messageEncrypted.append(between)
    lastPrime = between
    
    primes.append(values[0]//between)
    if primes.count(lastPrime) == 0:
        primes.append(lastPrime)
        ++primeListSize

    for i in range(1, length):
        currentValue = values[i]//lastPrime
        if primeListSize < 26 and primes.count(currentValue) == 0:
            primes.append(currentValue)
            ++primeListSize
            
        messageEncrypted.append(currentValue)
        lastPrime = currentValue
        
    primes.sort()
    primeDictionary = {}

    for char in range(0, len(primes)):
        primeDictionary[primes[char]] = chr(ord('A') + char)

    for prime in messageEncrypted:
        messageUnencrypted.append(primeDictionary[prime])

    return ''.join(messageUnencrypted)

tests = int(input())

for test in range(0, tests):
    length = int(input().split()[1])
    noOfValues = input()
    noOfValues = noOfValues.split(' ')
    values = []
    
    for value in range(0, len(noOfValues)):
        values.append(int(noOfValues[value]))
    
    print('Case #' + str(test+1) + ": " + decrypt_cryptopangram(values))

###
# Test case 
#
# 2
# 103 32
# 217 1891 4819 2291 2987 3811 1739 2491 4717 445 65 1079 8383 5353 901 187 649 1003 697 3239 7663 291 123 779 1007 3551 1943 2117 1679 989 3053 5041
# 10000 25
# 3292937 175597 18779 50429 375469 1651121 2102 3722 2376497 611683 489059 2328901 3150061 829981 421301 76409 38477 291931 730241 959821 1664197 3057407 4267589 4729181 5335543
###
