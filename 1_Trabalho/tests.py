
# Every test function returns 1 in case of success and 0 otherwise
def hyperbolic_test(utilization, period):
    return 1

def liu_lay_test(utilization, period):
    return 1

def rta_test(utilization, period):
    return 1

def plotGraph(case, graphH, graphL, graphR):
    if case == 0:
        title("Light Light Bro")
    return

def generateTaskSet(max_utilization, case):
    if case == 0: light | light
    elif case == 1: light | mid
    ...

    return arrayUtilization, arrayPeriod

def main():

    graphH = [] # Stores values of current graphic for Hyperbolic test
    graphL = [] # Stores values of current graphic for Liu&Layland test
    graphR = [] # Stores values of current graphic for RTA test

    countH = 0 # Counts how many task sets could be scheduled by Hyperbolic test
    countL = 0 # Counts how many task sets could be scheduled by Liu&Layland test
    countR = 0 # Counts how many task sets could be scheduled by RTA test

    max_util = 0.1

    # For each case
    for case in range(0, 9):
        # For max_util 0.1, 0.2 ... 1
        for y in range(1,11):
            # Generate 100 different task sets
            for z in range(1,101):
                arrayUtilization, arrayPeriod = generateTaskSet(max_util, case)
                countH += hyperbolic_test(arrayUtilization, arrayPeriod)
                countL += liu_lay_test(arrayUtilization, arrayPeriod)
                countR += rta_test(arrayUtilization, arrayPeriod)

            graphH.append(countH)
            graphL.append(countL)
            graphR.append(countR)

            countH = countL = countR = 0
            max_util += 0.1

        plotGraph(case, graphH, graphL, graphR)
    

if __name__ == "__main__":
    main()
