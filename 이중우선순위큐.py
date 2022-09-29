# 이중 우선순위 큐는 다음 연산을 할 수 있는 자료구조를 말합니다.

# 명령어	수신 탑(높이)
# I 숫자	큐에 주어진 숫자를 삽입합니다.
# D 1	큐에서 최댓값을 삭제합니다.
# D -1	큐에서 최솟값을 삭제합니다.
# 이중 우선순위 큐가 할 연산 operations가 매개변수로 주어질 때, 모든 연산을 처리한 후 큐가 비어있으면 [0,0] 비어있지 않으면 [최댓값, 최솟값]을 return 하도록 solution 함수를 구현해주세요.

# 힙큐를 이용하여 이중우선순위 큐를 구현
import heapq
def solution(operations):
    answer = []
    queue = []
    for opers in operations:
        
        first = opers.strip(" ")[0]
        second = int(opers.strip(" ")[1:])
        
        print(second)
        if first == "I" :
            heapq.heappush(queue,second)
        elif first == "D":
            print("asdasd")
            if not queue:
                pass
            
            elif second == 1:
                queue.pop()
            elif second == -1:
                heapq.heappop(queue)
            print(f"queue = {queue}, second = {second}")
    if queue:
        if queue[-1] > queue[-2]:
            answer.append(queue[-1])
        else:
            answer.append(queue[-2])
        
        answer.append(queue[0])
    if not queue:
        answer = [0,0]
    return answer
