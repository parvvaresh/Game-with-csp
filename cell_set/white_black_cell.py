from .cell import cell
from .detail_cell import type_of_cells


class white_cell(cell):
    def __init__(self, location: set, value=0) -> None:
        super().__init__(location, category=type_of_cells["WHITE"])
        self.value = value


class black_cell(cell):
    def __init__(self, location: set) -> None:
        super().__init__(location, category=type_of_cells["BLACK"])
