#include<limits.h>

class Solution {
public:
    vector<int> findMissingElements(vector<int>& nums) {
        int min = nums[0];
        int max = nums[0];
        unordered_map<int,bool> mp;
        for (int num: nums){
            mp[num] = true;
            if (num < min){
                min = num;
            }
            if (num > max){
                max = num;
            }
        }
        vector<int> missing;
        for(int i = min+1;i<max;i++){
            if (!mp[i]){
                missing.push_back(i);
            }
        }
        return missing;
    }
};