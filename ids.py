# Helper function to check if the current state is the goal state
def is_goal(state):
    goal_state = ((1, 2, 3),
                  (4, 5, 6),
                  (7, 8, 0))
    return state == goal_state

# Helper function to find the position of the blank tile (0)
def find_blank(state):
    for i, row in enumerate(state):
        for j, tile in enumerate(row):
            if tile == 0:
                return i, j

# Helper function to generate successors (valid moves) from the current state
def successors(state):
    blank_i, blank_j = find_blank(state)
    moves = []
    
    # Possible directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for di, dj in directions:
        new_i, new_j = blank_i + di, blank_j + dj
        if 0 <= new_i < 3 and 0 <= new_j < 3:
            # Make a new state by swapping the blank with the adjacent tile
            new_state = [list(row) for row in state]  # Deep copy
            new_state[blank_i][blank_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[blank_i][blank_j]
            moves.append(tuple(tuple(row) for row in new_state))  # Convert to tuple for immutability
    return moves

# Depth-limited search (DFS) function
def depth_limited_search(state, depth):
    if is_goal(state):
        return [state]  # Return the solution path
    if depth == 0:
        return None

    for next_state in successors(state):
        result = depth_limited_search(next_state, depth - 1)
        if result is not None:
            return [state] + result  # Append the current state to the solution path
    
    return None

# Iterative deepening search (IDS)
def iterative_deepening_search(initial_state):
    depth = 0
    while True:
        result = depth_limited_search(initial_state, depth)
        if result is not None:
            return result  # Return the solution path when found
        depth += 1

# Example: Initial state of the puzzle
initial_state = ((1, 2, 3),
                 (4, 0, 5),
                 (7, 8, 6))

# Perform Iterative Deepening Search
solution = iterative_deepening_search(initial_state)

# Print the solution path
if solution:
    print("Solution found!")
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution found.")
