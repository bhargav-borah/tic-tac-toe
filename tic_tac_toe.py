order = 3

game_map = [["." for i in range(order)] for j in range(order)]

def map_filled():
    count = 0
    for row in game_map:
        count += row.count(".")
    if count == 0:
        return True
    return False
        
def display(game_map):
    print(end = "  ")
    for col_num in range(len(game_map[0])):
        print(col_num+1, end = " ")
    print()
    for row_num, row in enumerate(game_map):
        print(row_num+1, end = " ")
        for num in row:
            print(num, end = " ")
        print()
    print()

#Row-wise check
def check_for_row_triad():
    
    for row in game_map:
        if(row.count(symb1) == order):
            print("Player 1 wins!")
            return True
        elif row.count(symb2) == order:
            print("Player 2 wins!")
            return True
    return False

#Column-wise check
def check_for_col_triad():

    for col in range(order):
        lst = []
        for row in range(order):
            lst.append(game_map[row][col])
        if lst.count(symb1) == order:
            print("Player 1 wins")
            return True
        elif lst.count(symb2) == order:
            print("Player 2 wins")
            return True
    return False

#Diagonal-wise check
def check_for_diagonal_triad():

    lst = []
    for i in range(order):
        lst.append(game_map[i][i])
    if lst.count(symb1) == order:
        print("Player 1 wins!!!")
        return True
    elif lst.count(symb2) == order:
        print("Player 2 wins!!!")
        return True

    lst.clear()
    for i in range(order):
        lst.append(game_map[i][order-1-i])
    if lst.count(symb1) == order:
        print("Player 1 wins!!!")
        return True
    elif lst.count(symb2) == order:
        print("Player 2 wins!!!")
        return True
        
    return False

def winner_found():
    return check_for_row_triad() or check_for_col_triad() or check_for_diagonal_triad()

def play(player_num, symb):
    print(f"Player {player_num}: ")
    display(game_map)
    while True:
        while True:
            row = input("Enter row no.: ")
            try:
                if int(row)-1 not in range(order):
                    print("Enter valid row position")
                else:
                    row = int(row)
                    row -= 1
                    break
            except:
                print("Enter valid input")
           
        while True:
            col = input("Enter column no.: ")
            try:
                if int(col)-1 not in range(order):
                    print("Enter valid column position")
                else:
                    col = int(col)
                    col -= 1
                    break
            except:
                print("Enter valid input")
   
        if game_map[row][col] == ".":
           game_map[row][col] = symb
           break
        else:
           print("This position is already occupied. Try another position")

    print()
    display(game_map)
   
   
while True:
    symb1 = input("Enter the symbol for player 1 (o/x): ").lower()
    if symb1 in ["x", "o"]:
        break
    else:
        print("Enter valid input")

symb2 = "o"
if symb1 == "o":
    symb2 = "x"
   
print(f"Player1: {symb1} || Player2: {symb2}")
print()

while True:

    play(1, symb1)
    if winner_found():
        break
    if map_filled():
        print("The game board is filled. The game is drawn")
        break

    play(2, symb2)
    if winner_found():
        break
    if map_filled():
        print("The game board is filled. The game is drawn")
        break
