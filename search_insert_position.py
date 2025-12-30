class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i]>= target:
                return i
        return len(nums)
    
def main():
    #sorted array
    nums = [1,2,4,5,8]
    target = 3
    sol = Solution()              # create object
    result = sol.searchInsert(nums, target)  # call method
    print(result)

if __name__ == "__main__":
    main()