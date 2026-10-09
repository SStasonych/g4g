class Solution {
    public void rotateMatrix(int[][] mat) {
        int n = mat.length;
        rotateDiagonal(mat, n);
        rotateHorizontal(mat, n);
    }
    
    void rotateDiagonal(int[][] m, int n) {
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                int tmp = m[i][j];
                m[i][j] = m[j][i];
                m[j][i] = tmp;
            }    
        }
    }
    
    void rotateHorizontal(int[][] m, int n) {
        for (int i = 0; i < n/2; i++) {
            for (int j = 0; j < n; j++) {
                int tmp = m[i][j];
                m[i][j] = m[n - 1 - i][j];
                m[n - 1 - i][j] = tmp;
            }    
        }
    }
    
    
}