#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 15:06:32 2020

@author: evenmyrennybo
"""
import random

def createBoard(size):
    #make an empty list
    board = []
    #make a loop that have en empty loop inside of it
    for i in range(size):
        iLoop = []
        #make a loop that put empty strings into the list in the first loop.
        for b in range(size):
            space = ' '
            iLoop.append(space)
        #append the list into the first list so you get x amount of empty strings in x amount og lists
        board.append(iLoop)
    
    return board  
    

def printBoard(board):
    #make a headliner
    print('\n')
    print('Tik Tac Board')
    
    #find the rows in board
    row = len(board)
    #use a loop to find what to append into the board
    for r in range(row):
        
        emptyStr = ''
        
        col = len(board[r])
        #formate the board and make the board
        for c in range(col):
            emptyStr += '|' + board[r][c] 
        print('-'+('-'*len(board))*2) #make the 
         
        print(emptyStr + '|')
    print('-'+('-'*len(board))*2)
    
    
    
        
def getMoves(size):
    #ask for placements from the user and return them are not out of range
    x = int(input('Please enter the x coordinate: '))
    y = int(input('Please enter the y coordinate: '))
    #use if and else sentence to find if it is  out of range
    if x < len(size) and y < len(size):
        return x,y
        
    else:
        print('Invalid coordinates. Try again!')
        #runs the getMoves if the spot is out of range
        getMoves(size)
        
def userPlay(x,y,board):
    
    #convert an empty string into an 'O' if spot is available 
    if board[x][y] == ' ':
        board[x][y] = 'O'
        
        #call the printBoard function
        printBoard(board)
        
    else: 
        #if spot is taken call getMoves function
        print('Spot is taken. Choose a new spot')
        getMoves(board)
    return board 

    
    
def computerPlay(board):
    
    
    #find two random coordinates
    r1 = random.randint(0,(len(board) - 1))
    r2 = random.randint(0,(len(board) - 1))
    
    
    #if the coordinates is available, convert the empty sting into a 'X'
    if board[r1][r2] == ' ':
        board[r1][r2] = 'X'
        printBoard(board)
        
    else:
        #if it is taken, ask the computer for a new value
        computerPlay(board)
    return board

def checkRows(x, board):
    #seperating every list and reads if it is the same 
    for row in board:
        #checks if every symbol is the same
        if all(i == x for i in row):
            print('The winner is', x) #prints the winner
            return #exit the program
            
            
def checkCols(x, board):
    #checking in the colons are the same symbols 
   for i in range(len(board)):
        #looking through every colon for having the same symbol
        if all(board[j][i] == x for j in range(len(board))):
            print('The winner is', x) #prints the winner
            exit() #exit the program
            
            
def checkDiag_1(x, board):
    #checking diagonals from left to right 
    if all(board[i][i] == x for i in range(len(board))):
        print('The winner is', x) #prints the winner
        return #exits the program
        
        
def checkDiag_2(x, board):
    #using a while loop to reverse the diagonal so it works the from right to left
    i = 0
    j = 2
    list_diag = [''] * len(board)
    while i < len(board):
        list_diag[i] = board[i][j]
        i += 1
        j -= 1
        #checks every reverse diagonal to check if they are the same symbol
    if all(list_diag[count] == x for count in range(len(list_diag))):
        print('The winner is', x)
        return
        
def valEmptySpace(board):
    
    #if the board doesn't get any winner we will return a tie result
    value = 0
    for row in board: 
        for col in row:
            if col != ' ':
                value += 1
            if value == len(board) ** 2:
                print('No valid places to insert, result is a draw')
                return


def whoWon(x, boardList):
    
    #checking every possible way of winning 
    checkRows(x, boardList)
    checkCols(x, boardList)
    checkDiag_1(x, boardList)
    checkDiag_2(x, boardList)
    valEmptySpace(boardList)


def main ():
    
    size = 3
    boardList = createBoard(size)
    printBoard(boardList)
    #use the while loop so it will run until we have a winner.
    while size != 0:
        x,y = getMoves(boardList)
        newBoard = userPlay(x,y, boardList)
        whoWon('O', boardList)
        computerPlay(newBoard)
        whoWon('X', boardList)
    
    return

main()
