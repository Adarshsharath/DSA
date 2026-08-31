class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int len = nums.size() - 1;
        
        vector<vector<int>> ans;
        for (int first = 0; first < len + 1-3; first++) {
            if (first > 0 && nums[first] == nums[first - 1]) {
                    continue;
                }
            for (int fix = first+1; fix < len + 1-2; fix++) {
                if (fix > first+1 && nums[fix] == nums[fix - 1]) {
                    continue;
                }
                int left = fix + 1;
                int right = len;
                while (left < right) {
                    long long sum = (long long)nums[first] + nums[left] + nums[right] + nums[fix];
                    if (sum == target) {
                        ans.push_back({nums[first], nums[fix], nums[left], nums[right]});
                        left++;
                        right--;
                        while (left < right && nums[left] == nums[left - 1])
                            left++;

                        while (left < right && nums[right] == nums[right + 1])
                            right--;
                    }
                    else if (sum > target) {
                        right--;
                    }
                    else if (sum < target) {
                        left++;
                    }
                }
            }
        }
        return ans;
    }
};