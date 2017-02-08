import sys, bfs, dfs, ast, ida

methods = ['bfs', 'dfs', 'ast', 'ida']

if len(sys.argv) != 3:
    print('usage: python driver.py <method> <board>')
else:
    method = sys.argv[1]
    board_str = sys.argv[2]
    if method in methods:
        board_arr = board_str.split(',')
        goal = map(str, range(0, len(board_arr)))
        switch = {
            'bfs': bfs.run,
            'dfs': dfs.run,
            'ast': ast.run,
            'ida': ida.run
        }
        switch[method](board_arr, goal)
    else:
        print '<method> must be bfs|dfs|ast|ida'
