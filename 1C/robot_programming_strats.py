def findProgram(strings, stringLengths, adv):
    indexTracker = [0 for i in range(adv)]

    winnerSequence = []

    for i in range(500):
        triggers = {
            'R': False,
            'P': False,
            'S': False
        }

        done = True
        for a in range(adv):
            if(indexTracker[a] == -1):
                continue
            # print(strings[a])
            done = False
            if( strings[a][indexTracker[a]] == 'R'):
                triggers['R'] = True
            elif( strings[a][indexTracker[a]] == 'P'):
                triggers['P'] = True
            elif( strings[a][indexTracker[a]] == 'S'):
                triggers['S'] = True

        if(done):
            return ''.join(winnerSequence)

        unique = 0
        # print(triggers)
        for rps in triggers:
            if triggers[rps]:
                unique+=1

        picked = ''
        if(unique == 1):
            if(triggers['P']):
                winnerSequence.append('S')
            elif(triggers['S']):
                winnerSequence.append('R')
            elif(triggers['R']):
                winnerSequence.append('P')
            return ''.join(winnerSequence)
        elif(unique == 2):
            if(triggers['P'] and triggers['R']):
                winnerSequence.append('P')
                picked = 'P'
            elif(triggers['S'] and triggers['P']):
                winnerSequence.append('S')
                picked = 'S'
            elif(triggers['R'] and triggers['S']):
                winnerSequence.append('R')
                picked = 'R'
        else:
            break

        for a in range(adv):
            if(indexTracker[a] == -1):
                continue
            # print(strings[a])
            if( strings[a][indexTracker[a]] == 'R' and picked == 'P'):
                indexTracker[a] = -1
            elif( strings[a][indexTracker[a]] == 'P' and picked == 'S'):
                indexTracker[a] = -1
            elif( strings[a][indexTracker[a]] == 'S' and picked == 'R'):
                indexTracker[a] = -1
            else:
                indexTracker[a] = (indexTracker[a]+1) % stringLengths[a]


    return 'IMPOSSIBLE'


tests = int(input())

for test in range(0, tests):
    args = int(input())
    strings = []
    stringLengths = []

    for i in range(args):
        program = input()
        strings.append(program)
        stringLengths.append(len(program))

    

    print('Case #{}: {}'.format(test+1, findProgram(strings, stringLengths, args)))