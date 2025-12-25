'''Given an integer array nums sorted in non-decreasing order,
remove the duplicates in-place such that each unique element appears only once.'''

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        j = 0

        if not nums:
            return 0

        for i in range(1, len(nums)):
            if nums[j] !=nums[i]:
                j += 1
                nums[j] = nums[i]
        return j+1
        
        #Time Complexity : O[n]
        #space Complexity : O[1]
def main():
    nums = [1,1,2,2,3,4,8]

    sol  = Solution()
    result = sol.removeDuplicates(nums)

    print(result)
    print(nums[:result])

if __name__ == "__main__":
    main()
