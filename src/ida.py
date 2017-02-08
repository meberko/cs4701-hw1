import math, heapq

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

def run(board_arr, goal):
    visited = []
    path_to_goal = ''
    cost_of_path = 0
    nodes_expanded = 0
    fringe_size = 0
    max_fringe_size = 0
    search_depth = 0
    max_search_depth = 0
    goal_unfound = True
    rows = int(math.sqrt(len(board_arr)))
    cols = rows
    fringe = []

    priority = get_manhattan_priority(board_arr, rows, cols)
    heapq.heappush(fringe, (priority, board_arr, ''))
    fringe_size += 1
    max_fringe_size += 1
    while not fringe == [] and goal_unfound:
        # Remove
        curr = heapq.heappop(fringe)
        curr_board = curr[1]
        curr_path = curr[2]
        visited.append(curr_board)
        fringe_size -= 1
        search_depth = len(curr_path.split(' ')[1:])
        blank_idx = curr_board.index('0')

        # Check
        if curr_board == goal:
            goal_unfound = False
            path_to_goal = curr_path.split(' ')[1:]
            cost_of_path = len(path_to_goal)

        # Expand
        else:
            nodes_expanded += 1
            up_board = up_action(curr_board, blank_idx, rows, cols)
            if not up_board == []:
                if not up_board in visited:
                    heapq.heappush(fringe, (get_manhattan_priority(up_board, rows, cols), up_board, curr_path + ' Up'))
                    fringe_size += 1

            down_board = down_action(curr_board, blank_idx, rows, cols)
            if not down_board == []:
                if not down_board in visited:
                    heapq.heappush(fringe, (get_manhattan_priority(down_board, rows, cols), down_board, curr_path + ' Down'))
                    fringe_size += 1

            left_board = left_action(curr_board, blank_idx, rows, cols)
            if not left_board == []:
                if not left_board in visited:
                    heapq.heappush(fringe, (get_manhattan_priority(left_board, rows, cols), left_board, curr_path + ' Left'))
                    fringe_size += 1

            right_board = right_action(curr_board, blank_idx, rows, cols)
            if not right_board == []:
                if not right_board in visited:
                    heapq.heappush(fringe, (get_manhattan_priority(right_board, rows, cols), right_board, curr_path + ' Right'))
                    fringe_size += 1
            if search_depth == max_search_depth:
                max_search_depth += 1
            if fringe_size > max_fringe_size:
                max_fringe_size = fringe_size
    print("path_to_goal: %s\ncost_of_path: %d\nnodes_expanded: %d\nfringe_size: %d\nmax_fringe_size: %d\nsearch_depth: %d\nmax_search_depth: %d\n" % (str(path_to_goal), cost_of_path, nodes_expanded, fringe_size, max_fringe_size, search_depth, max_search_depth))


