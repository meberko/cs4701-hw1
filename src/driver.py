import sys
import math
import bfs

methods = ['bfs', 'dfs', 'ast', 'ida']

if len(sys.argv) != 3:
    print('usage: python driver.py <method> <board>')
else:
    method = sys.argv[1]
    board_str = sys.argv[2]
    if method in methods:
        board_arr = board_str.split(',')
        rows = math.sqrt(len(board_arr))
        cols = rows
        print('board: %s' % str(board_arr))
    else:
        print '<method> must be bfs|dfs|ast|ida'
