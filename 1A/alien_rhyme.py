def findRhymes( words ):
    if len(words) == 1:
        return 0
        
    words = sorted(words, key=lambda word: word[len(word)::-1])

    suffixesSeen = []

    reserveWords = []
    pairExists = True
    pairs = 0

    while pairExists:
        lastSuffix = None
        lastWord = None
        pairExists = False

        for i in range(len(words)-1):
            suffix = matchSuffix(words[i], words[i+1])

            s = True
            if lastSuffix != None and len(suffix) < len(lastSuffix):
                s = False

            if suffix != None and s and suffixesSeen.count(suffix) == 0:
                lastSuffix = suffix
                reserveWords = [i , i+1]
                pairExists = True

        if( pairExists ):
            suffixesSeen.append(lastSuffix)
            del words[reserveWords[0]]
            del words[reserveWords[1]-1]

            pairs += 2

    return len(suffixesSeen)*2

def matchSuffix( word1, word2 ):
    word1Index = len(word1) - 1
    word2Index = len(word2) - 1

    suffix = []

    for i in range(min(word1Index, word2Index), -1, -1):
        if( word1[word1Index] != word2[word2Index]):
            break

        suffix.append(word1[word1Index])

        word1Index -= 1
        word2Index -= 1
    
    if not suffix:
        return None

    return ''.join(suffix)

tests = int(input())

for test in range(0, tests):
    numWords = int(input())
    words = []

    for i in range(numWords):
        words.append(input())
    
    print('Case #{}: {}'.format(test+1, findRhymes( words )))