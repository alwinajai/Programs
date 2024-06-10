tictac=[" " for x in range(9)]
def des():
    row1=f"| {tictac[0]} | {tictac[1]} | {tictac[2]} |"
    row2=f"| {tictac[3]} | {tictac[4]} | {tictac[5]} |"
    row3=f"| {tictac[6]} | {tictac[7]} | {tictac[8]} |"
    print()
    print(row1)
    print(f'-------------')
    print(row2)
    print(f'-------------')
    print(row3)
    print()
def move(inp):
        try:
            if inp=="X":
                number=1
            elif inp=="O":
                number=2
            print("Options:")
            print("|1|2|3|")
            print("|4|5|6|")
            print("|7|8|9|")
            print(f"Your turn player {number}")
            choice = int(input("Enter your move (1-9): "))
            if tictac[choice-1]==" ":
                tictac[choice-1]=inp
            else:
                print()
                print("That space is already occupied!")
                move(inp)
        except (IndexError,ValueError):
            print("Invalid input. Please enter a value between 1 and 9")
            move(inp)
def win(icon):
    if (tictac[0]==icon and tictac[1]==icon and tictac[2]==icon) or (tictac[3]==icon and tictac[4]==icon and tictac[5]==icon) or (tictac[6]==icon and tictac[7]==icon and tictac[8]==icon) or (tictac[0]==icon and tictac[3]==icon and tictac[6]==icon) or (tictac[1]==icon and tictac[4]==icon and tictac[7]==icon) or (tictac[2]==icon and tictac[5]==icon and tictac[8]==icon) or (tictac[0]==icon and tictac[4]==icon and tictac[8]==icon) or (tictac[2]==icon and tictac[4]==icon and tictac[6]==icon):
        return True
    else:
        return False
def draw():
    if " " not in tictac:
        return True
    else:
        return False
while True:
    des()
    move("X")
    des()
    if win("X"):
        print("P1 wins the game")
        break
    elif draw():
        print("Draw")
        break
    move("O")
    if win("O"):
        des()
        print("P2 wins the game")
        break
    elif draw():
        print("Draw")
        break