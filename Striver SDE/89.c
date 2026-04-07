/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include<math.h>
int* grayCode(int n, int* returnSize) {
    int total = 1<<n;  //Genearete all binary numbers 2^n if n = 3 then 000,001,010.....100
    int* arr = malloc(total*sizeof(int));
    int k = 0;
    for (int i = 0;i<total;i++){
        int gray = i^(i >> 1);  //use this formula to calculate gray code and append to the list
        arr[k++] = gray;
    }
    *returnSize = total;
    return arr;
}