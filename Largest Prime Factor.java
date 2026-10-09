class Solution {

    static int largestPrimeFactor(int n) {
        int max = 2;
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) max = i;
            while (n % i == 0) {
                n = n/i;
            }
        }
        return Math.max(max, n);
    }
}