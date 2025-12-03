def reverse_list(items):
    result : list = []
    # helper variable
    items_len = len(items)

    for i in range(items_len, 0, -1):
        # unsure why items[i - 1] works but it does ¯\_(ツ)_/¯
        result.append(items[i - 1])

    return result


run_cases = [
    (
        ["Shortsword", "Healing Potion", "Iron Breastplate", "Kite Shield"],
        ["Kite Shield", "Iron Breastplate", "Healing Potion", "Shortsword"],
    ),
    ([1, 2, 300, 4, 5], [5, 4, 300, 2, 1]),
]

submit_cases = run_cases + [
    ([], []),
    (["a"], ["a"]),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),
    (
        ["apple", "banana", "cherry", "date", "elderberry"],
        ["elderberry", "date", "cherry", "banana", "apple"],
    ),
    (["hello", "world"], ["world", "hello"]),
]


def test(input, expected_output):
    print("---------------------------------")
    print(f"Input list: {input}")
    print(f"Expected reversed list: {expected_output}")
    result = reverse_list(input)
    print(f"Actual reversed list: {result}")
    if result == expected_output:
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
