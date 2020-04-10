def findCuts(col, row, vGroups, hGroups, vLimit, hLimit):
    vCuts = []
    hCuts = []

    cGroup = 0
    for c in range(len(col)):
        
        cGroup += col[c]
        if( cGroup > vGroups ):
            return []
        elif( cGroup == vGroups):
            cGroup = 0
            vCuts.append(c + 1)
            if( vLimit == len(vCuts)):
                break

    rGroup = 0
    for r in range(len(row)):
        rGroup += row[r]
        if( rGroup > hGroups ):
            return []
        elif( rGroup == hGroups):
            rGroup = 0
            hCuts.append(r + 1)
            # print(hCuts)
            if( hLimit == len(hCuts)):
                break

    vCuts.append(len(col))
    hCuts.append(len(row))

    return [vCuts, hCuts]

def verifyCuts(waffle, vCuts, hCuts, chipsInSection):

    lastVCut = 0
    lastHCut = 0
    for vCut in vCuts:
        for hCut in hCuts:
            sectionChips = 0
            # print(vCut, hCut)
            for c in range(lastVCut, vCut):
                for r in range(lastHCut, hCut):
                    # print(r, c)
                    if(waffle[r][c] == '@'):
                        sectionChips += 1

            if(sectionChips != chipsInSection):
                return False

            lastHCut = hCut
        lastHCut = 0
        lastVCut = vCut

    return True

tests = int(input())

for test in range(0, tests):
    args = [int(i) for i in input().split()]

    r = args[0]
    c = args[1]    
    hcutslimit = args[2]
    vcutslimit = args[3]

    
    chipInRows = []
    chipInColoums = []
    totalChips = 0

    waffle = []

    for i in range(r):
        row = input()
        r = []
        for char in row:
            r.append(char)
        waffle.append(r)
    # print(waffle)
    for row in waffle:
        chipInRow = 0
        for char in row:
            if(char == '@'):
                chipInRow += 1
                totalChips+= 1
        chipInRows.append(chipInRow)

    for i in range(c):
        chipInCol = 0
        for row in waffle:
            if( row[i] == '@'):
                chipInCol += 1
                
        chipInColoums.append(chipInCol)

    cuts = [[]]
    if totalChips%((vcutslimit+1)*(hcutslimit+1)) == 0:
        cuts = findCuts(chipInColoums, chipInRows, totalChips/(vcutslimit+1), totalChips/(hcutslimit+1), vcutslimit, hcutslimit)
        if(cuts and verifyCuts(waffle, cuts[0], cuts[1], totalChips/((vcutslimit+1)*(hcutslimit+1)))):
            print('Case #{}: {}'.format(test+1, "POSSIBLE"))
        else:
            print('Case #{}: {}'.format(test+1, "IMPOSSIBLE"))
    else:
        print('Case #{}: {}'.format(test+1, "IMPOSSIBLE"))