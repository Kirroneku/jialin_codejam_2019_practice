import random
import copy

def findPath(r, c):
    # grid
    matrix = [[{'neighbours': r+c-2, 'visited': False} for i in range(c)] for j in range(r)]
    for j in range(r):
        for i in range(c):
            for o in range(1, max(r,c)):
                if( j+o < r and o+i < c):
                    (matrix[j+o][o+i])['neighbours'] += 1
                if( j - o >= 0 and i - o >= 0):
                    (matrix[j-o][i-o])['neighbours'] += 1
                if( j - o >= 0 and o+i < c):
                    (matrix[j-o][o+i])['neighbours'] += 1
                if( j + o < r and i-o >= 0):
                    (matrix[j+o][i-o])['neighbours'] += 1
    resetMatrix = copy.deepcopy(matrix)

    # start on random
    visted = 0
    lastCell = []
    curMax = 0
    listOfMax = []
    for i in range(0, r):
        for j in range(0, c):              
            if (matrix[i][j])['neighbours'] >= curMax:
                listOfMax.append({'i': i, 'j': j, 'm': matrix[i][j]['neighbours']})
                curMax = matrix[i][j]['neighbours']
                lastCell = [i, j]
    
    for cell in range(len(listOfMax)):
        if (cell >= len(listOfMax)):
            break
        if listOfMax[cell]['m'] != curMax:
            del listOfMax[cell]

    # print(listOfMax)

    visitOrder = []
    lastMax = 0
    # start randomly

    while visted < r*c:
        isFound = False
        (matrix[lastCell[0]][lastCell[1]])['visited'] = True
        visted += 1
        visitOrder.append([lastCell[0]+1, lastCell[1]+1])
        if visted == r * c:
            break
        # print(visitOrder)

        for o in range(0, r):
            j = lastCell[0]
            i = lastCell[1]
            (matrix[o][i])['neighbours'] -= 1

            if( j+o < r and o+i < c):
                (matrix[j+o][o+i])['neighbours'] -= 1
            if( j - o >= 0 and i - o >= 0):
                (matrix[j-o][i-o])['neighbours'] -= 1
            if( j - o >= 0 and o+i < c):
                (matrix[j-o][o+i])['neighbours'] -= 1
            if( j + o < r and i-o >= 0):
                (matrix[j+o][i-o])['neighbours'] -= 1
                
        for o in range(0, c):
            (matrix[lastCell[0]][o])['neighbours'] -= 1

        curMax = 0
        selectCell = []

        for i in range(0, r):
            for j in range(0, c):
                if (matrix[i][j])['visited'] == False and not isNeighbour(i, j, lastCell):
                    # shortcut to select cell                    
                    if (matrix[i][j])['neighbours'] >= curMax:
                        curMax = matrix[i][j]['neighbours']
                        selectCell.append({'i': i, 'j': j, 'm': matrix[i][j]['neighbours']})
                    
                        isFound = True

        for cell in range(len(selectCell)):
            if (cell >= len(selectCell)):
                break
            if selectCell[cell]['m'] != curMax:
                del selectCell[cell]

        # print(selectCell)
        # print(matrix)
        if( not isFound and not listOfMax ):
            return []
        elif( not isFound ):
            matrix = copy.deepcopy(resetMatrix)
            visitOrder = []
            visted = 0
            getMax = listOfMax.pop()
            lastCell = [getMax['i'], getMax['j']]
        else:
            selectCell = selectCell[random.randrange(0, len(selectCell))]
            lastCell = [selectCell['i'], selectCell['j']]

    return visitOrder


def isNeighbour(r, c, lastCell):
    return (r == lastCell[0] or c == lastCell[1] or r - c == lastCell[0] - lastCell[1] or r + c == lastCell[0] + lastCell[1])

tests = int(input())

for test in range(0, tests):
    curArgs = input().split()
    ans = findPath(int(curArgs[0]), int(curArgs[1]))
    if not ans:
        print('Case #{}: {}'.format(test+1, "IMPOSSIBLE"))
    else:
        print('Case #{}: {}'.format(test+1, "POSSIBLE"))
        for pair in ans:
            print('{} {}'.format(pair[0], pair[1]))
