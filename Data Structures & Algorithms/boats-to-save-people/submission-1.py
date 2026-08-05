class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i=0
        j=len(people)-1
        c=0
        while(i<j):
            s=people[i]+people[j]
            if(s<=limit):
                c+=1
                i+=1
                j-=1
            if(s>limit):
                if(people[j]<=limit):
                    c+=1
                j-=1
        if i == j:
           c += 1
        return c


        