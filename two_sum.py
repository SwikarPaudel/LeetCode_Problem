<<<<<<< HEAD
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


def main():
    nums = [2,7,11,13]
    target = 9


    sol = Solution()
    result = sol.twoSum(nums, target)

    print(result)


if __name__ == "__main__":
    main()
=======
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


def main():
    nums = [2,7,11,13]
    target = 9

    sol = Solution()
    result = sol.twoSum(nums, target)

    print(result)


if __name__ == "__main__":
    main()

>>>>>>> 56df374ce9cf56227c2bebcddd21eb1ce19a7bdb
