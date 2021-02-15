import math
import matplotlib.pyplot as plt
from random import seed
from random import random

# Every test function returns 1 in case of success and 0 otherwise
def hyperbolic_test(utilization):
    utilization_mult = 1
    for u in utilization:
        utilization_mult *= (u + 1)
    if 2 >= utilization_mult:
        return 1
    else:
        return 0

def liu_lay_test(utilization, period):
    utilization_sum = 0
    harmonic = True
    n = 0
    test = 0
    for u in utilization:
        utilization_sum += u
        n += 1
        if n > 0 and harmonic:
            if period[n] % period[n+1] != 0 and period[n+1] % period[n] != 0:
                harmonic = False

    if harmonic:
        test = 1
    else:
        test = n * (pow(2, (1/n)) - 1)
    if test >= utilization_sum:
        return 1
    else:
        return 0

def rta_test(utilization, period):
    i = 0
    for p in period:
        ri = []
        result = 0
        j = 0
        k = 1

        # Calculates ri[0]
        result = period[i] * utilization[i]
        while (j < i):
            result += period[j] * utilization[j]
            j += 1

        ri.append(result)
        
        # Calculates ri[1]
        result = period[i] * utilization[i]
        j = 0
        while (j < i):
            result += math.ceil(ri[k - 1] / period[j]) * period[j] * utilization[j]
            j += 1

        ri.append(result)

        # Calculates ri[k]
        while (abs(ri[k] - ri[k-1]) > 0.1):
            k += 1
            result = period[i] * utilization[i]
            j = 0
            while (j < i):
                result += math.ceil(ri[k - 1] / period[j]) * period[j] * utilization[j]
                j += 1

            ri.append(result)

        if ri[k] > p and i > 0: # Assuming Di = Ti
            return 0

        i += 1

    return 1

def plotGraph(case, graphH, graphL, graphR):
    title = "Title"
    filename = ""
    if case == 0:
        title = "Light Utilization / Light Period"
        filename = "plot0.png"
    elif case == 1:
        title = "Light Utilization / Moderate Period"
        filename = "plot1.png"
    elif case == 2:
        title = "Light Utilization / Long Period"
        filename = "plot2.png"
    elif case == 3:
        title = "Middle Utilization / Light Period"
        filename = "plot3.png"
    elif case == 4:
        title = "Middle Utilization / Moderate Period"
        filename = "plot4.png"
    elif case == 5:
        title = "Middle Utilization / Long Period"
        filename = "plot5.png"
    elif case == 6:
        title = "Heavy Utilization / Light Period"
        filename = "plot6.png"
    elif case == 7:
        title = "Heavy Utilization / Moderate Period"
        filename = "plot7.png"
    elif case == 8:
        title = "Heavy Utilization / Long Period"
        filename = "plot8.png"


    x = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    fig = plt.figure()
    plt.plot(x, graphH)
    plt.plot(x, graphL)
    plt.plot(x, graphR)

    plt.title(title)
    plt.xlabel("Total Utilization")
    plt.ylabel("Schedulability [%]")
    plt.savefig(filename)

def generateTaskSet(max_utilization, case):
    min_utilization_case = 0.0
    max_utilization_case = 0.0
    min_period_case = 0.0
    max_period_case = 0.0
    
    #Set the parameters to the given case
    if case == 0:
        min_utilization_case = 0.0001
        max_utilization_case = 0.01
        min_period_case = 3E-3
        max_period_case = 33E-3
    elif case == 1:
        min_utilization_case = 0.0001
        max_utilization_case = 0.01
        min_period_case = 10E-3
        max_period_case = 100E-3
    elif case == 2:
        min_utilization_case = 0.0001
        max_utilization_case = 0.01
        min_period_case = 50E-3
        max_period_case = 250E-3
    elif case == 3:
        min_utilization_case = 0.001
        max_utilization_case = 0.09
        min_period_case = 3E-3
        max_period_case = 33E-3
    elif case == 4:
        min_utilization_case = 0.001
        max_utilization_case = 0.09
        min_period_case = 10E-3
        max_period_case = 100E-3
    elif case == 5:
        min_utilization_case = 0.001
        max_utilization_case = 0.09
        min_period_case = 50E-3
        max_period_case = 250E-3
    elif case == 6:
        min_utilization_case = 0.09
        max_utilization_case = 0.1
        min_period_case = 3E-3
        max_period_case = 33E-3
    elif case == 7:
        min_utilization_case = 0.09
        max_utilization_case = 0.1
        min_period_case = 10E-3
        max_period_case = 100E-3
    elif case == 8:
        min_utilization_case = 0.09
        max_utilization_case = 0.1
        min_period_case = 50E-3
        max_period_case = 250E-3

    arrayUtilization = []
    arrayPeriod = []
    x
    current_utilization = 0.0
    while current_utilization < max_utilization:
        arrayPeriod.append(random.uniform(min_period_case,max_period_case))
        if(max_utilization - current_utilization < max_utilization_case and not(max_utilization - current_utilization > min_utilization_case)):
            arrayUtilization.append(max_utilization - current_utilization)
            current_utilization = max_utilization
        else:
            holder = random.uniform(min_utilization_case, max_utilization_case)
            current_utilization += holder
            arrayUtilization.append(holder)

    return arrayUtilization, arrayPeriod

def main():

    plt.ion() # Sets plotting functions as non-blocking

    # REMOVE DEFAULT VALUES (use "graphH = []") ---------------------------------
    graphH = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] # Stores values of current graphic for Liu&Layland test
    graphL = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91] # Stores values of current graphic for Hyperbolic test
    graphR = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50] # Stores values of current graphic for RTA test

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
                countH += hyperbolic_test(arrayUtilization)
                countL += liu_lay_test(arrayUtilization, arrayPeriod)
                countR += rta_test(arrayUtilization, arrayPeriod)

            # UNCOMMENT ----------------------
            # graphH.append(countH)
            # graphL.append(countL)
            # graphR.append(countR)

            countH = countL = countR = 0
            max_util += 0.1
        
        plotGraph(case, graphH, graphL, graphR)

    # Blocks script while plots are open
    plt.ioff()
    plt.show()
    

if __name__ == "__main__":
    main()
    print("Plots were saved in current folder")
