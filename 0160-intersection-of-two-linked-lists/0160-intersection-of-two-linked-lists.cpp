/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode* curA = headA;
        ListNode* curB = headB;

        while (curA!= NULL){
            curB = headB;
            while(curB!=NULL){
                if (curA == curB){
                    return curA;
                }
                curB = curB->next;
            }
            curA= curA->next;
        }
        return NULL;
    }
};