# Sudoku Solver with Backtracking
Welcome to the Sudoku Solver with Backtracking! This Python program is designed to solve Sudoku puzzles using the backtracking algorithm. Sudoku is a popular logic-based combinatorial number-placement puzzle, and this solver aims to efficiently find a solution for any given puzzle.

### Agent Class (`agent` and `ai_agent`):

- **Initialization:**
  - The `__init__` method initializes the agent with a given game board. It sets `self.board` and `self.allowed_numbers`.

- **Solving the Game (`solve_game` Method):**
  - The `solve_game` method initiates the solving process by calling the `backtrack` method.
  - If a solution is found, it prints the solved board using the `show_board` method.
  - If no solution is found, it prints a message indicating that no solution was found.

- **Backtracking (`backtrack` and `_backtrack` Methods):**
  - The `backtrack` method creates a deep copy of the board and then calls the private `_backtrack` method to start the recursive backtracking process.
  - The `_backtrack` method checks if the game is finished and consistent. If so, it returns the solved assignment; otherwise, it continues with the backtracking process.

### Game Class (`game`):

- **Initialization:**
  - The `__init__` method initializes the game with a given size, a list of cells, and other details.
  - It extracts limited cells and creates the initial game board using the `create_board_geame` method.

- **Board Creation (`create_board_geame` Method):**
  - The `create_board_geame` method generates a 2D board with white cells, black cells, and limited target cells.

- **Consistency Check (`check_consistent` Method):**
  - The `check_consistent` method checks whether the current assignment of values to limited cells is consistent with the given limitations.

- **Limited Cell Assignment (`assign_limited_cell` Method):**
  - The `assign_limited_cell` method assigns values to limited cells based on the solution found during backtracking.

- **Display Board (`show_board` Method):**
  - The `show_board` method prints the current state of the game board, displaying white cell values, black cells, and limited targets.

### Cell Classes (`white_cell`, `black_cell`, `limitation_target_cell`):

- **Initialization:**
  - The `__init__` methods initialize cells with their locations and categories.

### Limitation_Target and Limitation_Target_Cell Classes:

- **Initialization:**
  - The `__init__` methods initialize limitation targets and limitation target cells with relevant details.

### Utility Functions:

- **Selected Unassigned Limited (`selected_unassigned_limited` Method):**
  - Selects an unassigned limited cell based on the number of unassigned cells in the limitation.

- **Get All State (`get_all_state` Method):**
  - Generates all possible states for a limited cell by considering the allowed numbers and the current assignment.

- **Get Difference Way for Sum (`get_difference_way_for_sum` Method):**
  - Generates different ways to achieve a target sum with a given set of allowed numbers.

- **Check (`_check` Method):**
  - Checks if a state is consistent, ensuring that no element is repeated.

- **Is Consistent (`is_consistent` Method):**
  - Checks if assigning a value to a limited cell maintains consistency with the limitations.
