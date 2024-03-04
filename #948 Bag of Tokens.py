def face_up(token,power):
    power-=token
    return power

def face_down(token,power):
    power+=token
    return power

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        curr_score = 0
        tokens.sort()

        if len(tokens)==0:
            return 0
        # if tokens[0]<power:
        #     return 0
        
        n = len(tokens)

        l,r = 0,n-1

        while l<=r:
            if power>=tokens[l]:
                power = face_up(tokens[l],power)
                curr_score+=1
                # print("{}\t{}\t{}".format(tokens[l],power,curr_score))
                l+=1
            elif curr_score>=1:
                power = face_down(tokens[r],power)
                curr_score-=1
                # print("{}\t{}\t{}".format(tokens[r],power,curr_score))
                r-=1
            else:
                break            

            score = max(curr_score,score)
        return score
