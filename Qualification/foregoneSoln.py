def split(a):
    digit = 1
    b = 0
    while( a != 0 ):
        curDigit = a%10

        if( curDigit == 4):
            b += digit
        a = a//10
        digit *= 10
    
    return b

tests = int(input())

for test in range(0, tests):
    currentCheck = int(input())
    b = split(currentCheck)
    print('Case #' + str(test+1) + ": " + str(currentCheck-b) + " " + str(b))
