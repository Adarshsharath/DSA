class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {

        sort(nums.begin(), nums.end());

        int len = nums.size() - 1;
        int closest = nums[0] + nums[1] + nums[2];

        for (int fix = 0; fix < len + 1; fix++) {

            if (fix > 0 && nums[fix] == nums[fix - 1]) {
                continue;
            }

            int left = fix + 1;
            int right = len;

            while (left < right) {

                int sum = nums[left] + nums[right] + nums[fix];

                if (abs(sum - target) < abs(closest - target)) {
                    closest = sum;
                }

                if (sum > target) {
                    right--;
                }

                if (sum < target) {
                    left++;
                }

                if (sum == target) {
                    return sum;
                }
            }
        }

        return closest;
    }
};