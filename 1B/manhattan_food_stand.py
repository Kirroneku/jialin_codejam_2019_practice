from collections import OrderedDict

def findFoodStand(people, gridSize):
    # allDirections = []

    xAdditions = OrderedDict()
    yAdditions = OrderedDict()
    startX = 0
    startY = 0
    for i in range(people):
        direction = input().split()
        x = int(direction[0])
        y = int(direction[1])
        facing = direction[2]
        # allDirections.append({'x': x, 'y': y, 'Facing': facing})
        if facing == 'N':
            if(yAdditions.get((y)) == None):
                yAdditions[(y)] = 0
            if(yAdditions.get((y+1)) == None):
                yAdditions[(y+1)] = 0
            yAdditions[(y+1)] += 1

        elif( facing == 'S' ):            
            if(yAdditions.get((y-1)) == None):
                yAdditions[(y-1)] = 0
            if(yAdditions.get((y)) == None):
                yAdditions[(y)] = 0

            yAdditions[(y)] -= 1
            startY += 1
            
        elif( facing == 'E'):
            if(xAdditions.get((x)) == None):
                xAdditions[(x)] = 0
            if(xAdditions.get((x+1)) == None):
                xAdditions[(x+1)] = 0
            xAdditions[(x+1)] += 1

        else:            
            if(xAdditions.get((x-1)) == None):
                xAdditions[(x-1)] = 0
            if(xAdditions.get((x)) == None):
                xAdditions[(x)] = 0

            xAdditions[(x)] -= 1
            startX += 1

    for k in xAdditions:
        startX += xAdditions[k]
        xAdditions[k] = startX
    
    for k in yAdditions:
        startY += yAdditions[k]   
        yAdditions[k] = startY

    resetStartX = startX
    maxPass = 0
    maxPassCoords = [0, 0]

    if not bool(xAdditions):
        xAdditions[0] = 0
    if not bool(yAdditions):
        yAdditions[0] = 0

    for j in yAdditions:
        for i in xAdditions:
            totalPass = yAdditions[j] + xAdditions[i] 
            if totalPass > maxPass:
                maxPassCoords = [i, j]
                maxPass = totalPass
            
    return maxPassCoords

def passThrough( direction, i, j):
    facing = direction['Facing']
    x = direction['x']
    y = direction['y']
    
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