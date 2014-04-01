#!/bin/python
# zzz

import argparse
import datetime

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculates wake up times based on sleep cycles')
    parser.add_argument('--cycles', default=6, type=int, help='number of sleep cycles to calculate')
    parser.add_argument('--sleepDelay', default=15, type=int, help='offset in minutes used to compensate for the time taken to fall asleep')
    parser.add_argument('--cycleLength', default=90, type=int, help='length in minutes of a complete sleep cycle')
    args = parser.parse_args()

    sleepDelay = datetime.timedelta(minutes=args.sleepDelay)
    cycleDelta = datetime.timedelta(minutes=args.cycleLength)
    currentTime = datetime.datetime.now()

    for cycle in range(1, args.cycles + 1):
        cycleEndTime = currentTime + (cycleDelta * cycle)
        print("%d Cycle(s): Wake up at %s" % (cycle, cycleEndTime.strftime("%I:%H%p")))
