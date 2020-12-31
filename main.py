board= ["-", "-", "-"
        "-", "-", "-"
        "-", "-", "-"]
current_play= "X"
        
def playboard():
  print(board[0]+ "|" + board[1] + "|" + board[2])
  print(board[3]+ "|" + board[4] + "|" + board[5])
  print(board[6]+ "|" + board[7] + "|" + board[8])
  
def playgame():
  playboard()
  
def turn():
  postion= input("Chose a number from 1-9")
  position= int(position) - 1
  board[position]="X"
  
playgame()

  
