import math

tests = int(input())

for test in range(0, tests):
    args = [int(x) for x in input().split()]

    people = args[0]
    languagesPolled = args[1]
    
    peopleToRound = 1
    while peopleToRound != people:
        determiner = peopleToRound/people * 100
        if determiner - math.floor(determiner) >= 0.5:
            break
        peopleToRound += 1

    # print(peopleToRound)
    # This way max can be reached within 10000-ish operations

    polled = [int(x) for x in input().split()]

    total = 0

    peopleAvaliable = people

    minCantFind = people


    for poll in polled :
        peopleAvaliable -= poll

    cheapestRounding = []

    for poll in polled :
        determiner = poll/people * 100
        if determiner - math.floor(determiner)  >= 0.5:
            total += math.ceil(determiner)
        elif peopleAvaliable > 0 :
            times = 1
            found = False
            while(peopleAvaliable >= times):
                determiner = (poll+times)/people * 100
                if determiner - math.floor(determiner)  >= 0.5:
                    cheapestRounding.append({'poll': poll, 'times': times, 'determiner': math.ceil(determiner)})
                    found = True
                    break
                times += 1
            if not found:
                total += round(poll/people * 100)
                # minCantFind = min(poll+peopleAvaliable, minCantFind)
        else:
            total+= round(determiner)

    cheapestRounding = sorted(cheapestRounding, key=lambda x:x['times'])

    for rounding in cheapestRounding:
        if( rounding['times'] > peopleAvaliable ):
            total += round(rounding['poll']/people * 100)
        else:
            peopleAvaliable -= rounding['times'] 
            total += rounding['determiner']
        # print(total)
        

    while peopleAvaliable >= peopleToRound:
        peopleAvaliable -= peopleToRound
        total += math.ceil(peopleToRound/people *100)

    if( peopleAvaliable > 0 ):
        total+= round(peopleAvaliable/people *100)

    print('Case #{}: {}'.format(test+1, total))