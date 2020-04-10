# wow I hate this problem
# Not done

def fairFights(cSwords, dSwords, fairDiff):
    swordRange = [0, 0]
    addingSwordIndex = 0

    rangeDMax = 0
    rangeCMax = 0
    rangeDMin = 10**5+1
    rangeCMin = 10**5+1
    validRanges = 0
    isValidSwords = True
    while(isValidSwords):
        newCSword = cSwords[addingSwordIndex]
        newDSword = dSwords[addingSwordIndex]

        rangeCMax = max(rangeCMax, newCSword)
        rangeDMax = max(rangeDMax, newDSword)

        if(abs(rangeCMax - rangeDMax) > fairDiff):
            for i in range(swordRange[0], swordRange[1]+1):
                if cSwords[i] == rangeCMax:
                    # find new max of new swords
                    for c in range(i+1, swordRange[1]+1):
                        rangeCMax = max(rangeCMax, cSwords[c])

                if dSwords[i] == rangeDMax:
                    for d in range(i+1, swordRange[1]+1):
                        rangeDMax = max(rangeDMax, dSwords[d])

                if(abs(rangeCMax - rangeDMax) < fairDiff):
                    break
        
            swordRange[0] = i+1          
            swordRange[1] = i+1
        else: 
            swordRange[1] += 1



        addingSwordIndex += 1

    return



tests = int(input())

for test in range(0, tests):
    args = input().split()
    
    fairDiff = int(args[1])
    cSwords = (int for sword in input().split())
    dSwords = (int for sword in input().split())

    fairFights(cSwords, dSwords, fairDiff)

    print('Case #{}: {}'.format(test+1, fairFights(cSwords, dSwords, fairDiff)))