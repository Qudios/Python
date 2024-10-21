from Modules.Board import Board
import time

start = time.time()
board = Board(11, 50)
board.random_cells(100)
board.render()
end = time.time()
print(end - start)
