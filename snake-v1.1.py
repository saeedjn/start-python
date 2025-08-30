import random
import os
import time
import msvcrt

rows = 15
cols = 15

board = [[" " for _ in range(cols)] for _ in range(rows)]
snake = [(7,7),(7,6),(7,5)]
food = (random.randint(0,rows-1), random.randint(0,cols-1))



for r in range(rows) :
    row_str = ""
    for c in range(cols) :
        if (r,c) in snake:
            row_str += "o"
        elif (r,c) == food : 
            row_str += "*"
        else : 
            row_str += " "
    print(row_str)

def draw_board(snake,food) :
    os.system("cls")
    for r in range(rows) :
        row_str = ""
        for c in range(cols) :
            if (r,c) in snake:
                row_str += "o"
            elif (r,c) == food : 
                row_str += "*"
            else : 
                row_str += " "
        print(row_str)


while True :
    direction = input().lower()
    head_row, head_col = snake[0]
    if direction == "w" : 
        new_head = (head_row - 1, head_col)
        if new_head in snake or not ( 0 <= new_head[0] < rows) or not ( 0 <= new_head[1] < cols) :
            print("Game Over")
            break
        snake.insert(0, new_head)
        if new_head != food :
            snake.pop()
        else : 
            food = (random.randint(0,rows-1), random.randint(0,cols-1))
        draw_board(snake,food)
    elif direction == "s": 
        new_head = (head_row + 1, head_col)
        if new_head in snake or not ( 0 <= new_head[0] < rows) or not ( 0 <= new_head[1] < cols) :
            print("Game Over")
            break
        snake.insert(0, new_head)
        if new_head != food :
            snake.pop()
        else : 
            food = (random.randint(0,rows-1), random.randint(0,cols-1))
        draw_board(snake,food)
    elif direction == "d" :
        new_head = (head_row, head_col + 1)
        if new_head in snake or not ( 0 <= new_head[0] < rows) or not ( 0 <= new_head[1] < cols) :
            print("Game Over")
            break
        snake.insert(0, new_head)
        if new_head != food :
            snake.pop()
        else : 
            food = (random.randint(0,rows-1), random.randint(0,cols-1))
        draw_board(snake,food)
    elif direction == "a" :
        new_head = (head_row, head_col - 1)
        if new_head in snake or not ( 0 <= new_head[0] < rows) or not ( 0 <= new_head[1] < cols) :
            print("Game Over")
            break
        snake.insert(0, new_head)
        if new_head != food :
            snake.pop()
        else : 
            food = (random.randint(0,rows-1), random.randint(0,cols-1))
        draw_board(snake,food)
    else : continue        