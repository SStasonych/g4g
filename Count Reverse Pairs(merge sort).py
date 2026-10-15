class Solution:
    def countRevPairs(self, arr):
        def merge(arr, start, end):
            if start == end:
                return 0
            mid = (start + end) // 2
            count1 = merge(arr, start, mid)
            count2 = merge(arr, mid +1, end)
            i = start
            j = mid + 1
            count = 0
            countj = 0
            
            while i <= mid and j <= end:
                if arr[i] > 2*arr[j]:
                    i += 1
                    countj += 1
                else:
                    j += 1
                    count += countj
                    
            if  j <= end:
                count += countj*(end + 1 -j)
            
            
            temp = []
            i = start
            j = mid + 1
            while i <= mid and j <= end:
                if arr[i] > arr[j]:
                    temp.append(arr[i])
                    i += 1
                else:
                    temp.append(arr[j])
                    j += 1
                    
            while i <= mid:
                temp.append(arr[i])
                i += 1
                
            while j <= end:
                temp.append(arr[j])
                j += 1
                
            for k in range(len(temp)):
                arr[start + k] = temp[k]
    
            
            return count1 + count2 + count
    
        return merge(arr, 0, len(arr) - 1)