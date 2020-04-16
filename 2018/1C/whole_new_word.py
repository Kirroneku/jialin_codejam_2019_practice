tests = int(input())

for test in range(0, tests):
    args = [int(X) for X in input().split()]

    words = args[0]
    length = args[1]

    madeUpWords = []

    indexsForWords = []
    noWord = False
    startWords = []
    for i in range(words):
        madeUpWords.append(input())
        indexsForWords.append(1)
        startWords.append(i)

    found = False
    for j in startWords:
        newWord = []
        for index in range(length):
            first = True
            char = ''
            if( index == 0):
                first = False
                char = madeUpWords[j][index]
            # print(indexsForWords)
            for i in range(len(indexsForWords)):
                if( indexsForWords[i] == 0 ):
                    indexsForWords[i] = 1
                elif( first ):
                    char = madeUpWords[i][index]
                    first = False
                    # print(char)
                if( char != '' and char == madeUpWords[i][index] ):
                    indexsForWords[i] = 0
            if( char == ''):
                noWord = True
                break
            newWord.append(char)

        # print(newWord)
        if( not noWord and madeUpWords.count(''.join(newWord)) == 0 ):
            found = True
            print('Case #{}: {}'.format(test+1, ''.join(newWord)))
            break
        else:
            for i in range(len(indexsForWords)):
                indexsForWords[i] = 1

    if not found:
        print('Case #{}: {}'.format(test+1, '-'))