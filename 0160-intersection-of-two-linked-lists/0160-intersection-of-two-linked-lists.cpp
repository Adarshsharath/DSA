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
        // ListNode* curA = headA;
        // ListNode* curB = headB;

        // while (curA!= NULL){
        //     curB = headB;
        //     while(curB!=NULL){
        //         if (curA == curB){
        //             return curA;
        //         }
        //         curB = curB->next;
        //     }
        //     curA= curA->next;
        // }
        // return NULL;
        ListNode* curA = headA;
        ListNode* curB = headB;
        int lenA = 0;
        int lenB = 0;
        while(curA!=NULL){
            lenA++;
            curA=curA->next;
        }
        while(curB!=NULL){
            lenB++;
            curB=curB->next;
        }
        int sm = 0;
        curA = headA;
        curB = headB;

        if (lenA > lenB){
            sm = lenA - lenB;
            while(sm){
                if (curA!=NULL){
                    curA = curA->next;
                }
                sm--;
            }
            while(curA!=NULL){
                
                if(curA==curB){
                    return curA;
                }
                curA= curA->next;
                curB= curB->next;
            }
        }
        else{
            sm = lenB - lenA;
            while(sm){
                if (curB!=NULL){
                    curB = curB->next;
                }
                sm--;
            }
            while(curB!=NULL){
                
                if(curA==curB){
                    return curA;
                }
                curA= curA->next;
                curB= curB->next;
            }
        }
        return NULL;
    }
};