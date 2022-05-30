#本游戏python3.4.0下编写调试,只能在windows下运行。
import random
import subprocess
import time
#定义函数
def draw_board(the_board):
 subprocess.call("cls", shell = True)
 print('  -------\n' + '  |' + the_board[9] + '|' + the_board[8] + '|' + the_board[7] + '|\n' + '  -------\n' + '  |' + the_board[6] + '|' + the_board[5] + '|' + the_board[4] + '|\n' + '  -------\n' + '  |' + the_board[3] + '|' + the_board[2] + '|' + the_board[1] + '|\n' + '  -------')
def input_player_letter():
 letter = ' '
 while not (letter == 'X' or letter == 'O'):
  print('请选择X或O作棋子：', end = '')
  letter = input().upper()
 if letter == 'X':
  return ['X', 'O']
 else:
  return ['O', 'X']
def who_first():
 if 1 == random.randint(1, 2):
  return 'computer'
 else:
  return 'player'
def is_again():
 print('再一次？(Yes or No)')
 return input().lower().startswith('y')
def is_space_free(the_board, move):
 return the_board[move] == ' '
def choose_random_from_list(the_board, move_from_list):
 possible_moves = []
 for i in move_from_list:
  if is_space_free(the_board, i):
   possible_moves.append(i)
 if len(possible_moves) != 0:
  return random.choice(possible_moves)
 else:
  return None
def make_move(the_board, the_letter, the_move):
 the_board[the_move] = the_letter
def get_board_copy(the_board):
 duplicated_board = []
 for i in board:
  duplicated_board.append(i)
 return duplicated_board
def is_board_full(the_board):
 for i in range(1, 9):
  if is_space_free(the_board, i):
   return False
 else:
  return True
def get_player_move(the_board):
 the_move = 0
 while the_move not in list(range(1, 9)) or not is_space_free(the_board, the_move):
  print('请输入走步：', end = '')
  the_move = int(input())
 return the_move
def is_winner(the_board, the_letter):
 return (the_board[1] == the_letter and the_board[2] == the_letter and the_board[3] == the_letter) or (the_board[4] == the_letter and the_board[5] == the_letter and the_board[6] == the_letter) or (the_board[7] == the_letter and the_board[8] == the_letter and the_board[9] == the_letter) or (the_board[1] == the_letter and the_board[5] == the_letter and the_board[9] == the_letter) or (the_board[2] == the_letter and the_board[5] == the_letter and the_board[8] == the_letter) or (the_board[3] == the_letter and the_board[5] == the_letter and the_board[7] == the_letter) or (the_board[1] == the_letter and the_board[4] == the_letter and the_board[7] == the_letter) or (the_board[2] == the_letter and the_board[5] == the_letter and the_board[8] == the_letter) or (the_board[3] == the_letter and the_board[6] == the_letter and the_board[9] == the_letter)
def get_computer_move(the_board, computer_letter):
 global player_letter
 global move
 if player_letter == 'X':
  computer_letter = 'O'
 else:
  player_letter = 'O'
  computer_letter = 'X'
 #虚拟棋盘查看是否自己可一步得胜
 for i in range(1,9):
  copy = get_board_copy(board)
  if is_space_free(board, i):
   make_move(copy, computer_letter, i)
   if is_winner(copy, computer_letter):
    return i
 #虚拟棋盘查看是否对手可一步得胜
 for i in range(1,9):
  if is_space_free(board, i):
   copy = get_board_copy(board)
   make_move(copy, player_letter, i)
   if is_winner(copy, player_letter):
    return i
 move = choose_random_from_list(board, [1, 3, 7, 9])
 if move != 0:
  return move
 if is_space_free(board, 5):
  return 5
 return choose_random_from_list(board, [2, 4, 6, 8, 7])
