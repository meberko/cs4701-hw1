import math, sets, util, time

def run(board_arr, goal):
    cost_of_path = nodes_expanded = fringe_size = max_fringe_size = search_depth = max_search_depth = 0
    goal_unfound = True
    rows = cols = int(math.sqrt(len(board_arr)))
    path_to_goal = []
    fringe = []
    fringe_set = set()
    visited = set()

    fringe.append(util.Node(board_arr, None, None, 0))
    fringe_set.add(util.Node(board_arr, None, None, 0))
    fringe_size += 1
    max_fringe_size += 1
    max_time = 0
    while fringe and goal_unfound:
        # Remove
        curr_node = fringe.pop() # Pop current config
        curr_board = curr_node.board_arr
        visited.add(curr_node) # Add current config to visited
        search_depth = curr_node.depth
        max_search_depth = max(search_depth, max_search_depth)
        blank_idx = curr_board.index('0')

        # Check
        if curr_board == goal:
            goal_unfound = False
            fringe_size = len(fringe)
            while True:
                try:
                    path_to_goal.append(curr_node.move)
                    if curr_node.depth == 1:
                        cost_of_path = len(path_to_goal)
                        path_to_goal.reverse()
                        break
                    curr_node = curr_node.parent
                except:
                    break
            return ("path_to_goal: %s\ncost_of_path: %d\nnodes_expanded: %d\nfringe_size: %d\nmax_fringe_size: %d\nsearch_depth: %d\nmax_search_depth: %d" % (str(path_to_goal), cost_of_path, nodes_expanded, fringe_size, max_fringe_size, search_depth, max_search_depth))

        # Expand
        nodes_expanded += 1

        right_node = util.Node(util.right_action(curr_board, blank_idx, rows, cols), curr_node, 'Right', search_depth+1)
        if right_node.board_arr and right_node not in visited and right_node not in fringe_set:
            fringe.append(right_node)
            fringe_set.add(right_node)

        left_node = util.Node(util.left_action(curr_board, blank_idx, rows, cols), curr_node, 'Left', search_depth+1)
        if left_node.board_arr and left_node not in visited and left_node not in fringe_set:
            fringe.append(left_node)
            fringe_set.add(left_node)

        down_node = util.Node(util.down_action(curr_board, blank_idx, rows, cols), curr_node, 'Down', search_depth+1)
        if down_node.board_arr and down_node not in visited and down_node not in fringe_set:
            fringe.append(down_node)
            fringe_set.add(down_node)

        up_node = util.Node(util.up_action(curr_board, blank_idx, rows, cols), curr_node, 'Up', search_depth+1)
        if up_node.board_arr and up_node not in visited and up_node not in fringe_set:
            fringe.append(up_node)
            fringe_set.add(up_node)

        fringe_size = len(fringe)
        max_fringe_size = max(fringe_size, max_fringe_size)
    return False
