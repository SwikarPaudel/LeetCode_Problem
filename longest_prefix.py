"""Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
"""
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        ans = ""
        for i in range(len(strs[0])):
            ch = strs[0][i]
            for j in strs:
                if i>=len(j) or ch!=j[i]:
                    return ans
            ans += ch
        return ans
#Time Complexity = O[N x M]  
#Space Complexity = O[1]
def main():
    strs = ["flower","flow","flight"]
    sol=Solution()
    result = sol.longestCommonPrefix(strs)
    print(result)

if __name__ == "__main__":
    main()