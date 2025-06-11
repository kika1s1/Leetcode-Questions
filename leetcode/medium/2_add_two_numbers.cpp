/*
 * 2. Add Two Numbers
 * Platform: LEETCODE
 * Difficulty: medium
 * Language: cpp
 * Problem URL: https://leetcode.com/problems/add-two-numbers/description/
 * Date: 2025-06-11T18:55:58.235Z
 * Author: CodeSync Extension
 */

class Solution:    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:        if not l1 and not l2:            return None        elif not l1:            return l2        elif not l2:            return l1        a = l1.val + l2.val        head = ListNode(a % 10)        head.next = self.addTwoNumbers(l1.next, l2.next)        if a >= 10:            head.next = self.addTwoNumbers(head.next, ListNode(1))        return head