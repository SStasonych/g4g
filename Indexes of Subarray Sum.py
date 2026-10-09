class Solution:
    def subarraySum(self, arr, target):
        n = len(arr)
        start = 0
        end = 0
        sum1 = arr[0]
        
        while end < n:
            if sum1 < target: 
                end +=1
                if end == n: return [-1]
                sum1 += arr[end]
            if sum1 > target:
                sum1 -= arr[start]
                start +=1
            if sum1 == target: return [start+1, end+1]
            
        return [-1]
            
        