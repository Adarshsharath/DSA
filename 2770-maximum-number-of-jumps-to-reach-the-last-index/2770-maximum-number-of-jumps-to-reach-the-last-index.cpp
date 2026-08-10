class Solution {
public:

    int maximumJumps(vector<int>& nums, int target) {

        int n = nums.size();

        vector<int> dp(n, -2);

        function<int(int)> fun = [&](int idx) {

            if (idx == n - 1) {
                return 0;
            }

            // Already calculated
            if (dp[idx] != -2) {
                return dp[idx];
            }

            int ans = -1;

            for (int j = idx + 1; j < n; j++) {

                int diff = nums[j] - nums[idx];

                if (-target <= diff && diff <= target) {

                    int result = fun(j);

                    if (result != -1) {
                        ans = max(ans, 1 + result);
                    }
                }
            }

            dp[idx] = ans;
            return ans;
        };

        return fun(0);
    }
};