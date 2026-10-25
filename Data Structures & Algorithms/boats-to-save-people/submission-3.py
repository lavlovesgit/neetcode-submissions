class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l=0
        c=0
        r=len(people)-1
        while(l<r):
            s=people[l]+people[r]
            if(s<=limit):
                c+=1
                l+=1
                r-=1
            else:
                if people[r]<=limit:
                    c+=1
                    r-=1
                elif people[l]<=limit:
                    c+=1
                    l+=1
        if l==r:
            return c+1
        else:
            return c


        