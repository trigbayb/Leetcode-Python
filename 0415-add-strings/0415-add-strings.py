class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i=1
        output=""
        k=0
        while i<=max(len(num1), len(num2)):
            if i>len(num1):
                sum1=0
            else:
                sum1=int(num1[-i])
            if i>len(num2):
                sum2=0
            else:
                sum2=int(num2[-i])
            output+=str((sum1+sum2+k) % 10)
            k=(sum1+sum2+k)//10
            i+=1
        if k>0:
            output+=str(k)
        return output[::-1]
            

        