#문제 설명
# 네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미합니다. 예를 들어, 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어있고, 컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때 컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 정보를 교환할 수 있습니다. 따라서 컴퓨터 A, B, C는 모두 같은 네트워크 상에 있다고 할 수 있습니다.

# 컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 네트워크의 개수를 return 하도록 solution 함수를 작성하시오.
#dfs를 이용하여 네트워크의 수를 리턴함. 
def solution(n, computers):
    answer = 0
    cnt = 0
    num = 1
    def dfs(idx: int, computers: list,num):
        #print(f"{num}번째 dfs idx ={idx}, list = {computers}")
        num += 1
        if computers[idx][idx] == 0:
            return
        else:
            computers[idx][idx] = 0
            for i in range(len(computers[idx])):
                if computers[idx][i] == 1:
                    dfs(i,computers,num)
        
    for i in range(len(computers)):
        if computers[i][i] == 1:
            dfs(i,computers,num)
            #print(computers)
            cnt += 1
    return cnt
