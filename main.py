from numpy import matrix
from modules.puzzle import Puzzle
from solvers.dfs_solver import solve_dfs
from solvers.bfs_solver import solve_bfs
from solvers.a_star_solver import solve_a_star
from modules.input_handler import InputHandler
from modules.command import MoveUp, MoveDown, MoveLeft, MoveRight


def iniciar_puzzle():
    
    try:
        size_input = input('Digite o tamanho do puzzle (pressione Enter para usar 4): ')
        size = int(size_input) if size_input.strip() != '' else 4
    except ValueError:
        size = 4

    puzzle = Puzzle(size=size)

    input_handler = InputHandler()
    input_handler.register_command(MoveUp(puzzle), 'up')
    input_handler.register_command(MoveDown(puzzle), 'down')
    input_handler.register_command(MoveLeft(puzzle), 'left')
    input_handler.register_command(MoveRight(puzzle), 'right')

    return puzzle, input_handler

if __name__ == '__main__':
    puzzle, input_handler = iniciar_puzzle()

    print(f'Número de inversões no tabuleiro: {puzzle.count_inversions()}')

    while not puzzle.is_solvable:
        print('Configuração sem solução...')
        resposta = input('Deseja tentar gerar um novo tabuleiro? (s/n): ').lower()
        if resposta == 's':
            puzzle, input_handler = iniciar_puzzle()
            print(f'Número de inversões no tabuleiro: {puzzle.count_inversions()}')
        else:
            print('Programa encerrado')
            exit(0)

    print('Configuração válida')

    while not puzzle.is_solved():
        _input = input("W - up, S - down, L - left, R - right, B - resolver BFS, M - resolver A*, F - resolver DFS, Q - sair: ").lower()
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
        elif _input == 'b':
            print('Resolvendo com BFS...')
            caminho = solve_bfs(puzzle)
            if caminho:
                print('Executando solução (BFS)...')
                for move in caminho:
                    puzzle.move(move)
                    print(matrix(puzzle.state))
                print('Resolvido com BFS!')
            break
        elif _input == 'm':
            print('Resolvendo com A*...')
            caminho = solve_a_star(puzzle)
            if caminho:
                print('Executando solução (A*)...')
                for move in caminho:
                    puzzle.move(move)
                    print(matrix(puzzle.state))
                print('Resolvido com A*!')
            break
        elif _input == 'f':
            print('Resolvendo com DFS...')
            caminho = solve_dfs(puzzle)
            if caminho:
                print("Executando solução (DFS)...")
                for move in caminho:
                    puzzle.move(move)
                    print(matrix(puzzle.state))
                print("Puzzle resolvido!")
            break
        elif _input == 'q':
            print('Programa encerrado')
            exit(0)