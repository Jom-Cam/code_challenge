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

test_string_1 = ' ] {} ()'
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
    
    for x in input:

        if input_start_with_closing(x, closing_brackets, current_bracket):
            print('Invalid')
            return
        if x != ' ' and x in opening_brackets:
            current_bracket = x  # Update the current open bracket
        else :
            if (current_bracket == '[' and x != ']') or \
                (current_bracket == '{' and x != '}') or \
                (current_bracket == '(' and x != ')'):
                print("Invalid format")
                return
            current_bracket = ''  # Reset current_bracket after closing the bracket

    if current_bracket:  # If there are unclosed opening brackets
        print("Invalid format, open bracket found but not closed")
        return
    
    print("Valid format")

def input_start_with_closing(input, closing_brackets, current_bracket):
     return input in closing_brackets and current_bracket == ''


matching(test_string_1)
