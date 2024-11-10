from random import randrange

MAX_X = 20
MAX_Y = 50


class Snake:
    parts = []

    def __init__(self, coord, d):
        self.x = coord[0]
        self.y = coord[1]
        self.d = d
        Snake.parts.append(self)

    def coord(self):
        return (self.x, self.y)

    def move(self, d):
        match d:
            case 0:
                self.x -= 1
            case 1:
                self.y += 1
            case 2:
                self.x += 1
            case 3:
                self.y -= 1
            case _:
                self.move(self.d)

    def __repr__(self):
        return str(self.coord())


dirs = ['w', 'd', 's', 'a', '']

Snake((5, 2), 1)

fruit = (randrange(MAX_X), randrange(MAX_Y))
while fruit == (5, 2):
    fruit = (randrange(MAX_X), randrange(MAX_Y))

win = 0
end = 0
while not end:
    snake_bits = [part.coord() for part in Snake.parts]

    print('=' * MAX_Y)
    for x in range(MAX_X):
        line = ''
        for y in range(MAX_Y):
            if (x, y) in snake_bits:
                line += '@'
            elif (x, y) == fruit:
                line += 'O'
            else:
                line += '.'
        print(line)

    last_cord = Snake.parts[-1].coord()
    last_d = Snake.parts[-1].d

    valid = 0
    next_d = ''
    while not valid:
        next_d = 'o'
        while next_d not in dirs:
            next_d = input('> ')
            if next_d:
                next_d = next_d[0].lower()

        next_d = dirs.index(next_d)

        if next_d == 4 or (next_d + 2) % 4 != Snake.parts[0].d:
            valid = 1

    for part in Snake.parts:
        part.move(next_d)

        if part.x < 0 or part.y < 0 or part.x > MAX_X - 1 or part.y > MAX_Y - 1:
            end = 1
            break

        temp = part.d
        if next_d < 4:
            part.d = next_d
        next_d = temp
    else:
        snake_bits.pop()

        if Snake.parts[0].coord() in snake_bits:
            end = 1
            continue

        snake_bits = [part.coord() for part in Snake.parts]

        i = 0
        while fruit in snake_bits and i <= MAX_X * MAX_Y:
            if i == 0:
                Snake(last_cord, last_d)
                first = 0
            fruit = (randrange(MAX_X), randrange(MAX_Y))
            i += 1

        if i == MAX_X * MAX_Y:
            win = 1
            end = 1

if win:
    print('Winner!')
else:
    print('Game Over!')
