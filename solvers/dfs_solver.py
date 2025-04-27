from copy import deepcopy

def solve_dfs(puzzle, max_depth=50):
    stack = []
    visited = set()

    stack.append((deepcopy(puzzle.state), [], 0))  # Estado, caminho, profundidade
    visited.add(serialize(puzzle.state))

    moves = ['up', 'down', 'left', 'right']
    size = puzzle.size  # Agora pega o tamanho automaticamente

    while stack:
        current_state, path, depth = stack.pop()

        if current_state == puzzle.goal_state:
            print("Puzzle resolvido com DFS!")
            print(f"Número de movimentos: {len(path)}")
            print(f"Caminho: {path}")
            return path

        if depth >= max_depth:
            continue

        empty_i, empty_j = find_empty(current_state, size)

        for move in moves:
            if is_move_legal(empty_i, empty_j, move, size):
                new_state = deepcopy(current_state)
                apply_move(new_state, empty_i, empty_j, move)
                serialized = serialize(new_state)

                if serialized not in visited:
                    visited.add(serialized)
                    stack.append((new_state, path + [move], depth + 1))

    print("Não foi possível resolver o puzzle com DFS dentro da profundidade máxima.")
    return None

def serialize(state):
    return ''.join(str(cell) for row in state for cell in row)

def find_empty(state, size):
    for i in range(size):
        for j in range(size):
            if state[i][j] == 0:
                return i, j
    return None

def is_move_legal(i, j, move, size):
    if move == 'up':
        return i > 0
    if move == 'down':
        return i < size - 1
    if move == 'left':
        return j > 0
    if move == 'right':
        return j < size - 1
    return False

def apply_move(state, i, j, move):
    if move == 'up':
        state[i][j], state[i-1][j] = state[i-1][j], state[i][j]
    if move == 'down':
        state[i][j], state[i+1][j] = state[i+1][j], state[i][j]
    if move == 'left':
        state[i][j], state[i][j-1] = state[i][j-1], state[i][j]
    if move == 'right':
        state[i][j], state[i][j+1] = state[i][j+1], state[i][j]