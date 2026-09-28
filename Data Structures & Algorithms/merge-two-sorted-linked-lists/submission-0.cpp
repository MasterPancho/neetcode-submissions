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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        // Edge cases
        if (list1 == NULL) {
            return list2;
        }
        else if (list2 == NULL) {
            return list1;
        }

        ListNode* cur1 = list1;
        ListNode* cur2 = list2;
        ListNode* mergeList;

        // Choose first node in the mergeList
        if (cur1->val <= cur2->val) {
            mergeList = cur1;
            cur1 = cur1->next;
        }
        else {
            mergeList = cur2;
            cur2 = cur2->next;
        }

        ListNode* tail = mergeList;

        while (cur1 != NULL && cur2 != NULL) {
 
            //From list 1
            if (cur1->val <= cur2->val) {
                tail->next = cur1;
                cur1 = cur1->next;
            }

            //From list 2
            else {
                tail->next = cur2;
                cur2 = cur2->next;
            }

            //Get the next node
            tail = tail->next;
        }

        if (cur1 != NULL)
            tail->next = cur1;
        else
            tail->next = cur2;

        return mergeList;
    }
};
    
