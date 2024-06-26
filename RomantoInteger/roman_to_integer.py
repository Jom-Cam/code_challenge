# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

# Examples:

# Input: s = "III" _ Output: 3 _ Explanation: III = 3.
# Input: s = "LVIII" _ Output: 58 _ Explanation: L = 50, V= 5, III = 3.
# Input: s = "MCMXCIV" _ Output: 1994 _ Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

# Constraints:

# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].
input = "IIM"

def roman_to_int(x):
    # Map of Roman numeral characters to their integer values
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    current_total = 0
    n = len(x)
    
    for i in range(n):
        # If the current value is less than the next value, subtract it
        if i < n - 1 and roman_map[x[i]] < roman_map[x[i + 1]]:
            current_total -= roman_map[x[i]]
            print(roman_map[x[i]])
        else:
            current_total += roman_map[x[i]]
            print(roman_map[x[i]])
    
    return current_total


print(roman_to_int(input))