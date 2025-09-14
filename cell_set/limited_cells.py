from .cell import cell
from .detail_cell import type_of_cells


class limitation_target:
    def __init__(self, ways: str, size: int, target_sum: int) -> None:
        self.ways = ways
        self.size = size
        self.target_sum = target_sum
        self.location = None


class limitation_target_cell(cell):
    def __init__(self, location, down_way, right_way) -> None:
        super().__init__(location, category=type_of_cells["LIMITED"])

        self.right_way = right_way
        self.down_way = down_way

        if self.right_way is not None:
            self.right_way.location = self.location

        if self.down_way is not None:
            self.down_way.location = self.location
