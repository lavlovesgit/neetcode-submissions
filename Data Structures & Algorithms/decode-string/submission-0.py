from collections import deque
class Solution:
    def decodeString(self, s: str) -> str:
        count=deque()
        string=deque()
        res=""
        k=0

        for i in s:
            if i.isdigit():
                k=10*k+int(i)
            elif i=='[':
                count.append(k)
                string.append('[')
                k=0
            elif i.isalpha():
                string.append(i)
            elif i==']':
                temp=""
                while(string[-1]!='['):
                    temp=string.pop()+temp
                if(string[-1]=='['):
                    string.pop()
                    mul=count.pop()
                    string.append(mul*temp)
        return ''.join(string)



                


        