/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* partition(struct ListNode* head, int x) {
    struct ListNode smallDummy;
    smallDummy.next = NULL;
    struct ListNode *small = &smallDummy;

    struct ListNode largeDummy;
    largeDummy.next = NULL;
    struct ListNode *large = &largeDummy;

    struct ListNode *cur = head;

    while (cur != NULL) {

        struct ListNode *nn = malloc(sizeof(struct ListNode));
        nn->val = cur->val;
        nn->next = NULL;

        if (cur->val < x) {
            small->next = nn;
            small = nn;          // Move tail forward
        } else {
            large->next = nn;
            large = nn;          // Move tail forward
        }

        cur = cur->next;
    }

    small->next = largeDummy.next;

    return smallDummy.next;
}