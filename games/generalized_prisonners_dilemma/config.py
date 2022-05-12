# GAME ENVIRONEMNT
NUM_PLAYERS=2
TURN_BASED=False
WIN_CRITERIA='score'
PAYOFF_MATRICES = \
    5 * [[[(1,1), (0,0)],  #1
          [(0,0), (0,0)]]]\
    + \
    5 * [[[(1,1), (0,2)],  #2
          [(2,0), (0,0)]]]\
    + \
    5 * [[[(10,10), (2,5)],  #3
          [(5,2), (0,0)]]]\
    + \
    5 * [[[(3,3), (5,2)],  #4
          [(2,5), (0,0)]]]\
    + \
    5 * [[[(5,5), (0,10)],  #5
          [(10,0), (0,0)]]]\
    + \
    5 * [[[(0,0), (0,1)],  #6
          [(1,0), (5,5)]]]\
    + \
    5 * [[[(5,3), (3,5)],  #7a
          [(1,0), (0,0)]]]\
    + \
    5 * [[[(3,5), (0,1)],  #7b
          [(5,3), (0,0)]]]\
    + \
    5 * [[[(1,1), (3,2)],  #9
          [(5,0), (0,0)]]]\
    + \
    5 * [[[(1,1), (0,5)],  #10
          [(2,3), (0,0)]]]

ITERATIONS = len(PAYOFF_MATRICES)