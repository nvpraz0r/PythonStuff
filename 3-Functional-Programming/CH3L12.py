import copy

# create a copy of the memos dict
# if document exists in memos return the copy of memos and word count
# otherwise create a word count using word_count(foo)
# store the word count in the memos copy
# return the word count and update memos copy
# def word_count_memo(document, memos):
#     copied_memos = memos.copy()
#     if document in copied_memos:
#         return copied_memos(document), copied_memos
#     num_of_words = word_count(document)
#     copied_memos[document] = num_of_words
#     return num_of_words, copied_memos
# 
def word_count_memo(document, memos):
    
    # copied_memos = memos.copy()
    # if document not in copied_memos:
    #     copied_memos[document] = word_count(document)
    #     return new_memos[document], copied_memos
    # else:
    #     return copied_memos[document], copied_memos

        new_memos = memos.copy()

        if document in new_memos:
            return new_memos[document], new_memos
        
        new_memos[document] = word_count(document)

        return word_count(document), new_memos






# Don't edit below this line


def word_count(document):
    count = len(document.split())
    return count


run_cases = [
    (
        "My hovercraft is full of eels",
        {
            "My hovercraft is full of eels": 6,
            "He's a lumberjack and he's okay. He sleeps all night and he works all day": 15,
        },
        (
            6,
            {
                "My hovercraft is full of eels": 6,
                "He's a lumberjack and he's okay. He sleeps all night and he works all day": 15,
            },
        ),
    ),
    (
        "Spam, spam, spam, spam, spam, spam, baked beans, spam, spam, and spam",
        {},
        (
            12,
            {
                "Spam, spam, spam, spam, spam, spam, baked beans, spam, spam, and spam": 12
            },
        ),
    ),
]

submit_cases = run_cases + [
    (
        "This is an ex-parrot",
        {"This parrot is no more": 5},
        (4, {"This parrot is no more": 5, "This is an ex-parrot": 4}),
    ),
    (
        "This doc should 'incorrectly' have 9999 words to test that the memoization is working",
        {
            "My hovercraft is full of eels": 6,
            "This doc should 'incorrectly' have 9999 words to test that the memoization is working": 9999,
        },
        (
            9999,
            {
                "My hovercraft is full of eels": 6,
                "This doc should 'incorrectly' have 9999 words to test that the memoization is working": 9999,
            },
        ),
    ),
]


def test(input_document, input_memos, expected_output):
    print("---------------------------------")
    print(f"Input document:\n  {input_document}")
    print(f"Input memos:")
    for key, value in input_memos.items():
        print(f"  {key}: {value}")
    print(f"Expected word count: {expected_output[0]}")
    print(f"Expected memos:")
    for key, value in expected_output[1].items():
        print(f"  {key}: {value}")
    input_memos_copy = input_memos.copy()
    result = word_count_memo(input_document, input_memos_copy)
    print(f"Actual word count: {result[0]}")
    print(f"Actual memos:")
    for key, value in result[1].items():
        print(f"  {key}: {value}")

    if input_memos_copy != input_memos:
        print("Mutated input memos\nFail")
        return False
    if input_memos == expected_output[1] and result[1] != expected_output[1]:
        print("Expected word count from the input memos\nFail")
        return False
    if result != expected_output:
        print("Fail")
        return False
    print("Pass")
    return True


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
