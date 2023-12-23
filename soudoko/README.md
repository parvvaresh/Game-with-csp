

# Sudoku Solver using Constraint Satisfaction Problem (CSP) Algorithm

This Python script provides a Sudoku solver using the Constraint Satisfaction Problem (CSP) algorithm. It is implemented with a modular structure, including classes for CSP, a set of CSP for Sudoku, and a class for managing the Sudoku board game.

## Usage

### Prerequisites

- Python 3.x

### Installation

No external dependencies are required. Simply download the script and run it using a Python interpreter.

### How to Run

1. Create a Sudoku board using the `board_game` class.
2. Initialize the CSP using the `set_csp` class, defining variables, domains, and constraints for the Sudoku problem.
3. Solve the Sudoku puzzle using the `csp` class and the backtracking algorithm.

```python
# Example Usage
game = board_game()
csp_det = set_csp()

variables = csp_det._varables()
Domains = csp_det._domains(game.get_puzzel(), variables)
constraints = csp_det._constraints(variables)

solver = csp(variables, Domains, constraints)
assignment = solver.solve()

# Update the Sudoku board with the solved values
for var, sol in assignment.items():
    game.get_puzzel()[var[0]][var[1]] = sol

# Display the solved Sudoku puzzle
game.show_puzzel()
```

## Classes

### 1. `board_game`

Handles the representation and display of the Sudoku board.

#### Methods

- `__init__(self, puzzle=None)`: Initializes the Sudoku board with the given puzzle (default is a sample puzzle).

- `show_puzzle(self)`: Displays the current state of the Sudoku board.

- `get_puzzle(self)`: Returns the current Sudoku puzzle.

- `set_puzzle(self, puzzle)`: Sets a new puzzle for the Sudoku board.

### 2. `set_csp`

Defines the variables, domains, and constraints for the Sudoku CSP.

#### Methods

- `_variables(self)`: Returns a list of variables for the Sudoku CSP.

- `_domains(self, puzzle, variables)`: Returns a dictionary of domains for each variable based on the given puzzle.

- `_set_constraints(self, variable)`: Returns a list of constraints for a given variable.

- `_constraints(self, variables)`: Returns a dictionary of constraints for each variable.

### 3. `csp`

Implements the CSP algorithm with backtracking to solve the Sudoku puzzle.

#### Methods

- `__init__(self, variables, domains, constraints)`: Initializes the CSP with variables, domains, and constraints.

- `solve(self)`: Solves the Sudoku puzzle using the backtracking algorithm and returns the solution.

- `backtrack(self, assignment)`: Recursive backtracking function to find a consistent assignment.

- `get_domains(self, var, assignment)`: Returns the domain for a given variable.

- `select_min_domain(self, assignment)`: Selects the variable with the minimum remaining values in its domain.

- `is_consistent(self, var, value, assignment)`: Checks if a variable assignment is consistent with the constraints.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



