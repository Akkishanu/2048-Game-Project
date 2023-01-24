#!/usr/bin/env python
# coding: utf-8

# In[11]:


import random

# To start the game we need a 4X4 matrix
def start_game():
    mat = [[0]*4 for i in range(4)]
    return mat





# To add new 2 after every move
def add_new_2(mat):
    r = random.randint(0,3)
    c = random.randint(0,3)
    while mat[r][c] != 0:
        r = random.randint(0,3)
        c = random.randint(0,3)
    mat[r][c] = 2
    
    
    
    
    
    
# To get the current state of the Game
def get_current_state(mat):
    
    # Anywhere 2048 is present
    for i in range(4):
        for j in range(4):
            if mat[i][j]==2048:
                return 'WON'
            
    # Anywhere 0 is present
    for i in range(4):
        for j in range(4):
            if mat[i][j]==0:
                return 'GAME NOT OVER'
            
    # Check every row and col except last row and last col for same num at adjacent places
    for i in range(3):
        for j in range(3):
            if mat[i][j]==mat[i+1][j] or mat[i][j]==mat[i][j+1]:
                return 'GAME NOT OVER'
            
    # Check last row for same num at adjacent places
    for j in range(3):
        if mat[3][j]==mat[3][j+1]:
            return 'GAME NOT OVER'
        
    # Check last col for same num at adjacent places
    for i in range(3):
        if mat[i][3]==mat[i+1][3]:
            return 'GAME NOT OVER'
        
    # Means you lost the game
    return 'LOST'




# To compress the element of mat according to left move
def compress(mat):
    changed = False
    new_mat = [[0]*4 for i in range(4)]
    for i in range(4):
        pos = 0
        for j in range(4):
            if mat[i][j] != 0:
                new_mat[i][pos] = mat[i][j]
                if j != pos:
                    changed = True
                pos += 1
    return new_mat, changed





# To merge the same numbers acording to left move
def merge(mat):
    changed = False
    for i in range(4):
        for j in range(3):
            if mat[i][j] != 0 and mat[i][j] == mat[i][j+1]:
                mat[i][j] = mat[i][j] * 2
                mat[i][j+1] = 0
                changed = True
    return mat, changed
                
                
                
                
                
                
# To reverse the mat
def reverse(mat):
    for i in range(4):
        mat[i] = mat[i][::-1]
    return mat





# To transpose the mat
def transpose(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i])
    return new_mat





# All possible moves in 2048 game
# Left Move:
#    (1) Compress
#    (2) Merge
#    (3) Compress
    
# Right Move:
#    (1) Reverse
#    (2) Compress
#    (3) Merge
#    (4) Compress
#    (5) Reverse
    
# Up Move:
#    (1) Transpose
#    (2) Compress
#    (3) Merge
#    (4) Compress
#    (5) Transpose
    
# Down Move:
#    (1) Transpose
#    (2) Reverse
#    (3) Compress
#    (4) Merge
#    (5) Compress
#    (6) Reverse
#    (7) Transpose


def move_down(grid):
    transposed_grid = transpose(grid)
    reversed_grid = reverse(transposed_grid)
    new_grid, changed1 = compress(reversed_grid)
    new_grid, changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid, temp = compress(new_grid)
    final_reversed_grid = reverse(new_grid)
    final_grid = transpose(final_reversed_grid)
    return final_grid, changed

def move_up(grid):
    transposed_grid = transpose(grid)
    new_grid, changed1 = compress(transposed_grid)
    new_grid, changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid, temp = compress(new_grid)
    final_grid = transpose(new_grid)
    return final_grid, changed

def move_right(grid):
    reversed_grid = reverse(grid)
    new_grid, changed1 = compress(reversed_grid)
    new_grid, changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid, temp = compress(new_grid)
    final_grid = reverse(new_grid)
    return final_grid, changed

def move_left(grid):
    new_grid, changed1 = compress(grid)
    new_grid, changed2 = merge(new_grid)
    changed = changed1 or changed2
    final_grid, temp = compress(new_grid)
    return final_grid, changed


# In[ ]:





# In[ ]:




