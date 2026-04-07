/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

//wrote this below function check the existence of an item in an array and return T/F
bool in(int* num,int len,int x){
    for (int i =0;i<len;i++){
        if (x==num[i]){
            return true;
        }
    }
    return false;
}

//This function calculates low and high and then iterartes from low+1 to high ==> [low+1,high) and insert missing elements to the arr
int* findMissingElements(int* nums, int numsSize, int* returnSize) {
    int low = nums[0];
    int high = nums[0];

    for(int i = 0; i < numsSize; i++){
        if (nums[i] < low) low = nums[i];
        if (nums[i] > high) high = nums[i];
    }

    int* arr = malloc((high - low - 1) * sizeof(int)); // safe
    int k = 0;

    for(int i = low + 1; i < high; i++){
        if(!in(nums, numsSize, i)){
            arr[k++] = i;
        }
    }

    *returnSize = k;
    return arr;
}