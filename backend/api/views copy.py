from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
import json
import copy

@csrf_exempt
def index(request):
    
    return HttpResponse('<h1>hello</h1>')

# # Hàm để tính giá trị f(u) cho các đỉnh kết thúc
# def f(u):
#     return u

# # Hàm MaxVal xác định giá trị cho các đỉnh Trắng
# def MaxVal(u, tree):
#     if len(tree[u]) == 0:
#         return f(u)
#     else:
#         # Trả về giá trị lớn nhất từ các đỉnh con của u
#         return max(MinVal(v, tree) for v in tree[u])

# # Hàm MinVal xác định giá trị cho các đỉnh Đen
# def MinVal(u, tree):
#     if len(tree[u]) == 0:
#         return f(u)
#     else:
#         # Trả về giá trị nhỏ nhất từ các đỉnh con của u
#         return min(MaxVal(v, tree) for v in tree[u])

# tree = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F', 'G'],
#     'D': [],  # Đỉnh kết thúc
#     'E': [],  # Đỉnh kết thúc
#     'F': [],  # Đỉnh kết thúc
#     'G': []   # Đỉnh kết thúc
# }


# Giá trị Minimax bắt đầu từ đỉnh A (gốc của cây)
# result = MaxVal('A', tree)
# print("Giá trị Minimax:", result)

emptyArray = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]



#   ["x", "", ""],
#   ["x", "", ""],
#   ["", "o", "o"]

empty = ''
x = 'x'
o = 'o'

def printArray(array):
    for row in array:
        print(row)

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
    if data[row][col] == o or  row >= len(data) - 1 or data[row + 1][col] != empty:
        return None
    if data[row + 1][col] == empty:
        data[row + 1][col] = data[row][col]
        data[row][col] = empty
    return data

def top(data, row, col):
    if row <= 0 or data[row - 1][col] != empty:
        return None
    if data[row - 1][col] == empty:
        data[row - 1][col] = data[row][col]
        data[row][col] = empty
    return data

def caseOfPoint(u, row, col):
    arr = []
    u_copy = copy.deepcopy(u)
    tempArray = right(u_copy, row, col)
    if tempArray != None:
        arr.append(tempArray)
    u_copy = copy.deepcopy(u)
    tempArray = left(u_copy, row, col)
    if tempArray != None:
        arr.append(tempArray)
    u_copy = copy.deepcopy(u)
    tempArray = bottom(u_copy, row, col)
    if tempArray != None:
        arr.append(tempArray)
    u_copy = copy.deepcopy(u)
    tempArray = top(u_copy, row, col)
    if tempArray != None:
        arr.append(tempArray)
    return arr

def all_case_of_type(u, type):
    len_u = range(len(u))
    all_case = []
    for row in len_u:
        for col in len_u:
            if u[row][col] == type:
                all_case += caseOfPoint(u, row, col)
    return all_case

def max_val(u, key):
    # print("of: x", key)
    # printArray(all_case_of_type(u, key))
    # print("===================")
    # print()
    # print()
    if not is_have_key(u, key):
        return 1
    else:
        return max(min_val(v, o if key == x else x) for v in all_case_of_type(u, key))


def min_val(u, key):   
    # print("of: o", key)
    # printArray(all_case_of_type(u, key))
    # print("===================")
    # print()
    # print()
    # if u == emptyArray:
    #     return u
    if not is_have_key(u, key):
        return -1
    else:
        return min(max_val(v,  o if key == x else x) for v in all_case_of_type(u, o))
       
def is_have_key(u, key):
    range_u = range(len(u))
    for row in range_u:
        for col in range_u:
            if u[row][col] == key:
                return True
    return False
 
def minimax(u, v):
    val = float('-inf')
    for w in children_of(u):
        min_val_w = min_val(w)
        if val <= min_val_w:
            val = min_val_w
            v = w
    return val, v

def front_of(u, row, col):
    sum = 0
    key = u[row][col]
    if key == x:
        count = 0
        for i in range(row+1, len(u)):
            if u[i][col] != key and u[i][col] != empty:
                if count == 0:
                    sum -= 40
                else:
                    sum -= 30
            count +=1
    elif key == o:
        count = 0
        for i in range(col -1, -1, -1):
            if u[row][i] != key and u[row][i] != empty:
                if count == 0:
                    sum += 40
                else:
                    sum += 30
            count +=1
    return sum

# tính tổng vị trí, tính chặn trực tiếp, chặn gián tiếp
def count_state(u):
    sum = 0
    range_u = range(len(u))
    for row in range_u:
        for col in range_u:
            value_point = u[row][col]
            if value_point != empty:
                if value_point == x:
                    sum += x_state[row][col]
                else:
                    sum += o_state[row][col]
                sum += front_of(u, row, col)
            
    return sum
    
# không còn ô trống hoặc có người thắng thì đó là nút lá
# cụ thể là chỉ có lại 1 loại quân trên bàn cờ
def isWin(u):
    have_x = False
    have_o = False
    for row in u:
        for col in row:
            if col == x:
                have_x = True
            if col == o:
                have_o = True
    if not have_x or not have_o:
        return True
    else:
        return False
# chat chat


# Hàm MaxVal
def MaxVal(u, alpha, beta):
    # Kiểm tra nếu u là lá hoặc là đỉnh kết thúc
    if isWin(u):
        return count_state(u)

    # Lặp qua các đỉnh con của u
    children_u = all_case_of_type(u, x) + all_case_of_type(u, o)
    for v in children_u:
        alpha = max(alpha, MinVal(v, alpha, beta))
        # Cắt bỏ các cây con từ các đỉnh còn lại
        if alpha >= beta:
            break
    return alpha

# Hàm MinVal
def MinVal(u, alpha, beta):
    # Kiểm tra nếu u là lá hoặc là đỉnh kết thúc
    if isWin(u):
        return count_state(u)

    # Lặp qua các đỉnh con của u
    children_u = all_case_of_type(u, x) + all_case_of_type(u, o)
    for v in children_u:
        beta = min(beta, MaxVal(v, alpha, beta))
        # Cắt bỏ các cây con từ các đỉnh còn lại
        if alpha >= beta:
            break
    return beta

# Thuật toán Alpha-beta để tìm nước đi cho Trắng
def Alpha_beta(u):
    alpha = float('-inf')
    beta = float('inf')
    best_move = None

    children_u = all_case_of_type(u, x) + all_case_of_type(u, o)
    for w in children_u:
        value = MinVal(w, alpha, beta)
        if alpha <= value:
            alpha = value
            best_move = w

    return best_move


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
temp = [
    ["x", "", ""],
    ["", "", ""],
    ["x", "o", "o"]
]
temp2 = [
    ["", "x", ""],
    ["", "o", ""],
    ["x", "", "o"]
]
temp3 = [
    ["", "", ""],
    ["", "", ""],
    ["x", "o", ""]
]


# @csrf_exempt
def send():
    
    # data = json.loads(request.body)["array"]
    
    # result = caseOfPoint(data, 1, 0)
    # result = max_val(data, x)
    # result = count_state(temp)
    # result = front_of(temp2, 0, 1)
    result = Alpha_beta(temp)
    # result = isWin(temp3)


    print(result)
    
    # for row in range(len(data)):
    #     for col in range(len(data)):
    #         result = findNear(data, row, col)
    #         break
    #     break
    # for i in result:
    #     printArray(i)
    #     print("===================")

    # return JsonResponse({"data": data})

send()