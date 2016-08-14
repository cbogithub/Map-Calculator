#!/usr/bin/python
# Version 1

import os
import sys
import time
import signal

def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        sys.exit(0)

def printmenu():
    os.system('cls') # for Windows
    os.system('clear')

    print (30 * '-')
    print (" CALCULATE ALL THE THINGS")
    print (30 * '-')
    print ("1. Accounts needed for steps size")
    print ("2. Scan time of steps")
    print ("3. Radius of scan from number of steps")
    print ("4. Steps need to cover a radius")
    print ("5. Scan cirlces per step size")
    print ("6. Number of workers per leap size (beehive)")
    print ("0. Quit")
    print (30 * '-')
    choice = raw_input('Enter your choice [0-6] : ')
    try:
        choice = int(choice)
    except:
        printmenu()
    print (30 * '-')

    if choice == 1:
        accountsForSteps()
    elif choice == 2:
        scantimeForSteps()
    elif choice == 3:
        radiusOfScan()
    elif choice == 4:
        stepsOfScan()
    elif choice == 5:
        circlesPerStep()
    elif choice == 6:
        workersPerStep()
    elif choice == 0:
        cleanExit("bye")
    else:
        printmenu()


def accountsForSteps():
    "Calculates the number of accounts needed for a specific step value to achiece a specific scan time"
    steps = int(input("Number of steps: "))
    delay = int(input("Scan delay: "))
    scantime = int(input("Scan time in seconds: "))

    runningtotal = delay
    for x in range(0,steps):
        time = x * 6 * delay
        runningtotal += time
    totaltime = runningtotal
    roughaccounts = totaltime / scantime

    for x in range(roughaccounts-1,roughaccounts+2):
        if x > 0:
            m, s = divmod(totaltime/x, 60)
            h, m = divmod(m, 60)
            print "%d accounts, -sd %d, -st %d, scans in %ds -%dh:%02dm:%02ds" % (x, delay, steps, totaltime/x, h, m, s)
    raw_input("Press Enter to continue...")
    printmenu()


def scantimeForSteps():
    "Calculates the time for a scan based on step size, number of accounts and scan delay"
    steps = int(input("Number of steps: "))
    delay = int(input("Scan delay: "))
    accounts = int(input("Number of accounts: "))
    runningtotal = delay
    for x in range(0,steps):
        time = x * 6 * delay
        runningtotal += time
    totaltime = runningtotal
    scantime = totaltime / accounts
    m, s = divmod(scantime, 60)
    h, m = divmod(m, 60)

    print "-st %d -sd %d: %ds - %dh:%02dm:%02ds - with %d accounts" %(steps,delay,scantime,h, m, s,accounts)
    raw_input("Press Enter to continue...")
    printmenu()


def radiusOfScan():
    steps = int(input("Number of steps: "))
    distance = ((steps-1) * 115) + 70
    print '%dm' %distance
    raw_input("Press Enter to continue...")
    printmenu()


def stepsOfScan():
    radius = int(input("Radius in metres: "))
    distance = (radius - 70) / 115
    for x in range(distance,distance+3):
        distance = ((x-1) * 115) + 70
        if x >0:
            print '%d steps - %dm' % (x, distance)
    raw_input("Press Enter to continue...")
    printmenu()


def circlesPerStep():
    steps = int(input("Max number of steps: "))
    runningtotal = 1
    for x in range(0,steps):
        temp = x * 6
        runningtotal += temp
    print "-st %d : %d scan circles" % (x+1,runningtotal )
    raw_input("Press Enter to continue...")
    printmenu()


def workersPerStep():
    steps = int(input("Max number of steps: "))
    runningtotal = 1
    for x in range(0,steps):
        temp = x * 6
        runningtotal += temp
    print "-lp %d : %d Workers" % (x+1,runningtotal )
    raw_input("Press Enter to continue...")
    printmenu()


def cleanExit(message):
    sys.exit(message)


signal.signal(signal.SIGINT, signal_handler)
printmenu()
