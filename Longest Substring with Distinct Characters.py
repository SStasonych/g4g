class Solution:
   def longestUniqueSubstr(self, s):
           n = len(s)
           start, end = 0, 0
           res = 1
           voc = {}
           voc[s[0]] = True

           while end < n - 1:
               end +=1

               if s[end] in voc and voc[s[end]]:
                   while s[start] != s[end]:
                        voc[s[start]] = False
                        start +=1
                   voc[s[start]] = False
                   start +=1
                
               voc[s[end]] = True


               if res < end - start + 1:
                   res = end - start + 1

           return res
            
            

            
        