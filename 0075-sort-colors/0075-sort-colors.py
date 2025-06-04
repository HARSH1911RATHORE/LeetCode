class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # l=0
        # r=len(nums)-1
        # i=0
        # while i<=r:
        #     if nums[i] == 0:
        #         nums[l], nums[i] = nums[i], nums[l]
        #         l+=1
        #         i+=1
        #     elif nums[i] == 2:
        #         nums[r], nums[i] = nums[i], nums[r]
        #         r-=1
        #     else:
        #         i+=1

        # return nums



        l = 0
        r = len(nums) - 1
        i = 0
        while i <=r:
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                i+=1
                l+=1
            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r-=1   
            else:
                i+=1
        return nums             



        # for i in range(len(nums)):   ##201   0) 201 102 1) 
            
        #     if nums[i]==0 and i<=r:# and l<len(nums)-1:
        #         nums[l],nums[i] = nums[i],nums[l]
        #         l+=1
        #     if nums[i]==2 and i<=r:# and r>0:
        #         nums[r],nums[i] = nums[i],nums[r]
        #         r-=1
        # return nums
        # i=0
        # while i<=r:
        #     if nums[i] == 0:
        #         nums[l],nums[i] = nums[i],nums[l]
        #         l+=1 
        #         i+=1
        #     elif nums[i] == 2:
        #         nums[r],nums[i] = nums[i],nums[r]
        #         r-=1 
        #     else:
        #         i+=1
        # return nums  
                     
            
        