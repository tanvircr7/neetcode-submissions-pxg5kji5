class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        l,r=0,len(people)-1
        ans = 0
        while l<r:
            if people[l]+people[r] <= limit:
                ans += 1
                l+=1
                r-=1
            else:
                ans += 1
                r-=1
                # maybe we could shove people[l] weight to some other boat
                # but there is no way we can shove people[r]
        
        if l==r:
            ans += 1
            # only possible for the last man standing who has no pair
        
        return ans