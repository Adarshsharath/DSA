#include <stdlib.h>

int fun(int idx, int* nums, int n, int target, int* dp) {

    if (idx == n - 1) {
        return 0;
    }

    if (dp[idx] != -2) {
        return dp[idx];
    }

    int ans = -1;

    for (int j = idx + 1; j < n; j++) {

        int diff = nums[j] - nums[idx];

        if (-target <= diff && diff <= target) {

            int result = fun(j, nums, n, target, dp);

            if (result != -1) {
                int value = 1 + result;

                if (value > ans) {
                    ans = value;
                }
            }
        }
    }

    dp[idx] = ans;

    return ans;
}

int maximumJumps(int* nums, int numsSize, int target) {

    int* dp = (int*)malloc(numsSize * sizeof(int));

    for (int i = 0; i < numsSize; i++) {
        dp[i] = -2;
    }

    int answer = fun(0, nums, numsSize, target, dp);

    free(dp);

    return answer;
}