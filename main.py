import random
from abc import ABC, abstractmethod
from copy import deepcopy

from numpy import matrix

import keyboard


class Command(ABC):
    def __init__(self, receiver):
        self.receiver = receiver

    @abstractmethod
    def execute(self) -> None:
        pass


class MoveUp(Command):
    def __init__(self, receiver):
        super().__init__(receiver)

    def execute(self) -> None:
        self.receiver.move('up')


class MoveDown(Command):
    def __init__(self, receiver):
        super().__init__(receiver)

    def execute(self) -> None:
        self.receiver.move('down')


class MoveLeft(Command):
    def __init__(self, receiver):
        super().__init__(receiver)

    def execute(self) -> None:
        self.receiver.move('left')


class MoveRight(Command):
    def __init__(self, receiver):
        super().__init__(receiver)

    def execute(self) -> None:
        self.receiver.move('right')


class InputHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command: Command, command_name) -> None:
        if command_name not in self.commands:
            self.commands[command_name] = []
        self.commands[command_name] = command

    def execute(self, command_name):
        if command_name not in self.commands:
            print("Comando não encontrado")
            return
        self.commands[command_name].execute()

class Puzzle:

    size = 4    # Tamanho do tabuleiro (size x size)

    def __init__(self, init_state=None) -> None:
        """Inicializa o jogo e define o estado atual do tabuleiro"""
        self.state = None
        self.goal_state = [
            [1,2,3,4],
            [5,6,7,8],
            [9,10,11,12],
            [13,14,15,0]
        ]
        self.generate_board()
        print(matrix(self.state))


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


if __name__ == '__main__':
    puzzle = Puzzle()

    input_handler = InputHandler()
    input_handler.register_command(MoveUp(puzzle), 'up')
    input_handler.register_command(MoveDown(puzzle), 'down')
    input_handler.register_command(MoveLeft(puzzle), 'left')
    input_handler.register_command(MoveRight(puzzle), 'right')

    print(f'Número de inversões no tabuleiro: {puzzle.count_inversions()}')

    if not puzzle.is_solvable:
        print('Configuração sem solução...')
        exit(1)
    else:
        print('Configuração válida')

    while not puzzle.is_solved():
        _input = input("W - up, S - down, L - left, R - right")
        if _input == 'w':
            input_handler.execute('up')
            print(matrix(puzzle.state))
        elif _input == 's':
            input_handler.execute('down')
            print(matrix(puzzle.state))
        elif _input == 'a':
            input_handler.execute('left')
            print(matrix(puzzle.state))
        elif _input == 'd':
            input_handler.execute('right')
            print(matrix(puzzle.state))
        elif _input == 'q':
            print('Programa encerrado')
            exit(0)