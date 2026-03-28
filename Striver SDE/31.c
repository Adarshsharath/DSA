void nextPermutation(int* nums, int numsSize) {
    int pivot = -1;

    // Step 1: find pivot
    for (int i = 0; i < numsSize - 1; i++) {
        if (nums[i] < nums[i + 1]) {
            pivot = i;
        }
    }

    // Step 2: if no pivot → reverse whole array
    if (pivot == -1) {
        for (int i = 0, j = numsSize - 1; i < j; i++, j--) {
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
        }
        return;
    }

    // Step 3: find next greater element (from right)
    int newPivot = 0;
    for (int i = numsSize - 1; i > pivot; i--) {
        if (nums[i] > nums[pivot]) {
            newPivot = i;
            break;
        }
    }

    // Step 4: swap
    int temp = nums[newPivot];
    nums[newPivot] = nums[pivot];
    nums[pivot] = temp;

    // Step 5: reverse suffix
    for (int i = pivot + 1, j = numsSize - 1; i < j; i++, j--) {
        temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}