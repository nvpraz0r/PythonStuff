# 
# this took way longer than I really care to admit
# observe the goober who started learning with java in it's natural habitat
# "i KnOw HoW tO Do ThIs In JaVa"
# 
def remove_duplicates(spells):
    # for i in range(len(spells)):
    #     if i == result[i]:
    #         result.add(i)

    # while len(result) != len(spells):
    #     for i, j in zip(spells, result):
    #         if i != j:
    #             result.add(i)

    # for i in range(1, len(spells)):
    #     if spells[i] != spells[i - 1]:
    #         result.add(i)
    result = list()

    for spell in spells:
        if spell not in result:
            result.append(spell)


    return result


run_cases = [
    (
        [
            "fireball",
            "eldritch blast",
            "fireball",
            "eldritch blast",
            "chill touch",
            "eldritch blast",
            "chill touch",
            "chill touch",
            "fireball",
            "fireball",
            "shocking grasp",
            "fireball",
            "fireball",
        ],
        ["chill touch", "eldritch blast", "fireball", "shocking grasp"],
    )
]

submit_cases = run_cases + [
    (["fireball", "fireball", "fireball"], ["fireball"]),
    (
        ["fireball", "eldritch blast", "chill touch", "shocking grasp"],
        ["chill touch", "eldritch blast", "fireball", "shocking grasp"],
    ),
    (["chill touch", "chill touch", "chill touch"], ["chill touch"]),
    (["shocking grasp", "shocking grasp", "shocking grasp"], ["shocking grasp"]),
    ([], []),
    (["eldritch blast", "eldritch blast", "eldritch blast"], ["eldritch blast"]),
]


def test(input, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * spells: {input}")
    print(f"Expected:  {expected_output}")
    result = remove_duplicates(input)
    print(f"   Actual: {result}")
    if not isinstance(result, list):
        print("Fail: result is not a list")
        return False
    result.sort()
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
