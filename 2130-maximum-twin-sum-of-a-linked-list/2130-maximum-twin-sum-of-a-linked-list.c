/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* getmid(struct ListNode* head){
    struct ListNode* first = head;
    struct ListNode* prev = NULL;

    while(first != NULL && first->next != NULL){
        first = first->next->next;
        prev = head;
        head = head->next;
    }

    prev->next = NULL;
    return head;
}

struct ListNode* rev(struct ListNode* head){
    struct ListNode* prev = NULL;
    struct ListNode* cur = head;
    struct ListNode* next = NULL;

    while(cur != NULL){
        next = cur->next;
        cur->next = prev;
        prev = cur;
        cur = next;
    }

    return prev;
}

int pairSum(struct ListNode* head){
    struct ListNode* first = head;
    struct ListNode* mid = getmid(head);
    struct ListNode* second = rev(mid);

    int max = 0;
    int sum = 0;

    while(second != NULL){
        sum = first->val + second->val;

        if(sum > max){
            max = sum;
        }

        first = first->next;
        second = second->next;
    }

    return max;
}