import sys

args = input().split()
tests = int(args[0])

for test in range(0, tests):   
    myString = []

    checkLetters = {
        'A': 0,
        'B': 0,
        'C': 0,
        'D': 0,
        'E': 0
    }

    figureSet = {
        'A': [],
        'B': [],
        'C': [],
        'D': [],
        'E': []
    }

    for i in range(119):
        print(str(int((i*5)+1)))
        # print(i+1)
        getLtr = input()
        
        # print(getLtr)
        figureSet[getLtr].append(int(i*5+2))
    
    nextCheck = []
    for figure in figureSet:
        if( len(figureSet[figure]) == 23):
            nextCheck = figureSet[figure].copy()
            myString.append(figure)
            checkLetters[figure] = 1
            break

    figureSet = {
        'A': [],
        'B': [],
        'C': [],
        'D': [],
        'E': []
    }

    for i in nextCheck:
        print(i)
        getLtr = input()
        figureSet[getLtr].append(i+1)


    nextCheck = []
    for figure in figureSet:
        if( len(figureSet[figure]) == 5 and checkLetters[figure] == 0):
            nextCheck = figureSet[figure].copy()
            myString.append(figure)
            checkLetters[figure] = 1
            break

    figureSet = {
        'A': [],
        'B': [],
        'C': [],
        'D': [],
        'E': []
    }

    for i in nextCheck:
        print(i)
        getLtr = input()
        figureSet[getLtr].append(i+1)

    nextCheck = []
    for figure in figureSet:
        if( len(figureSet[figure]) == 1 and checkLetters[figure] == 0):
            nextCheck = figureSet[figure].copy()
            myString.append(figure)
            checkLetters[figure] = 1
            break

    figureSet = {
        'A': [],
        'B': [],
        'C': [],
        'D': [],
        'E': []
    }

    for i in nextCheck:
        print(i)
        getLtr = input()
        figureSet[getLtr].append(i+1)

    for figure in figureSet:
        if( len(figureSet[figure]) == 0 and checkLetters[figure] == 0):
            myString.append(figure)
            checkLetters[figure] = 1
            break

    for char in myString:
        checkLetters[char] = 1

    for letter in checkLetters:
        if( checkLetters[letter] == 0):
            myString.append(letter)
            break
        
    # sys.stderr.write(''.join(myString) + '\n')
    print(''.join(myString))

    ans = input()
    if( ans == 'N'):
        break
    # print('Case #{}: {}'.format(test+1))