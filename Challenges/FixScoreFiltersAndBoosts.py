# https://www.boot.dev/challenges/3d6c5f0c-97a3-47e4-b246-1e44ff676467
# ASSIGNMENT:
# Fix both functions so that:
# 1. filter_scores(scores, predicate) -> returns a new list
#    containing only the scores where predicate(score) is True
# 2. map_scores(scores, transform) -> returns a new list
#    where eachs core is replaced with transform(score)
# 
# Both functions should use other functions that are passed in as arguments.
# predicate is a function that takes a single score and returns True or False
# transform is a function that takes a single score and returns a new score
# 
def filter_scores(scores, predicate):
    result = []
    for score in scores:
        if predicate:
            result.append(score)
    return result


def map_scores(scores, transform):
    result = []
    for score in scores:
        result.append(transform)
    return result

# 

def is_passing(score):
    return score >= 60


def add_bonus_10(score):
    return score + 10


def is_high_score(score):
    return score > 90


def double_score(score):
    return score * 2


def is_even(score):
    return score % 2 == 0


def subtract_five(score):
    return score - 5


run_cases = [
    # Simple passing filter and flat bonus
    ([55, 60, 72, 40], is_passing, add_bonus_10, [60, 72], [65, 70, 82, 50]),
    # All scores passing, doubling
    ([95, 100], is_passing, double_score, [95, 100], [190, 200]),
]

submit_cases = run_cases + [
    # No scores passing
    ([10, 20, 30], is_passing, add_bonus_10, [], [20, 30, 40]),
    # High score filter
    ([80, 91, 92, 50], is_high_score, double_score, [91, 92], [160, 182, 184, 100]),
    # Empty list
    ([], is_passing, add_bonus_10, [], []),
    # Even scores and subtract
    ([1, 2, 3, 4, 5, 6], is_even, subtract_five, [2, 4, 6], [-4, -3, -2, -1, 0, 1]),
]


def test(scores, predicate, transform, expected_filtered, expected_mapped):
    print("---------------------------------")
    print(f"Input scores: {scores}")
    print("")

    filtered_result = filter_scores(scores, predicate)
    mapped_result = map_scores(scores, transform)

    print(f"Expected filtered: {expected_filtered}")
    print(f"Actual filtered:   {filtered_result}")
    print("")
    print(f"Expected mapped:   {expected_mapped}")
    print(f"Actual mapped:     {mapped_result}")

    correct_filtered = filtered_result == expected_filtered
    correct_mapped = mapped_result == expected_mapped

    if correct_filtered and correct_mapped:
        return True
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)

    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
            print("Pass")
        else:
            failed += 1
            print("Fail")

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
