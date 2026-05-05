class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        work = [-cnt[1] for cnt in count.items()]

        q = deque()
        heapq.heapify(work)
        time = 0

        while work or q:
            time += 1

            if work:
                load = heapq.heappop(work)
                load += 1
                if load < 0:
                    q.append([load, time+n])
            else:
                time = q[0][1]
            
            while q and q[0][1]==time:
                heapq.heappush(work, q.popleft()[0])

        return time