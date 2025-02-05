import math

def solution(sizes):
    min_hw = 0 # hw 통틀어 가장 큰 값이 나온 명함을 제외한 가장 작은 값
    max_hw = 0 # hw 통틀어 가장 큰값
    w = []
    h = []
    min_list = [] # 명함 당 작은 면의 값 list
    
    for i in range(len(sizes)): # 가로들을 w, 세로들을 h 로 리스트에 넣기
        w.append(sizes[i][0])
        h.append(sizes[i][1])
        
    # 큰 값 고르기
    max_w = max(w) 
    max_h = max(h)
    
    # hw 통틀어 가장 큰 값
    max_hw = max_w if max_w >= max_h else max_h
    
    # 가로 세로 비교해서 작은 값 리스트에 넣기
    for i in range(len(sizes)):
        if h[i] <= w[i]:
            min_list.append(h[i])
        else:
            min_list.append(w[i])
        
    max_hw = max_w if max_w >= max_h else max_h
    min_hw = max(min_list)
        
    return max_hw*min_hw