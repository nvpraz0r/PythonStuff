# 125. Valid Palindrome
#
# A phrase is a palindrome if, after converting all uppercase letters
# into lowercase letters and removing all non-alphanumerice characters
# it reads the same forward and backward. Alphanumeric characters
# include letters and numbers
#
# Given the string "s" return "true" if it is a palindrome or "false" otherwise
#
def isPalindrome(s: str) -> bool:
    """
    Time:    
    :param s: Description
    :type s: str
    :return: Description
    :rtype: bool
    """

    if s == " ":
        return True

    cleaned_text = ''.join(char for char in s if char.isalnum())

    s = cleaned_text
    s_lower = s.lower()

    s_reversed = s[::-1]
    s_ = s_reversed.lower()

    for i in range(len(s)):
        if s_[i] != s_lower[i]:
            return False

    return True


def improvedIsPalindrome(s: str) -> bool:
    result = ''
    for c in s:
        if c.isalnum():
            result += c.lower()
    return result == result[::-1]

def main():
    result = isPalindrome("anna")
    print(result)


if __name__ == '__main__':
    main()