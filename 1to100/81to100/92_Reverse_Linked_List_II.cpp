/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        if(!head || left == right) {
            return head;
        }

        ListNode* dummy = new ListNode(-1);
        dummy->next = head;
        ListNode* prev = dummy;

        // Move prev to the node before the left position
        for (int i = 1; i < left; i++) {
            prev = prev->next;
        }

        ListNode* curr = prev->next;
        ListNode* nextNode = curr->next;

        // Reverse nodes from left to right
        for (int i = 0; i < right - left; i++) {
            curr->next = nextNode->next;
            nextNode->next = prev->next;
            prev->next = nextNode;
            nextNode = curr->next;
        }

        return dummy->next;
    }
};
