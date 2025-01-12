board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
current_play = "X"

def playboard():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

def turn():
    global current_play   
    position = input(f"{current_play}'s turn! Choose a position from 1-9: ")
    position = int(position) - 1
    if board[position] == "-":
        board[position] = current_play
        playboard()
        current_play = "O" if current_play == "X" else "X"   
    else:
        print("Position already taken. Try again!")
        turn()  

def playgame():
    playboard()
    for _ in range(9):   
        turn()
    print("Game over!")

playgame()
