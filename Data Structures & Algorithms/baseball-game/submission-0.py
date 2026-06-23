from collections import deque

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=deque()
        for i in operations:
            if i in ["+","C","D"]:
                match i:
                    case "+":
                        stack.append(stack[-1]+stack[-2])
                    case "D":
                        stack.append(2*stack[-1])
                    case "C":
                        stack.pop()



            else:
                stack.append(int(i))
        return sum(stack)
        
            
            


        