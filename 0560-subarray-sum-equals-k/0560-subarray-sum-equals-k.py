class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # sum = 0
        # count = 0
        # l = 0
        # for n in nums:
        #     sum += n
        #     while l < len(nums):
        #         if sum == k:
        #             count+=1
        #         sum -= nums[l]
        #         l += 1
        # Map_prefixsum = {0:1}
        # prefixsum = 0
        # count = 0
        # for n in nums:
        #     prefixsum += n
        #     diff = prefixsum - k
        #     count += Map_prefixsum.get(diff, 0)
        #     Map_prefixsum[prefixsum] = 1 + Map_prefixsum.get(prefixsum, 0)

        # return count


        Map = {0:1}
        prefixsum = 0
        res = 0
        for i in range(len(nums)):
            prefixsum += nums[i]
            diff = prefixsum - k
            res += Map.get(diff, 0)
            Map[prefixsum] = 1 + Map.get(prefixsum, 0)
        return res