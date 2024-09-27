from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import copy
import json

empty = ''
x = 'x'
o = 'o'

# Các trạng thái điểm của X và O
x_state = [
    [-10, -25, -40],
    [-5, -20, -35],
    [0, -15, -30]
]
o_state = [
    [30, 35, 40],
    [15, 20, 25],
    [0, 5, 10]
]

# Giới hạn độ sâu đệ quy
MAX_DEPTH = 10

# Kiểm tra nếu không còn quân cờ đối phương
def isWin(u):
    have_x = False
    have_o = False
    for row in u:
        for col in row:
            if col == x:
                have_x = True
            if col == o:
                have_o = True
    return not have_x or not have_o


def printArray(array):
    for row in array:
        print(row)
def printArray2(array):
    for row in array:
        for col in row:
            print(col)
    print('========================')
    print()
    
# Tính tổng điểm của trạng thái bàn cờ
def count_state(u):
    sum = 0
    # print("count state of: ")
    # printArray(u)
    # print("================================")
    for row in range(len(u)):
        for col in range(len(u)):
            value_point = u[row][col]
            if value_point != empty:
                if value_point == x:
                    sum += x_state[row][col]
                else:
                    sum += o_state[row][col]
    return sum

def right(data, row, col):
    if col >= len(data) - 1:
        if data[row][col] == x:
            data[row][col] = empty
            return data  
        else:
            return None
    if data[row][col + 1] != empty:
        return None
    if data[row][col + 1] == empty:
        data[row][col + 1] = data[row][col]
        data[row][col] = empty
        return data

def left(data, row, col):
    if data[row][col] == x or col <= 0 or data[row][col - 1] != empty:
        return None
    if data[row][col - 1] == empty:
        data[row][col - 1] = data[row][col]
        data[row][col] = empty
    return data

def bottom(data, row, col):
    if  data[row][col] == o or row >= len(data) - 1 or data[row + 1][col] != empty:
        return None
    if data[row + 1][col] == empty:
        data[row + 1][col] = data[row][col]
        data[row][col] = empty
    return data

def top(data, row, col):
    if row == 0 and data[row][col] == o:
        data[row][col] = empty
    elif row <= 0 or data[row - 1][col] != empty:
        return None
    elif data[row - 1][col] == empty:
        data[row - 1][col] = data[row][col]
        data[row][col] = empty
    return data


# Tìm tất cả các trạng thái con
def caseOfPoint(u, row, col):
    arr = []
    u_copy = copy.deepcopy(u)
    tempArray = right(u_copy, row, col)
    if tempArray is not None:
        arr.append(tempArray)
    u_copy = copy.deepcopy(u)
    tempArray = left(u_copy, row, col)
    if tempArray is not None:
        arr.append(tempArray)
    u_copy = copy.deepcopy(u)
    tempArray = bottom(u_copy, row, col)
    if tempArray is not None:
        arr.append(tempArray)
    u_copy = copy.deepcopy(u)
    tempArray = top(u_copy, row, col)
    if tempArray is not None:
        arr.append(tempArray)
    return arr

def all_case_of_type(u, key):
    len_u = range(len(u))
    all_case = []
    for row in len_u:
        for col in len_u:
            if u[row][col] == key:
                all_case += caseOfPoint(u, row, col)
    return all_case

# Alpha-beta pruning implementation with depth limit
count = 0
def MaxVal(u, alpha, beta, depth):
    if isWin(u) or depth == 0:
        if isWin(u):
            print("winx: ", u, count_state(u))
            print("========================")
        return count_state(u)
    for v in all_case_of_type(u, x):
        alpha = max(alpha, MinVal(v, alpha, beta, depth - 1))
        if alpha >= beta:
            break
    return alpha

def MinVal(u, alpha, beta, depth):
    
    if isWin(u) or depth == 0:
        if isWin(u):
            print("wino: ", u, count_state(u))
            print("========================")
        return count_state(u)
    
    for v in all_case_of_type(u, o):
        beta = min(beta, MaxVal(v, alpha, beta, depth - 1))
        if alpha >= beta:
            break
    return beta

def Alpha_beta(u):
    alpha = float('-inf')
    beta = float('inf')
    best_move = None
    # best_move = []
    
    # print("u: ", u)
    # print('all case:')
    # printArray2(all_case_of_type(u, o))
    # print('-========================================')
    
    for w in all_case_of_type(u, o):
        value = MinVal(w, alpha, beta, MAX_DEPTH)
        if alpha <= value:
            alpha = value
            best_move = w
            # best_move.append(w)

    
    return best_move

# View xử lý request và trả về kết quả
@csrf_exempt
def index(request):
    if request.method == 'POST':
        data = json.loads(request.body).get("value", [])
        
        if not data:
            return JsonResponse({"error": "Invalid data"}, status=400)
        print(data)

        result = Alpha_beta(data)
        # result = all_case_of_type(data, o)

        print("result: ")
        printArray(result)
        return JsonResponse({"best_move": result})
    
    return JsonResponse({"message": "Send a POST request with the game board data."})


# làm thêm cái mà nếu đi ra ngoài được cao điểm hơn là ok he