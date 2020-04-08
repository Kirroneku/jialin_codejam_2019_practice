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
            for j in  range(gridSize+1):
                if j > y :
                    yAdditions[j] += 1
        elif( facing == 'S' ):
            for j in  range(gridSize+1):
                if j < y :
                    yAdditions[j] += 1
        elif( facing == 'E'):
            for i in  range(gridSize+1):
                if i > x :
                    xAdditions[i] += 1
        else:
            for i in range(gridSize+1):
                if i < x:
                    xAdditions[i] += 1
    
    maxPass = 0
    maxPassCoords = [0, 0]

    for i in range(gridSize+1):
        for j in range(gridSize+1):
            totalPass = 0
            # for direction in allDirections:
                # if( passThrough(direction, i, j) ):
                #     totalPass += 1
            totalPass = xAdditions[i] + yAdditions[j]

            if totalPass > maxPass:
                maxPassCoords = [i, j]
                maxPass = totalPass

    return maxPassCoords

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