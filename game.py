from cell_set.white_black_cell import white_cell


class game:
    def __init__(self, size_x: int, size_y: int, list_of_cells: int) -> None:
        # initialize  a detail of puzzel
        self.size_x = size_x
        self.size_y = size_x
        self.list_of_cells = list_of_cells

        self.detail = {"WHITE": 0, "LIMITED": -1, "BLACK": -2}

        self.ways = {"DOWN": "down", "RIGHT": "right"}

        self.limited_cells = self.extract_limited_cells()

        # create board
        self.board = self.create_board_geame()

        # show this
        self.show_board()

    def extract_limited_cells(self) -> list:
        limited_cells = list()

        for element in self.list_of_cells:
            if element.category == self.detail["LIMITED"]:
                if element.down_way is not None:
                    limited_cells.append(element.down_way)

                if element.right_way is not None:
                    limited_cells.append(element.right_way)

        return limited_cells

    def create_board_geame(self) -> list:
        board = [
            [white_cell((i, j)) for j in range(self.size_x)] for i in range(self.size_y)
        ]

        for element in self.list_of_cells:
            board[element.location[0]][element.location[1]] = element
        return board

    def extract_cells_for_limitation(self, limited_cell) -> list:
        cell_included_limitation = list()

        if limited_cell.ways is self.ways["DOWN"]:
            for i in range(limited_cell.size):
                cell_included_limitation.append(
                    self.board[limited_cell.location[0] + i + 1][
                        limited_cell.location[1]
                    ]
                )

        if limited_cell.ways is self.ways["RIGHT"]:
            for i in range(limited_cell.size):
                cell_included_limitation.append(
                    self.board[limited_cell.location[0]][
                        limited_cell.location[1] + i + 1
                    ]
                )

        return cell_included_limitation

    def counter_limited_cell_unassigned(self, limited_cell) -> int:

        counter = 0
        for cell in self.extract_cells_for_limitation(limited_cell):
            if cell.value == 0:
                counter += 1
        return counter

    def is_limited_cell_assigned(self, limited_cell) -> bool:
        if self.counter_limited_cell_unassigned(limited_cell) == 0:
            return True
        return False

    def check_consistent(self) -> bool:
        for limited_cell in self.limited_cells:
            consistent_cells = self.extract_cells_for_limitation(limited_cell)
            if self.is_limited_cell_assigned(limited_cell):
                Sum = 0
                values = []
                for element in consistent_cells:
                    values.append(element.value)
                    Sum += element.value
                if Sum != limited_cell.target_sum or self._check_repeat(values):
                    return False

        return True

    def _check_repeat(self, values: list) -> bool:

        for element in values:
            if values.count(element) > 1:
                return True

        return False

    def game_is_finished(self) -> bool:
        for i in range(0, self.size_y):
            for j in range(0, self.size_x):
                if (
                    self.board[i][j].category == self.detail["WHITE"]
                    and self.board[i][j].value == 0
                ):
                    return False
        return True

    def show_board(self) -> None:
        for i in range(self.size_x):
            for j in range(self.size_y):
                if self.board[i][j].category is self.detail["BLACK"]:

                    print("■", end=" | ")

                elif self.board[i][j].category is self.detail["LIMITED"]:

                    right = "■"
                    down = "■"

                    result = f"{right}/{down}"

                    if self.board[i][j].right_way is not None:
                        right = self.board[i][j].right_way.target_sum
                    elif self.board[i][j].down_way is not None:
                        down = self.board[i][j].down_way.target_sum

                    result = f"{right}/{down}"
                    print(result, end=" | ")

                elif self.board[i][j].category is self.detail["WHITE"]:
                    print(self.board[i][j].value, end=" | ")
            print()

    def assign_limited_cell(self, limited_cell, values: list) -> None:

        if limited_cell.ways is self.ways["DOWN"]:
            for i in range(limited_cell.size):
                self.board[limited_cell.location[0] + i + 1][
                    limited_cell.location[1]
                ].value = values.pop(0)

        elif limited_cell.ways is self.ways["RIGHT"]:
            for i in range(limited_cell.size):
                self.board[limited_cell.location[0]][
                    limited_cell.location[1] + i + 1
                ].value = values.pop(0)
