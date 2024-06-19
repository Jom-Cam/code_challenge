# Given an integer x, return true if x is a 
# palindrome
# , and false otherwise.

# Example 1:
# Input: x = 121 Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Example 2:
# Input: x = -121 Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:
# Input: x = 10 Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

input = 111111

def isItpalindrome(x):
    x = str(x)

    # if x[1] != x[-1]:
    #     print("not")
        
    # else: 
      

        # a[start:stop]  # items start through stop-1
        # a[start:]      # items start through the rest of the array
        # a[:stop]       # items from the beginning through stop-1
        # a[:]           # a copy of the whole array

    while len(x) > 1:
        current_first_letter = x[0]
        current_last_letter = x[-1]
        x = x [1 : -1]

        if current_first_letter != current_last_letter:
            print("Not Palindrome")
            return False
        
    print("Palindrome")
    return True


isItpalindrome(input)