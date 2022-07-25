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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* sentinel = new ListNode(0);
        sentinel->next = head;
        ListNode* ptr = sentinel;
        
        int duplicate;
        while(ptr->next && ptr->next->next){
            // check if there's duplicates
            if(ptr->next->val == ptr->next->next->val){
                // save duplicated value
                duplicate = ptr->next->val;
                // check for next values
                while(ptr->next && ptr->next->val == duplicate){
                    // move pointer till no duplicate
                    ptr->next = ptr->next->next;
                }
            }
            else{
                // move one slot 
                ptr = ptr->next;
            }
        }
        return sentinel->next;
    }
};
