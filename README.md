Puzzle 15 - Algoritmos de Busca

Este projeto é uma implementação do clássico 15-Puzzle (ou puzzles NxN) usando Python, com suporte a três algoritmos de resolução:
	•	BFS (Busca em Largura)
	•	DFS (Busca em Profundidade)
	•	A* (A estrela com heurística de distância de mínima)

O projeto também permite controle manual para resolver o puzzle.

⸻

📂 Estrutura do Projeto

puzzle15/
├── main.py
├── modules/
│   ├── puzzle.py
│   ├── command.py
│   ├── input_handler.py
├── solvers/
│   ├── bfs_solver.py
│   ├── dfs_solver.py
│   ├── a_star_solver.py



⸻

🚀 Como Executar
	1.	Certifique-se que você tem o Python 3.8+ instalado.
	2.	Clone o projeto ou baixe os arquivos.
	3.	No terminal, navegue até a pasta principal:

cd caminho/para/puzzle15

	4.	Execute o programa:

python3 main.py



⸻

🎮 Como Jogar

Ao iniciar o programa:
	•	Será solicitado o tamanho do puzzle (pressione Enter para usar o tamanho padrão 4x4).
	•	O puzzle será gerado automaticamente e embaralhado.
	•	Se a configuração inicial não for solucionável, o sistema perguntará se você deseja tentar novamente.

Durante o jogo, você pode:

Tecla	Ação
W	Mover para cima
S	Mover para baixo
A	Mover para esquerda
D	Mover para direita
B	Resolver automaticamente com BFS
M	Resolver automaticamente com A*
F	Resolver automaticamente com DFS
Q	Sair do programa



⸻

🧠 Algoritmos Implementados
	•	BFS (Breadth-First Search):
Explora todos os vizinhos primeiro. Pode demorar muito para puzzles grandes (4x4 ou mais).
	•	DFS (Depth-First Search):
Explora o caminho o mais fundo possível antes de voltar. Usado com limite de profundidade para evitar loops infinitos.
	•	A* (A-Star Search):
Algoritmo eficiente que usa a distância de mínima como heurística para guiar a busca.

⸻

⚡ Funcionalidades Adicionais
	•	Tamanho Dinâmico: O usuário pode escolher o tamanho do puzzle (3x3, 4x4, 5x5, etc.).
	•	Geração automática do estado objetivo (goal_state).
	•	Verificação de Solvabilidade: Detecta se a configuração é solucionável antes de iniciar.
	•	Serialização dos estados para controle de visitados nos algoritmos.
	•	Cópia segura de estados (deepcopy) para expandir nós.

⸻

🛠️ Tecnologias Utilizadas
	•	Python 3
	•	Numpy (para visualização de matrizes)

⸻

✨ Créditos

Projeto desenvolvido para fins educacionais, com o objetivo de demonstrar o funcionamento dos algoritmos de busca aplicados ao problema clássico do Puzzle 15.

⸻

📌 Observação

⚠️ BFS e DFS podem não ser práticos para puzzles maiores que 4x4 devido ao crescimento exponencial do espaço de estados.
⚡ Para puzzles grandes, o A* é o mais recomendado.

⸻

✅ Pronto para rodar! 🎯

⸻
