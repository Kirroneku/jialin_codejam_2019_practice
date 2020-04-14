def process_bits(robots, bits, cashierData):
    assIndex = 0
    lastBit = 0

    maxTime = 0
    over = False
    # Problem... We can distribute the problem in such a way
    # such each robot gets some
    for cashier in range(len(cashierData)):
        if( bits == 0):
            break
        if( bits <= cashierData[cashier]['max']):
            curTime = cashierData[cashier]['scanTime']*bits + cashierData[cashier]['processTime']
            over = True
            if( lastBit == 0):
                lastBit = curTime
            elif( curTime < lastBit):
                lastBit = curTime
        elif( over ):
            break  
        else:
            curTime = cashierData[cashier]['scanTime']*cashierData[cashier]['max'] + cashierData[cashier]['processTime']
            bits -= cashierData[cashier]['max']
            maxTime = max(curTime, maxTime)

        maxTime = max(lastBit, maxTime)
    return maxTime

tests = int(input())

for test in range(0, tests):
    args = [int(x) for x in input().split()]
    robots = args[0]
    bits = args[1]
    cashiers = args[2]

    cashierData = []
    for cashier in range(cashiers):
        c = [int(x) for x in input().split()]
        
        cashierData.append(
            {
                'max': c[0],
                'scanTime': c[1],
                'processTime': c[2],
                'avgProcessTime': (c[0]*c[1] + c[2])/c[0]
            }
        )

    cashierData = sorted(cashierData, key=lambda x: x['avgProcessTime'])
    print(cashierData)

    ans = process_bits(robots, bits, cashierData)

    print('Case #{}: {}'.format(test+1, ans))