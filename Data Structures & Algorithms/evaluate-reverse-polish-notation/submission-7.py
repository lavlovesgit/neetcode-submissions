
from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack=deque()
        for i in tokens:
            
        
            if i in ["+","-","*","/"]:
                match i:
                    case "+":
                        stack.append(stack.pop()+stack.pop())
                    case "-":
                        x=stack[-2]-stack[-1]
                        stack.pop()
                        stack.pop()
                        stack.append(x)
                    case "*":
                        stack.append(stack.pop()*stack.pop())
                    case "/":
                        x=int(stack[-2]/stack[-1])
                        stack.pop()
                        stack.pop()
                        stack.append(x)

            else:
                stack.append(int(i))
            for j in stack:
                  print (j)
            print("*")
            
        
        return stack.pop()
         

        
            
            


        