# def Troublesort( L ):
#     done = False
#     while not done:
#         done = True
#         for i in range(0, len(L)-2):
#             if L[i] > L[i+2]:
#                 done = False
#                 temp = L[i]
#                 L[i] = L[i+2]
#                 L[i+2] = temp
#     return L

def checkIfSorted( L ):
    for i in range(0, len(L)-1):
        if( L[i] > L[i+1]):
            return i

    return -1


# def checkIfInterweaved( L1, L2 ):
#     flip = True
#     for i in L1:
#         if( flip ):
#             L1[]
#         else:
#             L2.append(i)
#         flip = not flip

#     return -1

tests = int(input())

for test in range(0, tests):
    vals = input()
    L = [int(x) for x in input().split()]
    # L = Troublesort( L )
    L1 = []
    L2 = []
    flip = True
    for i in L:
        if( flip ):
            L1.append(i)
        else:
            L2.append(i)
        flip = not flip
    
    L1.sort()
    L2.sort()

    flip = True
    newL = []
    index1 = 0
    index2 = 0
    for i in L:
        if( flip ):
            newL.append(L1[index1])
            index1+=1
        else:
            newL.append(L2[index2])
            index2+=1
        flip = not flip

    ifSorted = checkIfSorted(newL)

    if(ifSorted == -1):
        ifSorted = "OK"
    else:
        ifSorted = str(ifSorted)

    print('Case #' + str(test+1) + ': ' + ifSorted)