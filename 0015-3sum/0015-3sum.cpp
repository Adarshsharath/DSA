class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int len = nums.size()-1;
        int sum = 1;
        vector<vector<int>> ans;
        for(int fix =0;fix<len+1;fix++){
            if (fix > 0 && nums[fix] == nums[fix - 1]){
                continue;
            }
            int left = fix+1;
            int right = len;
            while(left<right){
                sum = nums[left]+nums[right]+nums[fix];
                if (sum == 0){
                    ans.push_back({nums[fix],nums[left],nums[right]});
                    left++;
                    right--;
                    while (left < right &&
                           nums[left] == nums[left - 1])
                        left++;

                    while (left < right &&
                           nums[right] == nums[right + 1])
                        right--;
                }
                if (sum > 0){
                    right--;
                }
                if (sum < 0){
                    left++;
                }
            }
        }        
        return ans;
    }
};