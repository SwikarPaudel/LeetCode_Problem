# Given an integer x, return true if x is a palindrome, and false otherwise.
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = x # save original number as s
        reversed_num = 0 
         
        while x>0:
           d = x % 10
           reversed_num = reversed_num * 10  + d
           x = x // 10

        if s == reversed_num:
            return True
        else: 
            return False
        
def main():
    x = 12321
    sol = Solution()
    result = sol.isPalindrome(x)
    print(result)

if __name__ == "__main__":
    main()