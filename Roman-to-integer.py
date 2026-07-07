class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }
        const = 0
        
        for i in range(0, len(s) - 1):
            current = roman[s[i]]
            next = roman[s[i+1]]
            
            if current < next:
                const -= current
            else:
                const += current
                
        const += roman[s[-1]]
        return const


if __name__ == "__main__":
    # 1. Create an object instance of your class
    solution = Solution()
    
    # 2. Define test cases
    test_cases = ["III", "LVIII", "MCMXCIV"]
    
    # 3. Run and print results
    print("--- Running Test Cases ---")
    for case in test_cases:
        result = solution.romanToInt(case)
        print(f"Input: {case:<10} -> Output: {result}")
