class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count=0
        for s in range(len(nums)-2):
            if (nums[s]+diff) in nums and (nums[s]+2*diff) in nums:
                count+=1
                print(nums[s],nums[s]+diff,nums[s]+2*diff)
        return count



