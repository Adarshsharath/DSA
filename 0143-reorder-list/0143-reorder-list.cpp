class Solution {
public:
    void reorderList(ListNode* head) {
        if (head == NULL || head->next == NULL)
            return;

        stack<ListNode*> st;

        ListNode* cur = head;
        int n = 0;

        while (cur != NULL) {
            st.push(cur);
            cur = cur->next;
            n++;
        }

        cur = head;


        for (int i = 0; i < n / 2; i++) {

            ListNode* next = cur->next;

            cur->next = st.top();
            st.pop();

            cur->next->next = next;

            cur = next;
        }

        cur->next = NULL;
    }
};