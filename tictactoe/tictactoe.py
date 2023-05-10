print("X O X")
print("O X O")
print("X X O")


def print_game_field(cells):
    print("---------")
    print("|", cells[0], cells[1], cells[2], "|")
    print("|", cells[3], cells[4], cells[5], "|")
    print("|", cells[6], cells[7], cells[8], "|")
    print("---------")

def analyze_game(cells):
    rows = [cells[:3], cells[3:6], cells[6:]]
    cols = [cells[i::3] for i in range(3)]
    diags = [[cells[0], cells[4], cells[8]], [cells[2], cells[4], cells[6]]]
    x_wins = False
    o_wins = False
    for row in rows + cols + diags:
        if row.count('X') == 3:
            x_wins = True
        elif row.count('O') == 3:
            o_wins = True
    x_count = cells.count('X')
    o_count = cells.count('O')
    empty_count = cells.count('_')
    diff = abs(x_count - o_count)
    if x_wins and o_wins or diff >= 2:
        return "Impossible"
    elif x_wins:
        return "X wins"
    elif o_wins:
        return "O wins"
    elif empty_count > 0:
        return "Game not finished"
    else:
        return "Draw"

cells = list("_________")
print_game_field(cells)

current_player = 'X'
while analyze_game(cells) == "Game not finished":
    try:
        row, col = map(int, input(f"Enter the coordinates for {current_player}: ").split())

        if row < 1 or row > 3 or col < 1 or col > 3:
            print("Coordinates should be from 1 to 3!")
            continue

        index = (row - 1) * 3 + (col - 1)

        if cells[index] != "_":
            print("This cell is occupied! Choose another one!")
            continue

        cells[index] = current_player
        print_game_field(cells)

        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'

    except ValueError:
        print("You should enter numbers!")
        continue

print(analyze_game(cells))
