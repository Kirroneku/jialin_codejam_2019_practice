def canDefend(armor, damageString):
    shoots = 0
    for char in damageString:
        if(char == 'S'):
            shoots += 1

    if( armor < shoots ):
        return -1

    swaps = 0
    damageArray = []
    for char in damageString:
        damageArray.append(char)

    damage = evalDamage(damageString)

    while( armor < damage ):
        for i in range(len(damageArray)-cAtEnd(damageArray)-1, -1, -1):
            if(damageArray[i] == 'C' and damageArray[i+1] == 'S'):
                damageArray[i+1] = 'C'
                damageArray[i] = 'S'
                swaps += 1
        damage = evalDamage(''.join(damageArray))

    return swaps

def evalDamage(damageString):
    currentDamage = 1
    totalDamage = 0
    for char in damageString:
        if(char == 'S'):
            totalDamage += currentDamage
        else:
            currentDamage *= 2

    return totalDamage

def cAtEnd(damageString):
    endC = 0
    i = len(damageString) - 1
    while( i > 0 and damageString[i] == 'C'):
        i -= 1
        endC += 1

    return endC


tests = int(input())

for test in range(0, tests):
    args = input().split()
    defenseVal = int(args[0])
    damageString = args[1]

    defense = canDefend(defenseVal, damageString)

    if( defense == -1 ):
        defense = "IMPOSSIBLE"
    else:
        defense = str(defense)

    print('Case #' + str(test+1) + ': ' + defense)