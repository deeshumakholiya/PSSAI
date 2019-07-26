from jobshop import *

if __name__ == '__main__':

    jobs = Jobs('instances/3x3')

    m = len(jobs[0])
    j = len(jobs)
    print("Chosen file:", 'instances/3x3')
    print("Number of machines:", m)
    print("Number of jobs:", j)
    printJobs(jobs)

    cost, solution = simulatedAnnealingSearch(jobs, maxTime=20, T=int(200), termination=int(10), halting=int(10), mode='random', decrease=float(0.8))

    printSchedule(jobs, solution)
