def solution(tickets):
    answer = []
    tickets.sort()
    stack = []
    lenth = len(tickets)
    #print(tickets)
    def dfs(city,tickets,cnt,stack,lenth,answer):
        stack.append(city)
        #print(stack)
        if len(stack) - 1 == lenth:
            if not answer: 
                for a in stack:
                    answer.append(a)
            
            return
        else:
            
            for i in range(len(tickets)):
                if tickets[i][0] == city:
                    temp = tickets[:i]+tickets[i+1:]
                    dfs(tickets[i][1],temp,cnt+1,stack,lenth,answer)
                    stack.pop()
            return
    for i in range(len(tickets)):
        while(stack):
            stack.pop()
        
        cur_city = tickets[i][0]
        next_city = tickets[i][1]
        if cur_city == "ICN":
            stack.append(cur_city)
        #print(f"tickets = {tickets} stack = {stack} cur _city = {cur_city}")
            temp = tickets[:i]+tickets[i+1:]
        
            dfs( next_city,temp,0,stack,lenth,answer)
            stack.pop()
            del temp
    return answer
