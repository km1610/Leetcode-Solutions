class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for i in range(len(tokens)):
            token = tokens[i]
            if token not in {'-','+','/','*'}:
                nums.append(token)
            else:
                n1 = nums.pop()
                n2 = nums.pop()
                if token == '/':
                    if n1[0]=='-' and n2[0]=='-':
                        n3 = int(n2)//int(n1)
                    elif n1[0]=='-' or n2[0]=='-':
                        n3 = -(abs(int(n2))//abs(int(n1)))
                    else:
                        n3 = int(n2)//int(n1)
                else:
                    n3 = eval(n2+token+n1)
                nums.append(str(n3))
        return int(nums[0])
