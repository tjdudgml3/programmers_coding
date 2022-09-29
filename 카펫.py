#Leo는 집으로 돌아와서 아까 본 카펫의 노란색과 갈색으로 색칠된 격자의 개수는 기억했지만, 전체 카펫의 크기는 기억하지 못했습니다.

#Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.

# 노란색과 갈색의 수적 관계를 이용하여 함수를 작성했음

def solution(brown, yellow):
    answer = []
    division = []
    for i in range(yellow):
        if yellow%(i+1) == 0:
            temp = [i+1,yellow/(i+1)]
            division.append(temp)
    for a in division:
        if a[0]*2 + a[1]*2 + 4 == brown:
            answer = [a[0]+2,a[1]+2]
            
    return answer
