board = [
  [7,8,0,4,0,0,1,2,0],
  [6,0,0,0,7,5,0,0,9],
  [0,0,0,6,0,1,0,7,8],
  [0,0,7,0,4,0,2,6,0],
  [0,0,1,0,5,0,9,3,0],
  [9,0,4,0,6,0,0,0,5],
  [0,7,0,3,0,0,0,1,2],
  [1,2,0,0,0,7,4,0,0],
  [0,4,9,2,0,6,0,0,7],
]

def valid(board, num, pos):
  #Check row
  for i in range(len(board[0])):
    if board[pos[0]][i] == num and pos[1] != i:
      return False
  #Check column
  for i in range(len(board)):
    if board[i][pos[1]] == num and pos[0] != i:
      return False
  #Check box
  box_x = pos[1] // 3
  box_y = pos[0] // 3

  for x in range(box_y * 3, box_y *3+3):
    for y in range (box_x*3, box_x *3+3):
      if board[x][y] == num and (x, y) != pos:
        return False
  return True

def solve(board):
  find = findEmpty(board)
  if not find:
    return True
  else:
    row, column = find
  for x in range(1, 10):
    if valid(board, x, (row, column)):
      board[row][column] = x

      if solve(board):
        return True

      board[row][column] = 0
  return False

def displayBoard(board):
  for x in range(len(board)):
    if x%3 == 0 and x != 0:
      print("-------------------------")
    for y in range(len(board[x])):
      if y%3 == 0 and y != 0:
        print(" | ", end="")
      if y==8:
        print(board[x][y])
      else:
        print(str(board[x][y]) + " ", end = "")
        
def findEmpty(board):
  for x in range(len(board)):
    for y in range(len(board[x])):
      if board[x][y] == 0:
        return (x, y) #row, column
  return None


displayBoard(board)
solve(board)
print("----------------------------------")
displayBoard(board)

