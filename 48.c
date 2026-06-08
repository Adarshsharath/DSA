void rotate(int** matrix, int matrixSize, int* matrixColSize) {

    // Step 1: Transpose
    for(int i = 0; i < matrixSize; i++) {
        for(int j = i + 1; j < matrixSize; j++) {

            int temp = matrix[i][j];
            matrix[i][j] = matrix[j][i];
            matrix[j][i] = temp;
        }
    }

    // Step 2: Reverse each row
    for(int i = 0; i < matrixSize; i++) {

        int left = 0;
        int right = matrixSize - 1;

        while(left < right) {

            int temp = matrix[i][left];
            matrix[i][left] = matrix[i][right];
            matrix[i][right] = temp;

            left++;
            right--;
        }
    }
}


//Method 2 using temp matrix
void rotate(int** matrix, int matrixSize, int* matrixColSize) {

    int n = matrixSize;

    // temporary matrix
    int temp[n][n];

    // place elements in rotated position
    for(int i = 0; i < n; i++) {

        for(int j = 0; j < n; j++) {

            int k = n - 1 - i;

            temp[j][k] = matrix[i][j];
        }
    }

    // copy back to original matrix
    for(int i = 0; i < n; i++) {

        for(int j = 0; j < n; j++) {

            matrix[i][j] = temp[i][j];
        }
    }
}