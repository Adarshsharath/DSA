void reverse(int* arr, int low, int high) {
    int end = high - 1;

    while (low < end) {
        int temp = arr[low];
        arr[low] = arr[end];
        arr[end] = temp;
        low++;
        end--;
    }
}

void rotate(int* nums, int numsSize, int k) {
    if (numsSize == 0)
        return;

    k %= numsSize;

    reverse(nums, 0, numsSize);
    reverse(nums, 0, k);
    reverse(nums, k, numsSize);
}