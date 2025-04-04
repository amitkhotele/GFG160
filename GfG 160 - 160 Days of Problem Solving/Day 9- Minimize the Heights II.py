class Solution:
    def getMinDiff(self, arr,k):
        n= len(arr)
        if n== 1:
            return 0
        arr.sort()
        
        ans= arr[-1] - arr[0]
        
        for i in range(n-1):
            high= max(arr[i]+k, arr[-1]-k)
            low= min(arr[0]+k, arr[i+1]-k)
            if low<0:
                continue
            
            ans= min(ans, high-low)
            
        return ans
