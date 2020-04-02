# CSE-512
Artificial Intelligence

//#####################//
         LAB 02
//####################//



//--------------------//
        Overview
//--------------------//

In this lab assignment, you will create a program that plays the following game.
1. The game board is an N x N grid. Columns are named A, B, C, …. (from left to right), and rows
are named 1, 2, 3, ... (from top to bottom).
2. Each player takes turns as in chess or tic-tac-toe. That is, player X takes a move, then player O,
then back to player X, and so forth.
3. Each square has a fixed point value between 1 and 99.
4. The objective of the game for each player is to score the most points. A player’s score is the
sum of the point values of his or her occupied squares minus the sum of all point values of the
squares occupied by the other player. Thus, one wants to capture the squares worth the most
points while preventing the other player from doing so.
5. The game ends when all the squares are occupied by the players since no more moves are left.
6. Players cannot pass their move, i.e., they must make a valid move if one exists.
7. Movement and adjacency relations are always vertical and horizontal but never diagonal.
8. The values of the squares can be changed for different games, but remain constant within a
game.
9. Game score is computed as the difference between (a) the sum of the values of all squares
occupied by your player and (b) the sum of the values of all squares occupied by the other
player.
10. On each turn, a player can make one of two moves: Stake or Raid

Stake – You can take any unoccupied square on the board. This will create a new piece in that square.
This move can be made as many times as one wants to during the game, but only once per turn.
However, a Stake cannot conquer enemy pieces. Once you have done a Stake, your turn is complete. 

Raid – From any square you occupy on the board, you can take the one next to it (up, down, left, right,
but not diagonally) if it is unoccupied. Thus, you get to create a new piece in the raided square. In
addition, any enemy adjacent to the raided square is conquered (that is, you turn its piece to your side).
If there are no enemies adjacent to the raided square, then no enemy pieces will be conquered. Once you
have done a Raid, your turn is complete. 


//--------------------//
   Input/Output Format
//--------------------//

Format for input.txt:
<N>
<MODE>
<YOUPLAY>
<DEPTH>
<... CELL VALUES ...>
<... BOARD STATE ...>
where
<N> is the board width and height, e.g., N=5 for the 5x5 board shown in the figures above. N is an integer strictly
greater than 0, and less than or equal to 26.
<MODE> is “MINIMAX” or “ALPHABETA”.
<YOUPLAY> is either “X” or “O” and is the player which you will play on this turn.
<DEPTH> is the depth limit of your search. By convention, the root of the search tree is at depth 0. DEPTH will
always be greater than or equal to 1.
<... CELL VALUES ...> contains N lines. In each line, there are N positive integers with space as the delimiter.
These numbers represent the value of each square.
<... BOARD STATE ...> contains N lines. In each line, there are N characters. Each character is either “X” or ”O” or
“.” to represent the state of the corresponding square as occupied by X, occupied by O, or free, respectively.
Format for output.txt:
<MOVE> <MOVETYPE>
<... NEXT BOARD STATE ...>
where
<MOVE> is your move. As in the figures above, we use capital letters for column and numbers for rows. An
example move is “F22”.
<MOVETYPE> is “Stake” or “Raid” and is the type of move that your <MOVE> is.
<... NEXT BOARD STATE ...> is the new board state after you have played your move. Same format as <... BOARD
STATE ...> in input.txt above. 



This input.txt:

3
MINIMAX
O
2
1 8 23
5 42 12
26 30 9
X..
...
...

Should yield the following output.txt:

B3 Stake
X..
...
.O.


