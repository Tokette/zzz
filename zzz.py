#!/bin/python
# zzz

import argparse
import datetime

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculates wake up times based on sleep cycles')
    parser.add_argument('-c', '--cycles', default=6, type=int, help='number of sleep cycles to calculate')
    parser.add_argument('-d', '--sleepDelay', default=15, type=int, help='offset in minutes used to compensate for the time taken to fall asleep')
    parser.add_argument('-l', '--cycleLength', default=90, type=int, help='length in minutes of a complete sleep cycle')
    args = parser.parse_args()

    cycleCount = args.cycles
    sleepDelay = datetime.timedelta(minutes=args.sleepDelay)
    cycleDelta = datetime.timedelta(minutes=args.cycleLength)
    currentTime = datetime.datetime.now()
    startTime = currentTime + sleepDelay

    print("Current Time: %s" % currentTime.strftime("%I:%M%p"))
    print("Sleeping Begins In %d Minutes At: %s" % (args.sleepDelay, startTime.strftime("%I:%M%p")))
    print("Using %d Minute Sleep Cycles" % args.cycleLength)
    for cycle in range(1, cycleCount + 1):
        cycleOffset = cycleDelta * cycle
        cycleTime = startTime + cycleOffset
        print("%d Cycle(s) %.2f Hours: Wake up at %s" % (cycle, cycleOffset.total_seconds() / 3600, cycleTime.strftime("%I:%M%p")))
