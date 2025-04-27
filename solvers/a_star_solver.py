import heapq
from copy import deepcopy

def solve_a_star(puzzle):
    heap = []
    visited = set()

    g_cost = 0
    h_cost = puzzle.min_distance(puzzle.state)
    f_cost = g_cost + h_cost

    heapq.heappush(heap, (f_cost, g_cost, deepcopy(puzzle.state), []))
    visited.add(puzzle.serialize())

    moves = ['up', 'down', 'left', 'right']

    while heap:
        _, g, current_state, path = heapq.heappop(heap)
        puzzle.state = deepcopy(current_state)

        if puzzle.is_solved():
            print("Puzzle resolvido com A*!")
            print(f"Número de movimentos: {len(path)}")
            print(f"Caminho: {path}")
            return path

        for move in moves:
            if puzzle.is_direction_legal(move):
                next_puzzle = puzzle.copy()
                next_puzzle.state = deepcopy(current_state)
                next_puzzle.move(move)

                serialized = next_puzzle.serialize()
                if serialized not in visited:
                    visited.add(serialized)
                    g_new = g + 1
                    h_new = next_puzzle.min_distance(next_puzzle.state)
                    f_new = g_new + h_new
                    heapq.heappush(heap, (f_new, g_new, deepcopy(next_puzzle.state), path + [move]))

    print("Não foi possível resolver o puzzle com A*.")
    return None