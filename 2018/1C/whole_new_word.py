tests = int(input())

for test in range(0, tests):
    args = [int(X) for X in input().split()]

    words = args[0]
    length = args[1]

    madeUpWords = []    
    newWord = []
    for i in range(words):
        madeUpWords.append(input())
    
    indicies = []
    for l in range(length):
        indicies.append(0)
        newWord.append(' ')

    done = False
    foundWord = False
    if length >= 2:
        while True:
            curIndex = length - 2
            for i in range(words): 
                indicies[length-1] = i
                for j in range(length):
                    newWord[j] = madeUpWords[indicies[j]][j]

                if( not ''.join(newWord) in madeUpWords ):
                    done = True
                    break
                
            if( done ):
                print('Case #{}: {}'.format(test+1, ''.join(newWord)))
                foundWord = True
                break

            indicies[length-1] = 0
            while( indicies[curIndex] == words-1 ):
                indicies[curIndex] = 0
                curIndex -= 1
                
            if( indicies[curIndex] != length-1):
                indicies[curIndex] += 1
                break

            if(curIndex == -1):
                break


        
    if not foundWord :
        print('Case #{}: {}'.format(test+1, '-'))