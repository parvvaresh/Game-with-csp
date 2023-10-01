
# Sudoku Solver

This is a C program that solves Sudoku puzzles using a backtracking algorithm. Sudoku is a popular puzzle game where you need to fill a 9x9 grid with digits so that each column, each row, and each of the nine 3x3 subgrids that compose the grid (also called "regions") contain all of the digits from 1 to 9.

## How to Use

1. Clone the repository or download the source code files.

2. Compile the program using a C compiler. For example, you can use GCC:

   ```sh
   gcc sudoku_solver.c -o sudoku_solver
   ```

3. Run the program:

   ```sh
   ./sudoku_solver
   ```

4. Input the Sudoku puzzle. You need to provide a 9x9 grid as input where empty cells are represented by '0', and filled cells have their respective digits.

   Example input:
   ```
   5 3 0 0 7 0 0 0 0
   6 0 0 1 9 5 0 0 0
   0 9 8 0 0 0 0 6 0
   8 0 0 0 6 0 0 0 3
   4 0 0 8 0 3 0 0 1
   7 0 0 0 2 0 0 0 6
   0 6 0 0 0 0 2 8 0
   0 0 0 4 1 9 0 0 5
   0 0 0 0 8 0 0 7 9
   ```

5. The program will solve the Sudoku puzzle if a solution exists and display the solved grid.

## Algorithm

The program uses a backtracking algorithm to solve the Sudoku puzzle. It follows these steps:

1. Start at the first empty cell (0,0) and attempt to fill it with a digit from 1 to 9.

2. Check if the digit is valid according to Sudoku rules (no repetitions in the same row, column, or 3x3 subgrid). If valid, move to the next empty cell and repeat the process.

3. If no valid digit is found for the current cell, backtrack to the previous cell and try a different digit.

4. Repeat steps 1-3 until the entire grid is filled or no valid solution exists.

## Input Format

The program expects the Sudoku puzzle input as a 9x9 grid of integers in the range of 0 to 9, where '0' represents an empty cell and other digits represent filled cells.

## Output

The program outputs the solved Sudoku grid if a solution is found. If no solution exists for the input puzzle, it will not provide any output.

Feel free to use and modify this program to solve Sudoku puzzles of your choice.
```
