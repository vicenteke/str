import math
import matplotlib.pyplot as plt
import random

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
    w0 = period[0]
    n = 0
    test = 0
    for u in utilization:
        utilization_sum += u
        if n > 0 and harmonic:
            if period[n] % w0 != 0:
                harmonic = False
        n += 1

    if harmonic:
        test = 1
    else:
        test = n * (pow(2, float(1/n)) - 1)
    if test >= utilization_sum:
        return 1
    else:
        return 0

def rta_test(utilization, period):
    # utilization, period = sort_by_priority(utilization, period)
    i = len(period) - 1
    for p in reversed(period):
        if i < 0:
            return 1

        ri = []
        result = 0
        j = 0
        k = 1

        # Calculates ri[0]
        result = period[i] * utilization[i]
        while (period[j] < p and j < i):
            result += period[j] * utilization[j]
            j += 1

        ri.append(result)
        
        # Calculates ri[1]
        result = period[i] * utilization[i]
        j = 0
        while (period[j] < p and j < i):
            result += math.ceil(ri[k - 1] / period[j]) * period[j] * utilization[j]
            j += 1

        ri.append(result)

        # Calculates ri[k]
        while (abs(ri[k] - ri[k - 1]) > 0.001):
            k += 1
            j = 0
            result = period[i] * utilization[i]
            while (period[j] < p and j < i):
                result += math.ceil(ri[k - 1] / period[j]) * period[j] * utilization[j]
                j += 1

            # As Ri[k + 1] >= Ri[k] always
            if result > p:
                return 0

            ri.append(result)

        i -= 1
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
    plt.plot(x, graphL, color = "#DC143C", label = "Liu&Layland")
    plt.plot(x, graphH, ':', color = "#008B8B", label = "Hyperbolic", linewidth = 3.5)
    plt.plot(x, graphR, color = "#FF7F50", label = "RTA")

    plt.legend(loc = "lower left")
    plt.title(title)
    plt.xlabel("Total Utilization")
    plt.ylabel("Schedulability [%]")
    plt.ylim(-4, 104)
    plt.savefig(filename)

# Generates a random number (uniform) within min and max, with 'resolution' decimals
def random_uniform_res(min, max, resolution):
    return round(random.uniform(min, max), resolution)

# Sorts both parameters based on priority (shorter period, higher priority)
def sort_by_priority(utilization, period):
    arrayUtilization = [u for p, u in sorted(zip(period, utilization))]
    period.sort()
    return arrayUtilization, period

# Writes 'utilization' and 'period' arrays to 'file'
def write_into_file(file, utilization, period):
    list = ['{:.4f}'.format(x) for x in utilization]
    str = "[" + ', '.join(list) + "]\n"
    file.write(str)
    list = ['{:.3f}'.format(x) for x in period]
    str = "[" + ', '.join(list) + "]\n"
    file.write(str)
    file.write('\n')

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

    if case >= 6:
        # Heavy utilization
        if max_utilization < 0.9:
            # Only possible combination is (10 * max_utilization) tasks of max_utilization_case
            for n in range(0, int(10 * max_utilization)):
                arrayUtilization.append(max_utilization_case)
                arrayPeriod.append(random_uniform_res(min_period_case, max_period_case, 3))

        else:
            # Can only be all max_utilization_case or all min_utilization_case + 1 task
            usesMinUtilization = int(random.random() * 2) % 2
            for n in range(0, int(10 * max_utilization) + usesMinUtilization):
                arrayPeriod.append(random_uniform_res(min_period_case, max_period_case, 3))
                if usesMinUtilization == 1:
                    if n == 10:
                        # For 1.0 utilization, last task has to be max_utilization_case
                        arrayUtilization.append(max_utilization_case)
                    else:
                        arrayUtilization.append(min_utilization_case)
                else:
                    arrayUtilization.append(max_utilization_case)

        return arrayUtilization, arrayPeriod

    else:
        current_utilization = 0.0
        while current_utilization < max_utilization:
            arrayPeriod.append(random_uniform_res(min_period_case, max_period_case, 3))
            if(max_utilization - current_utilization < max_utilization_case and not(max_utilization - current_utilization > min_utilization_case)):
                arrayUtilization.append(max_utilization - current_utilization)
                current_utilization = max_utilization
            else:
                if case < 3:
                    holder = random_uniform_res(min_utilization_case, max_utilization_case, 4)
                elif case < 6:
                    holder = random_uniform_res(min_utilization_case, max_utilization_case, 3)
                else:
                    holder = random_uniform_res(min_utilization_case, max_utilization_case, 2)

                current_utilization += holder
                arrayUtilization.append(holder)

    return arrayUtilization, arrayPeriod


def main():

    f = open("data.txt",'r+') # File that stores data used for calculations
    f.truncate(0) # Clear file
    plt.ion() # Sets plotting functions as non-blocking

    graphH = [] # Stores values of current graphic for Liu&Layland test
    graphL = [] # Stores values of current graphic for Hyperbolic test
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
                arrayUtilization, arrayPeriod = sort_by_priority(arrayUtilization, arrayPeriod)
                write_into_file(f, arrayUtilization, arrayPeriod)
                countH += hyperbolic_test(arrayUtilization)
                countL += liu_lay_test(arrayUtilization, arrayPeriod)
                countR += rta_test(arrayUtilization, arrayPeriod)

            graphH.append(countH)
            graphL.append(countL)
            graphR.append(countR)

            countH = countL = countR = 0
            max_util += 0.1
            max_util = round(10 * max_util) / 10
        
        plotGraph(case, graphH, graphL, graphR)
        graphH = []
        graphL = []
        graphR = []
        max_util = 0.1

    f.close()
    
    # Blocks script while plots are open
    plt.ioff()
    plt.show()
    

if __name__ == "__main__":
    main()
    print("Plots and data were saved in current folder")
