def findFoodStand(people, gridSize):
    allDirections = []

    xAdditions = [0 for i in range(gridSize+1)]
    yAdditions = [0 for i in range(gridSize+1)]

    for i in range(people):
        direction = input().split()
        x = int(direction[0])
        y = int(direction[1])
        facing = direction[2]
        allDirections.append({'x': x, 'y': y, 'Facing': facing})
        if facing == 'N':
            for j in  range(y+1, gridSize+1):
                yAdditions[j] += 1
        elif( facing == 'S' ):
            for j in range(0, y):
                yAdditions[j] += 1
        elif( facing == 'E'):
            for i in range(x+1, gridSize+1):
                xAdditions[i] += 1
        else:
            for i in range(0, x):
                xAdditions[i] += 1
    
    maxY = 0
    maxYIndex = 0

    maxX = 0
    maxXIndex = 0
    for j in range(gridSize+1):
        if maxY < yAdditions[j]:
            maxYIndex = j
            maxY = yAdditions[j] 

    for i in range(gridSize+1):
        if maxX < xAdditions[i]:
            maxXIndex = i  
            maxX = xAdditions[i] 
    print(xAdditions)
    print(yAdditions)
    return [maxXIndex, maxYIndex]

def passThrough( direction, i, j):
    facing = direction['Facing']
    x = direction['x']
    y = direction['y']
    
    # we can look on the vertical axis

    if( facing == 'N' and j > y):
        return True
    if( facing == 'S' and j < y):
        return True
    if( facing == 'E' and i > x):
        return True
    if( facing == 'W' and i < x):
        return True

    return False

tests = int(input())

for test in range(0, tests):
    args = input().split()
    people = int(args[0])
    gridSize = int(args[1])

    ans = findFoodStand(people, gridSize)
    print('Case #{}: {} {}'.format(test+1, ans[0], ans[1]))