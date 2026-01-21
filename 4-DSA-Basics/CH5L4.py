def power_set(input):
    # if the input list is empty return the powerset of an empty set
    # ( list containing an empty list )
    if len(input) == 0:
        return[[]]

    # otherwise create a list named "all_subsets"
    # ensure "all_subsets" contains an empty list to start
    all_subsets = [[]]

    # for each element in the input list
    for i in range(1, len(input)):
        # create an empty list named "new_subsets"
        new_subset = []
        # for each "subset" in "all_subsets"
        for subset in all_subsets:
            # create a new subset that contains all the elements of "subset" plus the current element
            
            # append the "new_subset" to the "new_subsets"

        # after the inner loop use extend to add "new_subsets" to "all_subsets"


    return input


#
#
#


run_cases = [
    ([1, 2], [[], [1], [2], [1, 2]]),
    ([1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]),
]

submit_cases = run_cases + [
    ([], [[]]),
    ([1], [[], [1]]),
    (
        [1, 2, 3, 4],
        [
            [],
            [1],
            [2],
            [1, 2],
            [3],
            [1, 3],
            [2, 3],
            [1, 2, 3],
            [4],
            [1, 4],
            [2, 4],
            [1, 2, 4],
            [3, 4],
            [1, 3, 4],
            [2, 3, 4],
            [1, 2, 3, 4],
        ],
    ),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    for i in input1:
        print(f" * {i}")
    print(f"Expected: {expected_output}")
    result = power_set(input1)
    print(f"Actual:   {result}")
    sorted_result = sorted([sorted(inner) for inner in result])
    sorted_expected_output = sorted([sorted(inner) for inner in expected_output])
    if sorted_result == sorted_expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
