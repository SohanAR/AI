import random

def print_board(board):
    for row in board:
        print(' '.join('Q' if col == 1 else '.' for col in row))
    print()

def generate_random_board(size):
    # Generates a random board of size `size` where each queen is placed in a random row in each column
    return [random.randint(0, size - 1) for _ in range(size)]

def calculate_conflicts(board):
    """Calculate the number of conflicting pairs of queens on the board"""
    conflicts = 0
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            # Check if two queens are in the same row or on the same diagonal
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                conflicts += 1
    return conflicts

def get_neighbors(board):
    """Generate all possible neighbors of the current board configuration"""
    neighbors = []
    n = len(board)
    for col in range(n):
        for row in range(n):
            if row != board[col]:
                # Create a new board with the queen in `col` moved to `row`
                neighbor = board[:]
                neighbor[col] = row
                neighbors.append(neighbor)
    return neighbors

def print_board_with_conflicts(board):
    size = len(board)
    print_board([[1 if board[col] == row else 0 for col in range(size)] for row in range(size)])
    print(f"Conflicts: {calculate_conflicts(board)}\n")

def hill_climbing(board):
    current_board = board
    current_conflicts = calculate_conflicts(current_board)
    
    print("Initial board:")
    print_board_with_conflicts(current_board)

    steps = 0  # To count the number of steps taken
    while True:
        neighbors = get_neighbors(current_board)
        neighbor_conflicts = [calculate_conflicts(neighbor) for neighbor in neighbors]
        
        # Display cost for the current state and all neighbors
        print(f"Step {steps}:")
        print(f"Current State Cost (Conflicts): {current_conflicts}")
        print("Neighbor States and Costs:")
        for i, neighbor in enumerate(neighbors):
            print(f"Neighbor {i+1}:")
            print_board([[1 if neighbor[col] == row else 0 for col in range(len(board))] for row in range(len(board))])
            print(f"Conflicts: {neighbor_conflicts[i]}")
        print()

        min_conflict = min(neighbor_conflicts)
        
        # If no improvement, stop
        if min_conflict >= current_conflicts:
            print(f"Terminated after {steps} steps.")
            break
        
        # Move to the neighbor with the least conflicts
        current_conflicts = min_conflict
        current_board = neighbors[neighbor_conflicts.index(min_conflict)]
        steps += 1
        
        print(f"Chosen State (Step {steps}):")
        print_board_with_conflicts(current_board)

    return current_board, current_conflicts

# Main function to solve 4 Queens using Hill Climbing
def solve_4_queens():
    size = 4
    board = generate_random_board(size)
    
    solution, conflicts = hill_climbing(board)
    
    if conflicts == 0:
        print("Solved the 4-Queens Problem!")
    else:
        print("Could not solve the 4-Queens Problem. Try again!")

# Run the algorithm
solve_4_queens()
