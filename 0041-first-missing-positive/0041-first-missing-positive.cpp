class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        map<int, bool> mp;

        for (int num : nums) {
            if (num > 0)
                mp[num] = true;
        }

        int prev = 0;

        for (auto p : mp) {
            if (p.first != prev + 1) {
                return prev + 1;
            }
            prev = p.first;
        }

        return prev + 1;
    }
};