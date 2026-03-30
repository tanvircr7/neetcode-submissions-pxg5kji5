class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxhp = [-cnt for cnt in count.values()]
        heapq.heapify(maxhp)

        time = 0
        q = deque()
        while maxhp or q:
            time += 1

            if maxhp:
                cnt = 1 + heapq.heappop(maxhp)

                if cnt < 0:
                    q.append([cnt, time+n])
            
            else:
                time = q[0][1]

            if q and q[0][1]==time:
                heapq.heappush(maxhp, q.popleft()[0])

        return time 

