class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0 
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k +=1
        return k
#Time Complexity : O[n]
#space Complexity : O[1]

def main():
    nums = [1,2,2,3,3,4]
    val = 2
    sol = Solution()
    s = sol.removeElement(nums,val)
    print(s)
    print(nums[:s])

if __name__ == "__main__":
    main()