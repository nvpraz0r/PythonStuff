def containsDuplicate(self, nums: List[int]) -> bool:
    """
    Docstring for containsDuplicate
    
    :param self: Description
    :param nums: Description
    :type nums: List[int]
    :return: Description
    :rtype: bool
    """

    # internal array
    result = set()

    # loop through parameter array
    for num in nums:
        # check if num is in parameter array
        if num in result:
            # return true if num is in parameter array
            return True
        # add num to internal array
        result.add(num)
    # if no duplicates are found return false
    return False


def main():
    containsDuplicate()


if __name__ == '__main__':
    main()