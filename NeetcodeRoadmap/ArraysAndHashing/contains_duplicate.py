# LC Problem 217
# Easy
# Topic: Arrays and Hashing

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return self.sets_approach(nums)


    def hashmap_approach(self, nums: List[int]) -> bool:
        # TC: O(n)
        # SC: O(n) -- map creation set() uses this under the hood
        m = {}

        for num in nums:
            if num in m:
                return True
            else:
                m[num] = 0
        return False


    def sets_approach(self, nums: List[int]) -> bool:
        # TC: O(n)
        # SC: O(n) - new set creation
        nums_set = set(nums)
        return len(nums_set) != len(nums)
        