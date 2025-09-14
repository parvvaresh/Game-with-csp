from copy import deepcopy


class ai_agent:
    def __init__(self, board) -> None:
        self.board = board
        self.allowed_numbers = list(range(1, 10))

    def solve_game(self) -> None:
        solution = self.backtrack(self.board)
        if solution is not None:
            solution.show_board()

        else:
            print("no solution found")

    def backtrack(self, board):
        return self._backtrack(deepcopy(board))

    def _backtrack(self, assignment):
        if assignment.game_is_finished() and assignment.check_consistent:

            print("solve this board !!!")
            return assignment

        limited_cell = self.selected_unassigned_limited(assignment)
        if limited_cell is not None:
            cell_included_limitation = assignment.extract_cells_for_limitation(
                limited_cell
            )

            value_sets = self.get_all_state(
                limited_cell, cell_included_limitation, assignment
            )
            for value_set in value_sets:
                if self.is_consistent(
                    limited_cell, deepcopy(value_set), deepcopy(assignment)
                ):
                    assignment.assign_limited_cell(limited_cell, value_set)
                    result = self._backtrack(deepcopy(assignment))
                    if result is not None:
                        return result

        return None

    def selected_unassigned_limited(self, assignment):

        limited_cells = dict()

        for limited_cell in assignment.limited_cells:
            if not assignment.is_limited_cell_assigned(limited_cell):
                unassigned_count = assignment.counter_limited_cell_unassigned(
                    limited_cell
                )
                limited_cells[limited_cell] = unassigned_count

        result = sorted(limited_cells.items(), key=lambda item: item[1])
        return result[0][0]

    def get_all_state(self, limited_cell, cell_included_limitation, assignment) -> list:

        value_sets = []
        assigned_cells = []
        unassigned_cells = []

        _allowed_numbers = deepcopy(self.allowed_numbers)
        for cell in cell_included_limitation:
            if cell.value == 0:
                unassigned_cells.append(cell)

            else:
                if cell.value in _allowed_numbers:
                    _allowed_numbers.remove(cell.value)

                assigned_cells.append(cell)

        sum_numbers = 0
        for cell in assigned_cells:
            sum_numbers += cell.value

        this_sum_now = limited_cell.target_sum - sum_numbers
        cell_counter = limited_cell.size - len(assigned_cells)

        unassigned_value_sets = self.get_difference_way_for_sum(
            this_sum_now, cell_counter, _allowed_numbers
        )

        for unassigned_value_set in unassigned_value_sets:
            variable_set = deepcopy(cell_included_limitation)
            value_set = []
            for cell in variable_set:
                if cell.value == 0:
                    value_set.append(unassigned_value_set.pop(0))
                else:
                    value_set.append(cell.value)
            value_sets.append(value_set)
        return value_sets

    def get_difference_way_for_sum(
        self, this_sum_now, cell_counter, allowed_numbers
    ) -> list:
        if cell_counter == 1 and this_sum_now in allowed_numbers:
            return [[this_sum_now]]

        states = list()
        for value in allowed_numbers:
            allowed_numbers_copy = deepcopy(allowed_numbers)
            allowed_numbers_copy.remove(value)
            if this_sum_now - value > 0:
                result = [
                    [value] + combo
                    for combo in self.get_difference_way_for_sum(
                        this_sum_now - value, cell_counter - 1, allowed_numbers_copy
                    )
                ]
                states.extend(result)

        for state in states:
            if self._check(state) == False:
                states.remove(state)

        return states

    def _check(self, state: list) -> bool:

        for element in state:
            if state.count(element) > 1:
                return False

        return True

    def is_consistent(self, limited_cell, value_set, assignment):
        assignment.assign_limited_cell(limited_cell, value_set)
        return assignment.check_consistent()
