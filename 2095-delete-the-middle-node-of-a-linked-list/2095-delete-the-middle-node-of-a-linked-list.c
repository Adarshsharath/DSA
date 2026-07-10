struct ListNode* deleteMiddle(struct ListNode* head) {

    if (head == NULL || head->next == NULL) {
        free(head);
        return NULL;
    }

    struct ListNode* fast = head;
    struct ListNode* cur = head;
    struct ListNode* prev = NULL;

    while (fast != NULL && fast->next != NULL) {
        fast = fast->next->next;

        prev = cur;
        cur = cur->next;
    }

    prev->next = cur->next;
    free(cur);

    return head;
}