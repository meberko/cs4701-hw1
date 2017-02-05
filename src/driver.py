import sys
import math
import bfs
import dfs

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
        switch = {
            'bfs': bfs.run(board_arr),
            'dfs': dfs.run(board_arr)
        }
        switch[method]
    else:
        print '<method> must be bfs|dfs|ast|ida'
