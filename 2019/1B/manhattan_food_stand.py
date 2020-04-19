from collections import OrderedDict

def findFoodStand(directions, gridSize):
    # 

    xIndicies = [0]
    yIndicies = [0]

    xAdditions = {}
    yAdditions = {}
    startX = 0
    startY = 0
    for direction in directions:    
        x = direction['x']
        y = direction['y']
        facing = direction['facing']
        if facing == 'N':
            if(yAdditions.get((y+1)) == None):
                yAdditions[(y+1)] = 0
            yAdditions[(y+1)] += 1
            if( yIndicies.count(y+1) == 0 ):
                yIndicies.append(y+1)

        elif( facing == 'S' ):            
            if(yAdditions.get((y)) == None):
                yAdditions[(y)] = 0

            yAdditions[(y)] -= 1
            startY += 1
            if( yIndicies.count(y) == 0 ):
                yIndicies.append(y)

        elif( facing == 'E'):
            if(xAdditions.get((x+1)) == None):
                xAdditions[(x+1)] = 0
            xAdditions[(x+1)] += 1
            if( xIndicies.count(x+1) == 0 ):
                xIndicies.append(x+1)

        else:            
            if(xAdditions.get((x)) == None):
                xAdditions[(x)] = 0

            xAdditions[(x)] -= 1
            startX += 1
            if( xIndicies.count(x) == 0 ):
                xIndicies.append(x)

    xIndicies.sort()
    yIndicies.sort()

    xAdditions[0] = startX
    yAdditions[0] = startY
    for k in xIndicies:
        if (k != 0):
            startX += xAdditions[k]
            xAdditions[k] = startX
    
    for k in yIndicies:
        if (k != 0):
            startY += yAdditions[k]   
            yAdditions[k] = startY

    maxY = 0
    maxYIndex = 0

    maxX = 0
    maxXIndex = 0    

    for j in yIndicies:
        if maxY < yAdditions[j]:
            maxYIndex = j
            maxY = yAdditions[j] 

    for i in xIndicies:
        if maxX < xAdditions[i]:
            maxXIndex = i  
            maxX = xAdditions[i] 
    
    # print(xAdditions)
    # print(yAdditions)
    return [maxXIndex, maxYIndex]

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
    allDirections = []
    
    args = input().split()
    people = int(args[0])
    gridSize = int(args[1])
    for i in range( people ):
        direction = input().split()
        
        x = int(direction[0])
        y = int(direction[1])
        facing = direction[2]
        allDirections.append({'x': x, 'y': y, 'facing': facing})

    ans = findFoodStand(allDirections, gridSize)
    print('Case #{}: {} {}'.format(test+1, ans[0], ans[1]))