import sys, time, bfs, dfs, ast, ida
import resource as re

def main():
    methods = ['bfs', 'dfs', 'ast', 'ida']
    running_time = 0
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
            start = time.clock()
            s = switch[method](board_arr, goal)
            running_time = time.clock() - start
            max_ram_usage = re.getrusage(re.RUSAGE_SELF).ru_maxrss
            s = s + ('\nrunning_time: %.8f\n' % (running_time))
            s = s + ('max_ram_usage: %.8f\n' % (max_ram_usage))
            f = open('output.txt', 'w')
            f.write(s)
            f.close()
        else:
            print '<method> must be bfs|dfs|ast|ida'

if __name__ == '__main__':  main()
