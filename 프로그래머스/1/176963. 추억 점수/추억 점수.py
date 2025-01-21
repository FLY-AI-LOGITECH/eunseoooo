def solution(name, yearning, photo):
    answer = []
    result = 0
    dic = {} # 딕셔너리 형식 dic 변수 선언
    
    # name(key), yearning(values)
    for i in range(len(name)):
        dic[name[i]] = yearning[i]
        
    # photo 줄 단위로 가져오기
    for line in range(len(photo)):
        # 줄단위 요소 지정
        for num in range(len(photo[line])):
            # 요소가 dic 안에 있다면 더해서 result 값으로
            if photo[line][num] in dic.keys():
                photo_name=photo[line][num]
                result += dic[photo_name]
        # 각 열 별 result 값을 answer에 추가한다음 초기화
        answer.append(result)
        result = 0
    
    return answer