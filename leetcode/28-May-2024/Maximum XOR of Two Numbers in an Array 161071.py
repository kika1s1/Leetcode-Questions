# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class TrieNode:
    def __init__(self):
        self.children = {}


def insert(root, binary_str):
    node = root
    for bit in binary_str:
        if bit not in node.children:
            node.children[bit] = TrieNode()
        node = node.children[bit]


def findMaxXOR(nums):
    max_xor = 0
    max_length = len(bin(max(nums))) - 2

    root = TrieNode()
    for num in nums:
        binary_str = format(num, '0' + str(max_length) + 'b')
        insert(root, binary_str)

    for num in nums:
        binary_str = format(num, '0' + str(max_length) + 'b')
        current_xor = 0
        node = root

        for bit in binary_str:
            complement = '0' if bit == '1' else '1'
            if complement in node.children:
                current_xor = current_xor << 1 | 1
                node = node.children[complement]
            else:
                current_xor = current_xor << 1
                node = node.children[bit]

        max_xor = max(max_xor, current_xor)

    return max_xor



class Solution:
  def findMaximumXOR(self, nums: List[int]) -> int:
    return findMaxXOR(nums)