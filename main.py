from cell_set.white_black_cell import white_cell, black_cell
from cell_set.limited_cells import limitation_target, limitation_target_cell
from cell_set.white_black_cell import white_cell, black_cell

from agent import agent
from game import game
from ai_agent import ai_agent


import time

cells = []


ways = {"DOWN": "down", "RIGHT": "right"}

cells.append(black_cell((0, 0)))
cells.append(black_cell((0, 1)))
cells.append(
    limitation_target_cell((0, 2), limitation_target(ways["DOWN"], 4, 22), None)
)
cells.append(
    limitation_target_cell((0, 3), limitation_target(ways["DOWN"], 4, 12), None)
)
cells.append(black_cell((0, 4)))
cells.append(black_cell((1, 0)))
cells.append(
    limitation_target_cell(
        (1, 1),
        limitation_target(ways["DOWN"], 2, 15),
        limitation_target(ways["RIGHT"], 2, 12),
    )
)
cells.append(
    limitation_target_cell((1, 4), limitation_target(ways["DOWN"], 2, 9), None)
)
cells.append(
    limitation_target_cell((2, 0), None, limitation_target(ways["RIGHT"], 4, 13))
)
cells.append(
    limitation_target_cell((3, 0), None, limitation_target(ways["RIGHT"], 4, 29))
)
cells.append(black_cell((4, 0)))
cells.append(
    limitation_target_cell((4, 1), None, limitation_target(ways["RIGHT"], 2, 4))
)
cells.append(black_cell((4, 4)))


puzzle = game(5, 5, cells)

ag = agent(puzzle)


start_time = time.time()
ag.solve_game()
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution Time: {round(execution_time, 2)} seconds")


ai_ag = ai_agent(puzzle)
puzzle = game(5, 5, cells)

start_time = time.time()
ai_ag.solve_game()
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution Time: {round(execution_time, 2)} seconds")
