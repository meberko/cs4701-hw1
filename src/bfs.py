import math, Queue

path_to_goal = 0
cost_of_path = 0
nodes_expanded = 0
fringe_size = 0
max_fringe_size = 0
search_depth = 0
max_search_depth = 0
goal = ['0','1','2','3','4','5','6','7','8']

def up_action(board_arr,blank_idx,r,c,fringe):
    b_arr = list(board_arr)
    if blank_idx / r != 0:
        swap(b_arr, blank_idx, blank_idx - 3)
        print_board(b_arr,r,c)
    else:
        print 'Can\'t go up'

def down_action(board_arr,blank_idx,r,c,fringe):
    b_arr = list(board_arr)
    if blank_idx / r != r-1:
        swap(b_arr, blank_idx, blank_idx + 3)
        print_board(b_arr,r,c)
    else:
        print 'Can\'t go down'

def left_action(board_arr,blank_idx,r,c,fringe):
    b_arr = list(board_arr)
    if blank_idx % r != 0:
        swap(b_arr, blank_idx, blank_idx - 1)
        print_board(b_arr,r,c)
    else:
        print 'Can\'t go left'

def right_action(board_arr,blank_idx,r,c,fringe):
    b_arr = list(board_arr)
    if blank_idx % r != r-1:
        swap(b_arr, blank_idx, blank_idx + 1)
        print_board(b_arr,r,c)
    else:
        print 'Can\'t go right'

def swap(a,i,j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp

def put_all(q):
    q.put('U')
    q.put('D')
    q.put('L')
    q.put('R')

def print_board(b_arr,r,c):
    print 'Board:'
    for i in range(0,r):
        for j in range(0,c):
            print b_arr[r*i+j],
        print
    print

def run(board_arr):
    rows = int(math.sqrt(len(board_arr)))
    cols = rows
    print_board(board_arr,rows,cols)
    blank_idx = board_arr.index('0')
    fringe = Queue.Queue()
    put_all(fringe)
    curr = fringe.get()
    actions = {
        'U': up_action,
        'D': down_action,
        'L': left_action,
        'R': right_action
    }
    actions[curr](board_arr, blank_idx, rows, cols, fringe)
    curr = fringe.get()
    actions[curr](board_arr, blank_idx, rows, cols, fringe)
    curr = fringe.get()
    actions[curr](board_arr, blank_idx, rows, cols, fringe)

