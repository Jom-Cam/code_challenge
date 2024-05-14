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
# string_match = { 
#                 '[' : ']',
#                 '{' : '}',
#                 '(' : ')'
#                 }

print(test_string_1)

def matching(input):
    current_bracket = ''
    for check in input:
        if check != ' ':
            if check == '[' or check == '{' or check == '(':
                current_bracket = check  # Update the current open bracket
                print(f'we are on character {check}')
                print(f'we currently have the open bracket of {current_bracket}')
            elif check == ']' or check == '}' or check == ')':
                if (current_bracket == '[' and check != ']') or \
                   (current_bracket == '{' and check != '}') or \
                   (current_bracket == '(' and check != ')'):
                    print("Invalid format")
                    return
                current_bracket = ''  # Reset current_bracket after closing the bracket
    if current_bracket:  # If there are unclosed opening brackets
        print("Invalid format, bracket found but not closed")
        return
    
    print("Valid format")

matching(test_string_1)