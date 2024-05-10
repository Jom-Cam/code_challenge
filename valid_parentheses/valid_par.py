# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false

# Constraints:
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

test_string_1 = ' [] {} ()'
current_bracket = ''
string_match = { 
                '[' : ']',
                '{' : '}',
                '(' : ')'
                }

print(test_string_1)

def matching(input, check):
    current_bracket = ''
    for test in input:
       if test != ' ':
           print(f'we are on index {test}')
           print(f'we currently have the open bracket of {current_bracket}')

matching(test_string_1,'}')