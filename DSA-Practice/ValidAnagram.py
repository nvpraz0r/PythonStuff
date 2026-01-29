# 242. Valid Anagram
#
# given two strings "s" and "t" return true
# if "t" is an anagram of "s", and false otherwise
#
def isAnagram( s: str, t: str) -> bool:
    """
    Docstring for isAnagram
    
    :param self: Description
    :param s: Description
    :type s: str
    :param t: Description
    :type t: str
    :return: Description
    :rtype: bool
    """

    # easy out
    if len(s) != len(t):
        return False

    # sort arrays
    s_sorted = sorted(s)
    t_sorted = sorted(t)

    s_string = "".join(s_sorted)
    t_string = "".join(t_sorted)

    for i in range(len(s)):
        if s_string[i] != t_string[i]:
            return False

    return True


def main():
    s = "anagram"
    t = "nagaram"
    result = isAnagram(s, t)
    print(result)


if __name__ == '__main__':
    main()