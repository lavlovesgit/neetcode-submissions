from collections import deque
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
           stack=deque()
           for i in asteroids:
                while(stack and i<0 and stack[-1]>0):
                    if(stack[-1]<abs(i)):
                        stack.pop()
                    elif stack[-1] == abs(i):
                        stack.pop()
                        break
                    else:  # stack[-1] > abs(a)
                        break
                else:
                    stack.append(i)



           return list(stack)




        