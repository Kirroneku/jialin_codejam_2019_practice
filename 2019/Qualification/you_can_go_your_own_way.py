# Fleetwood Mac - Go Your Own Way

def findPath( path ):
    myPath = ''
    # just do exactly the opposite they do
    # Will work b/c it is a square
    for char in path:
        if char == 'E':
            myPath += 'S'
        else:
            myPath += 'E'

    return myPath

tests = int(input())

for test in range(0, tests):
    square = int(input())
    lydiaPath = input()
    print('Case #' + str(test+1) + ': ' + findPath(lydiaPath))