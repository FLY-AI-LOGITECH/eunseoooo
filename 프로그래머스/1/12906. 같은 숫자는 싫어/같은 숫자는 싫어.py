def solution(arr):
    answer = []
    i = 0
    while i< len(arr)-1:
        num = arr[i]
        if num == arr[1+i]:
            i+=1
            continue
        else:
            answer.append(num)
            i+=1
        
    answer.append(arr[len(arr)-1])
        
    return answer