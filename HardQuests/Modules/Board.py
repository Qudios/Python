from random import randint

chars = {
    "0": "⬜",
    "1": "⬛"
}


class Board:

    def __init__(self, columns, rows):
        self.columns = columns - 1
        self.rows = rows - 1
        self.visual = ""
        self.board = []
        for y in range(columns):
            self.board.insert(y, [])
            for x in range(rows):
                self.board[y].insert(x, 0)

    def get(self):
        return self.board

    def render(self):
        self.visual = self.visual + "\n"
        for y in self.board:
            self.visual = self.visual + "\n"
            for x in y:
                self.visual = self.visual + chars[f"{x}"]
        print(self.visual)

    def pos_valid(self, x, y):
        try:
            self.board[y][x]
        except IndexError:
            return False
        return True

    def get_pos(self, x, y):
        if self.pos_valid(x, y):
            return self.board[y][x]

    def set_pos(self, x, y, alive=False):
        if self.pos_valid(x, y):
            if alive:
                self.board[y][x] = 1
            else:
                self.board[y][x] = 0
            self.render()

    def amount_of_cells(self):
        alive, dead = 0, 0
        for y in range(self.columns):
            alive += self.board[y].count(1)
            dead += len(self.board[y]) - alive
        return alive, dead

    def random_cells(self, amount):
        new_cells, tries = 0, 0
        if amount > self.rows * self.columns:
            return False
        if self.amount_of_cells()[1] < amount:
            return False
        while new_cells < amount:
            y = randint(0, self.columns)
            x = randint(0, self.rows)
            if self.board[y][x] == 0:
                self.board[y][x] = 1
                new_cells += 1
            else:
                tries += 1
                if tries > 100:
                    break

    def get_neighbours(self, x, y):
        if self.pos_valid(x, y):
            na = 0
            operations = [(1, 0), (-1, 0), (0, 1), (0, -1),
                          (1, 1), (1, -1), (-1, 1), (-1, -1)]
            for opera in operations:
                if self.pos_valid(x+opera[0], y+opera[1]):
                    if self.get_pos(x+opera[0], y+opera[1]) == 1:
                        na += 1
            return na

    def next_cell_state(self, x, y, na):
        cell = self.board[y][x]
        #  states = [()]
        if cell == 1:
            if na < 2:
                self.board[y][x] = 0
            elif na < 4:
                self.board[y][x] = 1
            else:
                self.board[y][x] = 0
        elif na == 3:
            self.board[y][x] = 1
