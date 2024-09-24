import math

# Hàm kiểm tra xem trò chơi đã kết thúc chưa (ai thắng, hòa, hay tiếp tục)
def check_winner(board):
    # Các dòng, cột và đường chéo
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]
    
    # Kiểm tra xem X hoặc O thắng
    for line in win_conditions:
        if line == ['X', 'X', 'X']:
            return 'X'
        if line == ['O', 'O', 'O']:
            return 'O'
    
    # Kiểm tra xem hòa chưa
    if all(cell != '' for row in board for cell in row):
        return 'Tie'
    
    # Nếu không, trò chơi tiếp tục
    return None

# Hàm đánh giá giá trị nút
def eval_board(board):
    winner = check_winner(board)
    if winner == 'X':
        return 1  # X thắng
    elif winner == 'O':
        return -1  # O thắng
    else:
        return 0  # Hòa hoặc chưa kết thúc

# Hàm thuật toán MaxVal
def MaxVal(board, alpha, beta):
    if check_winner(board) is not None:
        return eval_board(board)
    
    max_val = -math.inf
    for i in range(3):
        for j in range(3):
            if board[i][j] == '':
                board[i][j] = 'X'  # Trắng (X) đi
                max_val = max(max_val, MinVal(board, alpha, beta))
                board[i][j] = ''  # Hoàn tác nước đi
                alpha = max(alpha, max_val)
                if alpha >= beta:
                    return max_val
    return max_val

# Hàm thuật toán MinVal
def MinVal(board, alpha, beta):
    if check_winner(board) is not None:
        return eval_board(board)
    
    min_val = math.inf
    for i in range(3):
        for j in range(3):
            if board[i][j] == '':
                board[i][j] = 'O'  # Đen (O) đi
                min_val = min(min_val, MaxVal(board, alpha, beta))
                board[i][j] = ''  # Hoàn tác nước đi
                beta = min(beta, min_val)
                if alpha >= beta:
                    return min_val
    return min_val

# Thuật toán Alpha-beta tìm nước đi tốt nhất cho X
def Alpha_beta(board):
    best_move = None
    alpha = -math.inf
    beta = math.inf
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == '':
                board[i][j] = 'X'  # Trắng (X) đi
                move_val = MinVal(board, alpha, beta)
                board[i][j] = ''  # Hoàn tác nước đi
                
                if move_val > alpha:
                    alpha = move_val
                    best_move = (i, j)
    
    return best_move

# Hàm in bàn cờ
def print_board(board):
    for row in board:
        print(row)

# Bắt đầu trò chơi
def play_game():
    board = [['', '', ''], ['', '', ''], ['', '', '']]  # Bàn cờ rỗng
    current_player = 'X'  # X đi trước
    
    while True:
        print_board(board)
        winner = check_winner(board)
        if winner:
            if winner == 'Tie':
                print("Hòa!")
            else:
                print(f"Người chơi {winner} thắng!")
            break
        
        if current_player == 'X':
            print("Lượt của X (người chơi)")
            move = Alpha_beta(board)
            if move:
                board[move[0]][move[1]] = 'X'
                current_player = 'O'
        else:
            print("Lượt của O (máy)")
            i, j = map(int, input("Nhập vị trí nước đi O (i j): ").split())
            if board[i][j] == '':
                board[i][j] = 'O'
                current_player = 'X'

if __name__ == "__main__":
    play_game()
