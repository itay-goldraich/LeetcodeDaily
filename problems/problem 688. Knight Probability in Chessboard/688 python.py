import functools

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        @functools.lru_cache(None)
        def travel(move_left: int, row: int, col: int) -> float:
            if row not in range(n) or col not in range(n):
                return 0
            elif move_left == 0:
                return 1
            else:
                total = 0.0
                for dr, dc in moves:
                    total += travel(move_left - 1, row + dr, col + dc)
                total /= 8
                return total
        return travel(k, row, column)
