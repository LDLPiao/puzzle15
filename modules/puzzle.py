import random
from copy import deepcopy

from numpy import matrix

class Puzzle:

    size = 4    # Tamanho do tabuleiro (size x size)

    def __init__(self, size=4, generate=True) -> None:
        """Inicializa o jogo e define o estado atual do tabuleiro"""
        self.size = size
        self.state = None
        self.goal_state = self.generate_goal_state()  # cria o objetivo dinamicamente
        if generate:
            self.generate_board()
            print(matrix(self.state))
            
    def generate_goal_state(self):
        """Gera o estado objetivo automaticamente baseado no tamanho"""
        goal = []
        n = 1
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(n)
                n += 1
            goal.append(row)
        goal[self.size-1][self.size-1] = 0  # Último elemento é o espaço vazio
        return goal
        
    def serialize(self) -> str:
        return ''.join(str(cell) for row in self.state for cell in row)
    
    def copy(self):
        new_puzzle = Puzzle(generate=False)
        new_puzzle.state = deepcopy(self.state)
        return new_puzzle

    def generate_board(self):
        self.state = deepcopy(self.goal_state)
        n_moves = random.randint(100, 500)
        for i in range(n_moves):
            direction = random.choice(['up', 'down', 'left', 'right'])
            if self.is_direction_legal(direction):
                self.move(direction)

    def find_empty(self) -> tuple[int, int] | None:
        """Encontra a posição da casa vazia no tabuleiro"""
        for x in range(self.size):
            for y in range(self.size):
                if self.state[x][y] == 0:
                    return x,y
        return None

    def move(self, direction: str):
        """Realiza o movimento das peças no tabuleiro"""
        if not self.is_direction_legal(direction):
            print("Direção inválida")
            return

        i,j = self.find_empty()
        new_state = self.state
        match direction:
            case 'up':
                new_state[i][j],new_state[i-1][j] = new_state[i-1][j],new_state[i][j]
            case 'down':
                new_state[i][j], new_state[i+1][j] = new_state[i+1][j], new_state[i][j]
            case 'left':
                new_state[i][j], new_state[i][j-1] = new_state[i][j-1], new_state[i][j]
            case 'right':
                new_state[i][j], new_state[i][j+1] = new_state[i][j+1], new_state[i][j]

        self.state = new_state


    def is_direction_legal(self, direction: str) -> bool | None:
       """Checa se o movimento desejado é válido"""
       if direction == 'up':
            return True if self.find_empty()[0] > 0 else False
       elif direction == 'down':
            return True if self.find_empty()[0] < self.size - 1 else False
       elif direction == 'left':
           return True if self.find_empty()[1] > 0 else False
       elif direction == 'right':
           return True if self.find_empty()[1] < self.size - 1 else False
       return None

    def is_solved(self) -> bool:
        if self.state == self.goal_state:
            return True
        return False

    @property
    def is_solvable(self) -> bool:
        """Checa se a configuração atual possui solução"""
        # N é sempre par, portanto isso não precisa ser checado
        if self.find_empty()[0] % 2 == 0:
            return True if self.count_inversions() % 2 != 0 else False
        else:
            return True if self.count_inversions() % 2 == 0 else False

    def count_inversions(self) -> int:
        """Conta o número de inversões no tabuleiro"""
        arr = []
        for x in self.state:
            for y in x:
                arr.append(y)
        count = 0
        for i in range(self.size**2):
            for j in range(i + 1, self.size**2):
                if arr[i] and arr[j] and arr[i] > arr[j]:
                    count += 1

        return count
    
    def min_distance(self, state) -> int:
        distance = 0
        for i in range(self.size):
            for j in range(self.size):
                value = state[i][j]
                if value != 0:
                    target_x = (value - 1) // self.size
                    target_y = (value - 1) % self.size
                    distance += abs(i - target_x) + abs(j - target_y)
        return distance