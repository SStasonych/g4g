class SegmentTree():
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [[0, 0] for _ in range(4 * self.n)]
        if self.n > 0:
            self.build(arr, 1, 0, self.n - 1)
    
    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = [arr[start], arr[start]]
            return
        mid = (start + end) // 2
        self.build(arr, 2*node, start, mid)
        self.build(arr, 2*node + 1, mid + 1, end)
        self.tree[node][0] = self.tree[2*node][0] + self.tree[2*node + 1][0]
        self.tree[node][1] = max(self.tree[2*node][1], 
            self.tree[2*node][0] + self.tree[2*node + 1][1])
    
    def search(self, l, r):
        return self.search2(1, 0, self.n - 1, l, r)[1]
    
    def search2(self, node, start, end, l, r):
        if r < start or end < l:
            return [0, float('-inf')]
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        res1 = self.search2(2*node, start, mid, l, r)
        res2 = self.search2(2*node + 1, mid + 1, end, l, r)
        return res1[0] + res2[0], max(res1[1], res1[0] + res2[1])
    
        

class Solution:
    def maxPrefixSumQueries(self, arr, queries):
        st = SegmentTree(arr)
        res = []
        for q in queries:
            res.append(st.search(q[0], q[1]))
        return res
        