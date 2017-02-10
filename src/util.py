class Node:
    def __init__(self, board_arr, parent, move, depth):
        self.board_arr = board_arr
        self.parent = parent
        self.move = move
        self.depth = depth

    def __eq__(self, rhs):
        return self.board_arr == rhs.board_arr

    def __hash__(self):
        return hash(tuple(self.board_arr))

def up_action(board_arr,blank_idx,r,c):
    b_arr = list(board_arr)
    if blank_idx / r != 0:
        swap(b_arr, blank_idx, blank_idx - r)
        return b_arr
    else:
        return []

def down_action(board_arr,blank_idx,r,c):
    b_arr = list(board_arr)
    if blank_idx / r != r-1:
        swap(b_arr, blank_idx, blank_idx + r)
        return b_arr
    else:
        return []

def left_action(board_arr,blank_idx,r,c):
    b_arr = list(board_arr)
    if blank_idx % r != 0:
        swap(b_arr, blank_idx, blank_idx - 1)
        return b_arr
    else:
        return []

def right_action(board_arr,blank_idx,r,c):
    b_arr = list(board_arr)
    if blank_idx % r != r-1:
        swap(b_arr, blank_idx, blank_idx + 1)
        return b_arr
    else:
        return []

def swap(a,i,j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp

def print_board(b_arr,r,c):
    print 'Board:'
    for i in range(0,r):
        for j in range(0,c):
            print b_arr[r*i+j],
        print
    print

def get_manhattan_priority(board_arr,r,c):
    idx = 0
    priority = 0
    for i in board_arr:
        desired_i = int(i) / r
        desired_j = int(i) % r
        curr_idx = board_arr.index(str(i))
        curr_i = curr_idx / r
        curr_j = curr_idx % r
        priority += abs(desired_i - curr_i) + abs(desired_j - curr_j)
        idx += 1
    return priority

def create_board_set_element(board_arr):
    string = ''
    for i in board_arr:
        string = string + i
    return string