class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        mask, n=(1<<maximumBit)-1, len(nums)
        ans=[0]*n
        ans[-1]=nums[0]^mask
        for i in range(1, n):
            ans[~i]^=(ans[n-i]^nums[i])
        return ans
