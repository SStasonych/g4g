class Solution {
    public int nthRoot(int n, int m) {
        if (m == 0) return 0;
        if (m == 1) return 1;
        if (n == 1) return m;

        return getRoot(n, m, 1, (int) Math.floor(Math.sqrt(m)));
    }
    
    int getRoot(int n, int m, int start, int end) {
        int mid = (start + end)/2;
        int v = pow(mid, n, m);
        if (v == m) {
            return mid;
        } else if (start >= end) {
            return -1;
        }
        if (v > m) {
            return getRoot(n,m,start, mid - 1);
        } else {
            return getRoot(n,m,mid + 1, end);
        }   
    }
    
    int pow(int a, int n, int m) {
        int res = 1;
        for (int i = 0; i < n; i++){
           res *= a; 
           if (res > m) return res;
        }
        return res;
    }
}