print('欢迎玩 井字棋 游戏！')
time.sleep(1)
print('''▆▅▅▅▆▅▅▅▅▅▅▅▂▅▅▅▆▆▅▅▃▂▆▅▅▅▅▅▅▅▅
▆▆▆▃▂▆▆▅▃▄▆▅▂▅▆▇▇▆▆▆▄▂▆▆▆▆▆▆▆▆▅
▆▅▆▅　▁▅▂▃▅▆▅▂▆▆▇▆▅▆▇▄▂▆▆▆▆▆▆▆▆▅
▆▅▆▆▅　　▃▆▅▆▅▂▆▇▆▅▅▆▇▅▂▆▆▆▆▆▆▆▆▅
▆▆▆▆▆▃　▁▅▆▆▄▂▇▇▆▅▅▆▇▅▁▆▆▆▆▆▆▆▆▅
▆▅▆▆▃▂▃▁▁▅▆▄▂▇▇▆▅▆▇▇▅▂▆▆▆▅▅▅▅▅▅
▆▅▆▃▁▅▆▃▁▁▅▅▂▆▇▆▆▇▆▆▄▂▆▅▅▅▅▅▆▆▅
▆▅▆▄▅▆▆▆▄▂▂▃▃▆▆▇▇▆▆▆▅▂▆▆▆▆▆▆▆▆▆
▆▅▄▄▄▄▄▄▄▄▃　▂▅▄▄▃▄▄▄▃▂▅▄▄▅▅▅▅▅▅
▆▅▂▂▂▂▃▃▃▃▃▂　▁▃▂▃▃▃▃▂　▂▃▂▃▃▃▃▃▅
▆▅▆▆▆▇▇▇▇▆▆▅▂▁▄▆▆▆▄▅▄▂▆▆▆▆▆▆▆▆▅
▆▅▆▅▆▇▆▆▆▆▆▄▄▄　▃▆▂▂▅▄▂▆▅▅▆▅▅▆▆▅
▆▅▅▆▆▇▆▅▆▇▆▄▃▆▂　▂▃▅▆▄▂▆▅▅▅▅▅▅▆▅
▆▅▅▆▇▆▅▅▆▇▇▄▃▆▅▂　▃▆▅▄▂▆▅▅▅▅▅▆▆▅
▆▅▅▆▇▆▅▆▆▇▆▃▂▆▄▂▂▁▃▆▅▂▆▅▅▆▆▆▆▆▅
▆▅▆▆▇▆▆▇▇▆▆▄▂▄▁▄▅▂▁▂▅▂▆▅▆▆▆▆▆▆▅
▆▅▅▆▆▆▇▆▆▆▆▄▁▃▄▆▆▄▂▁▁▂▆▅▅▆▆▆▆▆▅
▆▅▂▂▂▂▃▂▂▂▂▂▁▃▃▃▃▂▁▁　　▂▂▂▂▂▂▃▄▅
▆▆▆▆▆▅▅▅▅▅▅▄▁▅▅▅▅▄▅▅▄　▁▅▆▅▅▅▅▆▆
▆▆▆▆▆▆▆▆▆▆▆▅▂▆▆▆▆▆▆▆▄▂▃▂▆▆▆▆▅▅▆
▆▆▆▆▆▆▆▆▆▆▆▅▂▆▆▆▆▆▆▆▄▂▆▂▁▅▆▃▃▆▆
▆▆▆▆▆▆▆▆▆▆▆▄▂▆▆▆▆▆▆▆▄▂▆▅▁▁▃▂▅▆▆
▆▆▆▆▆▆▆▆▆▆▆▄▃▆▆▆▆▆▆▆▄▃▆▆▄▁　▅▇▆▅
▆▆▆▆▆▆▆▆▆▆▆▄▂▆▆▆▆▆▆▆▄▃▆▆▄▁▁▁▅▆▅
▆▆▆▆▆▆▆▆▆▆▆▄▂▆▆▆▆▆▆▆▄▃▆▄▂▄▃▁　▅▆
▆▆▆▆▆▆▆▆▆▆▆▅▃▆▆▆▆▆▆▆▅▃▅▁▄▆▆▃▁　▄
▆▆▆▆▆▆▆▆▆▆▆▅▄▆▆▆▆▆▆▆▄▃▆▅▆▆▆▆▄▃▂''')
time.sleep(2)
subprocess.call("cls", shell = True)
while True:
 board = [' '] * 10
 player_letter, computer_letter = input_player_letter()
 turn = who_first()
 print(turn + '先走')
 time.sleep(1)
 game_is_playing = True
 while game_is_playing:
  if turn == 'player':
   draw_board(board)
   move = get_player_move(board)
   make_move(board, player_letter, move)
   if is_winner(board, player_letter):
    draw_board(board)
    print('恭喜！你赢了。')
    game_is_playinig = False
   else:
    if is_board_full(board):
     draw_board(board)
     print('平局！')
     break
    else:
     turn = 'computer'
  else:
   move = get_computer_move(board, computer_letter)
   make_move(board, computer_letter, move)
   if is_winner(board, computer_letter):
    draw_board(board)
    print('电脑胜利，你挂了！')
    game_is_playing = False
   else:
    if is_board_full(board):
     draw_board(board)
     print('平局!')
     break
    else:
     turn = 'player'
 if not is_again():
   break