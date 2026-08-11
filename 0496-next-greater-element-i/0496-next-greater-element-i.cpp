class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        vector<int> ans;

        for (int num1 : nums1) {
            bool great = false;

            for (int i = 0; i < nums2.size(); i++) {

                if (nums2[i] == num1) {

                    for (int j = i + 1; j < nums2.size(); j++) {

                        if (nums2[j] > num1) {
                            ans.push_back(nums2[j]);
                            great = true;
                            break;
                        }
                    }

                    break;
                }
            }

            if (!great) {
                ans.push_back(-1);
            }
        }

        return ans;
    }
};