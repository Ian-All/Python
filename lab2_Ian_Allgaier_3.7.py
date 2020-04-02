# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 19:10:19 2020

@author: Ian Allgaier

"""
import string


file= open("input.txt")
#
cell_val=[]
board_state=[]
#Temporary values--------------------------------------
value = ''
values=''
#Filling stater variables
size=   int(file.readline())
mode=   file.readline()
player= file.readline()
player=str.rstrip(player)
depth=  file.readline()
depth = int(str.rstrip(depth))

if player == 'X':
    opponent = 'O'
else:
    opponent = 'X'
#------------------------------------------------------
#Filling Cell Values
#------------------------------------------------------
for x in range(size):
    values=(file.readline())
    for char in values:
        if char==' ' or ("\n" in char):
            cell_val+=[value]
            value=''
        else:
            value+=char
#resetting values variable so it can hold board values
values=''
#------------------------------------------------------
#Filling Board Values
#------------------------------------------------------
for x in range(size):
    values=(file.readline())
    for char in values:
        if char==' ' or ("\n" in char):
            continue
        else:
            board_state+=[str(char)]


            


#FUNCTIONS------------------------------------------------------------------------------------------------
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#---------------------------------------------------------------------------------------------------------



#Find all player locations and empty board spaces
def identify_locations(board):
    x_locations=[]
    o_locations=[]
    free_locations=[]
    index=0
    
    for i in board:
        if i=='X':
            x_locations+=[index]
        elif i=='O':
            o_locations+=[index]
        else:
            free_locations+=[index]
        index+=1
        
    return x_locations,o_locations,free_locations



#look for board edges relative to given position
#outputs list formatted as such: (Position on board,side edge, tb edge)
#'none' if no edge
def edge_finder(num1):
    num=int(num1)
    listx=[]
    side_edge=''
    tb_edge=''
    
    if (num+1)%size==1:
        side_edge='left'
    elif (num+1)%size==0:
        side_edge='right'
    else:
        side_edge='none'
    if int(num/size)==(size-1):
        tb_edge='bottom'
    elif int(num/size)== 0:
        tb_edge='top'
    else:
        tb_edge='none'
    
    listx=[str(num)]
    listx+=[str(side_edge)]
    listx+=[str(tb_edge)]
            
    return listx




#Looking at adjacent pieces--------------------------------
#takes in one board location
#Outputs indecies of surrounding board positions in order (top,left,right,bottom)
#'NA' if the position is off-board (over an edge)
    
def adjacent_check(num):
    edge = edge_finder(num)
    
    side = edge[1]
    tb = edge[2]
    index = edge[0]
    output=[]
    
    top=''
    bottom=''
    left=''
    right=''
    
    if side=='left':
        if tb=='top':
            top='NA'
            bottom=str(int(index)+size)
            left='NA'
            right=str(int(index)+1)
        elif tb=='bottom':
            top=str(int(index)-size)
            bottom='NA'
            left='NA'
            right=str(int(index)+1)
        else:
            top=str(int(index)-size)
            bottom=str(int(index)+size)
            left='NA'
            right=str(int(index)+1)
    elif side=='right':
        if tb=='top':
            top='NA'
            bottom=str(int(index)+size)
            left=str(int(index)-1)
            right='NA'
        elif tb=='bottom':
            top=str(int(index)-size)
            bottom='NA'
            left=str(int(index)-1)
            right='NA'
        else:
            top=str(int(index)-size)
            bottom=str(int(index)+size)
            left=str(int(index)-1)
            right='NA'
    else: 
        if tb=='top':
            top='NA'
            bottom=str(int(index)+size)
            left=str(int(index)-1)
            right=str(int(index)+1)
        elif tb=='bottom':
            top=str(int(index)-size)
            bottom='NA'
            left=str(int(index)-1)
            right=str(int(index)+1)
        else:
            top=str(int(index)-size)
            bottom=str(int(index)+size)
            left=str(int(index)-1)
            right=str(int(index)+1)
    
    output+=[top]
    output+=[left]
    output+=[right]
    output+=[bottom]

    
    return output
    



#Checks if a position is taken
#returns NA if pos is free, or 'X'/'O'
def chk_pos_taken(num,board):
    free_indicies= identify_locations(board)[2]
    x_indicies= identify_locations(board)[0]
    o_indicies= identify_locations(board)[1]    
    
    result ='NA'
    
    if num in free_indicies:
        return result
    else:
        if num in x_indicies:
            result ='X'
            return result
        else:
            result = 'O'
            return result
        
        
        
        
#checks the value of a given board index
# returns value of index
def value_check(num):
    index = 0
    for i in cell_val:
        if int(num) == index:
            return int(i)
        index +=1
    print('value does not exist')
    
    
#this is a funciton specifically for 'raid_possible()' function
#this function checks if a raid is already present in the return list
#returns 1 if it exists in the list, 0 if not    
def already_in_list(num, index):
    if index == []:
        return 0
    else:
        for i in index:
            if i[0]== num:
                return 1
        return 0


#Returns a list of raids formatted as such: [[position to raid, point value of raid], ...]
#If raid is not possible, function will return an empty list []
def raid_possible(player_name,board):
    result =[]
    found_raid=[]
    value = 0
    indicator = 0
	
    x_indicies= identify_locations(board_state)[0]
    o_indicies= identify_locations(board_state)[1]
    free_indicies= identify_locations(board_state)[2]
    
    if player_name == 'X':
        if x_indicies ==[]:
            return result
        else:
            for i in x_indicies:
                adj = adjacent_check(i)
                for j in adj:
                    if j == ('NA'):
                        continue
                    elif not (int(j) in free_indicies):
                        continue
                    else:
                        opponent_check= adjacent_check(j)
                        for k in opponent_check:
                            if k == ('NA' or j):
                                continue
                            else:
                                if chk_pos_taken(int(k),board) == 'O':
                                    value+=value_check(k)
                                    indicator = 1
                                else:
                                    continue
                        if indicator == 1:
                            if already_in_list(j, result):
                                indicator = 0
                                value = 0
                                found_raid=[]
                            else:
                                found_raid+=[int(j)]
                                value+= value_check(j)
                                found_raid+=[value]
                                result+=[found_raid]
                        else:
                            continue
                        indicator = 0
                        value = 0
                        found_raid=[]
    else:
        if o_indicies==[]:
            return result
        else:
            for i in o_indicies:
                adj = adjacent_check(i)
                for j in adj:
                    if j == ('NA'):
                        continue
                    elif not (int(j) in free_indicies):
                        continue
                    else:
                        opponent_check= adjacent_check(j)
                        for k in opponent_check:
                            if k == ('NA' or j):
                                continue
                            else:
                                if chk_pos_taken(int(k),board) == 'X':
                                    value+=value_check(k)
                                    indicator = 1
                                else:
                                    continue
                        if indicator == 1:
                            if already_in_list(j, result):
                                indicator = 0
                                value = 0
                                found_raid=[]
                            else:
                                found_raid+=[int(j)]
                                value+= value_check(j)
                                found_raid+=[value]
                                result+=[found_raid]
                        else:
                            continue
                        indicator = 0
                        value = 0
                        found_raid=[]

    return result

        
#Takes in a player name X or O
#returns all indicies of possible moves
#formatted as ([Raid indicies],[Stake Indicies])    
def movelist(playername,board):
    free_indicies= identify_locations(board)[2]
    raid = raid_possible(playername,board)
    listofraids=[]
    remove_list=[]
    
    for i in raid:
        listofraids+=[i[0]]
    for x in free_indicies:
        if x in listofraids:
            remove_list+=[x]
    for x in remove_list:
        for y in free_indicies:
            if x == y:
                free_indicies.remove(y)
                break
    
    return listofraids, free_indicies



#Takes player name X or O
#returns all possible moves and their values
#Formatted as ([raids],[stakes])
#([index,value]...[])
def player_move_values(playername,board): 
    index=0
    positions = movelist(playername,board)[1]
    raid_list= raid_possible(playername,board)
    stake_hold=[]
    stake_list=[]
    
    for i in positions:
        for x in cell_val:
            if i == index:
                stake_hold+=[int(i)]
                stake_hold+=[int(x)]
                
            index+=1
        index=0
        stake_list+=[stake_hold]
        stake_hold=[]
    
    return raid_list, stake_list
    


#returns the move that returns the highest point value for a given player and board            
def best_move(playername,board):
    stake_moves = player_move_values(playername,board)[1]
    raid_moves = player_move_values(playername,board)[0]
    
    if raid_moves==[]:
        highest=stake_moves[0]
    else:
        highest=raid_moves[0]

    for i in raid_moves:
        if i[1] > highest[1]:
            highest=i
    for i in stake_moves:
        if i[1]>highest[1]:
            highest=i
            
            
    return highest
        
#checks the score of a given player
def check_score(playername, board):
    x_indicies= identify_locations(board)[0]
    o_indicies= identify_locations(board)[1]
    score = 0

    if playername == 'X':
        for i in x_indicies:
            score+= value_check(i)
    else:
        for i in o_indicies:
            score+= value_check(i) 
    return score

#returns new board showing captured positions
def capture(playername,board,capindex,cap_type):

    index = 0
    indicator = 0
    
    positions = adjacent_check(capindex)
    capture_points=[]
    new_board=[]
    
    if cap_type == 'R':
        capture_points+=[str(capindex)]
        for i in positions:
            if i == 'NA':
                continue
            elif chk_pos_taken(int(i),board) == playername:
                continue
            else:
                if chk_pos_taken(int(i),board) == 'NA':
                    continue
                else:
                    capture_points+=[i]
        
        for i in board:
            for j in capture_points:
                if str(index) == j:
                    new_board+=playername
                    indicator = 1
            if indicator == 0:
                new_board+=i
            indicator=0
            index+=1
    else:
        for i in board:
            if index==capindex:
                new_board+=[playername]
            else:
                new_board+=[board[index]]
            index+=1
            
    return new_board
    


#returns list of possible moves ordered by index (low->high)
#format: [[index,value,R/S],...]
def ordered_moves(playername, board):
    holdlist=[]
    raids =player_move_values(playername,board)[0]
    stakes= player_move_values(playername,board)[1]
    
    for i in raids:
        i.append('R')
        holdlist+=[i]
    for i in stakes:
        i.append('S')
        holdlist+=[i]
    
    return (sorted(holdlist,key=lambda x:x[0]))
    

#def algorithm(playername,board):
#    player1 = playername
#    player2 = ''
#    if player1 =='X':
#        player2 = 'O'
#    else:
#        player2 = 'X'
#    
#    og_set = ordered_moves(playername, board)
#    
#    player1_total= 0
#    player2_total= 0
#    
#    player1_best_move=[]
#
#    for i in og_set:
#        board1 = capture(playername,board,i[0],i[2])
#        if check_score(player1, board1) > player1_total:
#            player1_total = check_score(player1, board1)
#            player2_total= check_score(player2, board1)
#            player1_best_move = [i]
#                


#big boi algorithm
def minimax(playername,board,depth,maximizing): 
    moves = ordered_moves(playername,board)
    if depth == 0:
        val = check_score(player,board)
        return val , []
    
    elif maximizing:
        value = -1000000000000
        solution=[]
        for moveblock in moves:
            brd= capture(playername,board,moveblock[0],moveblock[2])
            bcopy=brd.copy()
            new_value= minimax(opponent,bcopy,depth-1,0)[0]
            if int(new_value) > int(value):
                value = new_value
                solution = moveblock
        return value, solution
    else:
        value = 1000000000000
        solution=[]
        for moveblock in moves:
            brd= capture(playername,board,moveblock[0],moveblock[2])
            bcopy=brd.copy()
            new_value= minimax(player,bcopy,depth-1,0)[0]
            if int(new_value) < int(value):
                value = new_value
                solution = moveblock
        return value, solution
    
    return value, solution

    

#print(minimax(player,board_state,depth,1))
    

new_cap = minimax(player,board_state,depth,1)
alphabet_string = string.ascii_uppercase
alphabet_list = list(alphabet_string)
#print(alphabet_list)
#print(new_cap[1][0])
#print(new_cap[1][2])
#print(player)

cindex=new_cap[1][0]
ctype=new_cap[1][2]

new_board= capture(player, board_state,int(cindex) , ctype)

#print(new_board)
    

lindex = cindex % size
letter = alphabet_list[lindex]

height = int(cindex / size) + 1

label = ''
if ctype == 'S':
    label = 'Stake'
else:
    label = 'Raid'

header = str(letter)+str(height)+' '+label+'\n'


file1 = open("output.txt","w")

def divide_chunks(l, n): 
    for i in range(0, len(l), n):  
        yield l[i:i + n] 
  
x = list(divide_chunks(new_board, size)) 

thestring=''

file1.write(header)
for i in x:
    for j in i:
        thestring+=str(j)
    thestring+='\n'
    file1.write(thestring)
    thestring=''
    
file1.close()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    

