import random
global state
state = [[0 for _ in range(4)] for _ in range(4)]


score = 0

def show(board):
  for i in board:
    print(i)
    print()

def reverse():
  for i in range(4):
    for j in range(3):
      state[i][j], state[i][3-j] = state[i][3-j], state[i][j]

def left_combine(state):
    for i in range(4):
      for j in range(3):
        
        
        if state[i][j] == state[i][j+1]:
          state[i][j] *= 2
          state[i][j+1] = 0
    return state
  
  


def left():


  for i in range(4):

    list_counter = 0
    for j in range(3):
      if state[i][j] == state[i][j+1]:
        state[i][j] *= 2
        state[i][j+1] = 0
  

    for j in range(4):
      if state[i][j] != 0:
        state[i][list_counter] = state[i][j]
        list_counter += 1
  
    for j in range(list_counter, 4):
      state[i][j] = 0



def right():
  reverse()
  left()
  reverse()

def upward_down_reverse():
  for j in range(4):
    for i in range(2):
      state[i][j], state[3-i][j] = state[3-i][j], state[i][j]
      
  
def upward_combine(state):
  for j in range(4):
    for i in range(3):
      
      
      if state[i][j] == state[i+1][j]:
        state[i][j] *= 2
        state[i+1][j] = 0
        
  return state


def up():


  for j in range(4):

    list_counter = 0

    for i in range(3):
    
    
      if state[i][j] == state[i+1][j]:
        state[i][j] *= 2
        state[i+1][j] = 0
    

    for i in range(4):
      if state[i][j] != 0:
        state[list_counter][j] = state[i][j]
        list_counter += 1
  
    for i in range(list_counter, 4):
      state[i][j] = 0

def down():
  upward_down_reverse()
  up()
  upward_down_reverse()

        
          
          
          
          
        

# def down():
#   for i in range(1, 4):
#     for j in range(4):
#       if state[i-1][j] != 0 or state[i][j] == state[i-1][j]:
#           state[i][j] += state[i-1][j]
#           state[i-1][j] = 0

# def left():
#   for i in range(4):
#       for j in range(3):
#         if state[i][j+1] != 0 or state[i][j] == state[i][j+1]:
#           state[i][j] += state[i][j+1]
#           state[i][j+1] = 0

# def right():
#   for i in range(4):
#     for j in range(1, 4):
#       if state[i][j-1] != 0 or state[i][j] == state[i][j-1]:
#           state[i][j] += state[i][j-1]
#           state[i][j-1] = 0

def rand_gen():
  while True:
    a = random.randint(0, 3)
    b = random.randint(0, 3)
    
    l = [2, 4]

    if state[a][b] == 0:
      state[a][b] = l[random.randint(0, 1)]
      break

    else:
      continue

  return

def checker(board):
  temp = board

  if upward_combine(board) == temp and left_combine(board) == temp:
    return False
  return True

  
  
    
    
    
          




  
a = random.randint(0, 3)
b = random.randint(0, 3)

l = [2, 4]

state[a][b] = l[random.randint(0, 1)]

show(state)


def game():
  while True:
   
    
    
  
    print("--------------------------------------------------")
  
    choice = input("up, down, left or right: ")
    
    if choice == "w":
      up()
    elif choice == "s":
      down()
    elif choice == "a":
      left()
    else:
      right()
  
    # if keyboard.is_pressed('w'):
    #   up()
  
  
    rand_gen()
    show(state)
  
    if not checker(state):
      game()

  

    print("\nScore: " + str(score))
  
  

game()
  

  
  