class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        
        bank_wo_security = []
        for i in bank:
            if int(i)>0:
                bank_wo_security.append(i)
        n = len(bank_wo_security)
        beams= 0
        for i in range(n-1):
            beams += bank_wo_security[i].count('1')*bank_wo_security[i+1].count('1')

        return beams
