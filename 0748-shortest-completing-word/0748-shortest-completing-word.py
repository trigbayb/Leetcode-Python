class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        count=10001
        for i in words:
            flag=True
            k=i
            for j in licensePlate:
                print(i, j, j.isnumeric() or j==" ", k)
                if j.lower() in k:
                    k=k.replace(j.lower(), "", 1)
                    print(k)
                elif j.isnumeric() or j==" ":
                    continue
                else:
                    flag=False
                    break
            if flag==True and len(i)<count:
                count=len(i)
                output=i
        return output
            
