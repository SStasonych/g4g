class Solution {
    int maxSubarraySum(int[] arr) {
        int n = arr.length;
        int currsum = 0;
        int minsum = 0;
        int res = -100000;

        for (int i = 1; i <= n; i++) {
            currsum = currsum + arr[i-1];
            if (res < currsum - minsum) {
                res = currsum - minsum;
            }
            if (minsum > currsum) {
                minsum = currsum;
            }
            
        }
        return res;
    }
}
