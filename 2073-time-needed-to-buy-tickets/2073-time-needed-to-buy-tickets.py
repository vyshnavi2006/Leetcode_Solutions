class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        q = deque()
        for i in range(len(tickets)):
            q.append(i)
        sec = 0
        while tickets[k] > 0:
            x = q.popleft()
            tickets[x]-=1
            sec+=1
            if tickets[x]>0:
                q.append(x)
        return sec
        


                



        