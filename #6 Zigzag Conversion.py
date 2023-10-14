class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        string = ['']*(numRows)

        count = 0
        index = 0
        while count!=len(s):
            if index==0:
                while index<numRows and count!=len(s):
                    string[index]+=s[count]
                    count+=1
                    index+=1
            elif index==numRows:
                index-=2
                while index>0 and count!=len(s):
                    string[index]+=s[count]
                    count+=1
                    index-=1
        
        return ''.join(string)
        
