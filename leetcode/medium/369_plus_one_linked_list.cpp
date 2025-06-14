/*
 * 369. Plus One Linked List
 * Platform: LEETCODE
 * Difficulty: medium
 * Language: cpp
 * Problem URL: https://leetcode.com/problems/plus-one-linked-list/
 * Date: 2025-06-14T08:53:43.896Z
 * Author: CodeSync Extension
 */

head = reverse_list(head)                dummy = head        temp = head        carry = 1        while temp:            temp.val = ((temp.val + carry)%10)            carry = (temp.val + carry)//10            temp = temp.next        if carry:            temp.next = ListNode(carry)        return reverse_list(dummy)