import sys
import random

def simulate(switch):
    '''This function accepts as argument a boolean variable indicating whether
    the case is of switching your choice after a goat reveal (if True) or 
    sticking with the original choice (if False). It then uses random numbers
    to perform a simulation/experiment of the Monty Hall game. Finally, it 
    returns 1 if the game was successful, i.e. the choosers gets car, and 0
    if game was a failure, i.e. the chooser gets a goat'''

    # Fill in your code here

    return 1

def main(N):
    successful_switch = 0
    successful_stick = 0
    for i in range(N):
        successful_switch += simulate(True)
        successful_stick += simulate(False)
    print N, ' simulations of Monte Hall were run...'
    print 'Successful Switching Strategies: ', 100.0*successful_switch/N, ' percent'
    print 'Successful Sticking  Strategies: ', 100.0*successful_stick/N,  ' percent'

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print ("Wrong number of arguments! Enter number of simulations to run as argument.\n"
               "Example Usage: python montyhall.py 1000 to run 1000 simulations\n")
    try:
        numsims = int(sys.argv[1])
    except:
        print 'Expected input type integer, obtained: ', sys.argv[1]
        sys.exit()
    main(numsims)
