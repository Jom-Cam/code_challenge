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
    opening_brackets = "([{"
    closing_brackets = ")]}"
    
    for check in input:
        if check != ' ':
            if check in opening_brackets:
                current_bracket = check  # Update the current open bracket
            elif check in closing_brackets:
                if not current_bracket:  # If no opening bracket found
                    print("Invalid format, closed bracket found but not opened")
                    return
                if (current_bracket == '[' and check != ']') or \
                   (current_bracket == '{' and check != '}') or \
                   (current_bracket == '(' and check != ')'):
                    print("Invalid format")
                    return
                current_bracket = ''  # Reset current_bracket after closing the bracket
    if current_bracket:  # If there are unclosed opening brackets
        print("Invalid format, open bracket found but not closed")
        return
    
    print("Valid format")

matching(test_string_1)
