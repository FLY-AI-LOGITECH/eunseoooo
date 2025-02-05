def solution(array, commands):
    answer = [] # 최종 출력 list
    list_new = [] # 2차원 배열 정렬해서 넣을 list
    
    for i in range(len(commands)):
        start = commands[i][0] - 1
        end = commands[i][1] - 1
        point = commands[i][2] - 1
        
        list_new.append(array[start:end + 1]) # 각 배열에서 해당 범위만 받아오기
        list_new[i].sort() # 정렬하기
        
        answer.append(list_new[i][point]) # k번째 수 가져와서 최종 배열에 넣기
        
    return answer