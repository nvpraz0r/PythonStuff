# !~ read the comments ~!
# each comment is a step in the assignment
# followed by it's code counterpart

def filter_messages(messages):
    # 1. create two empty arrays
    filtered_messages_array : list = []
    num_of_dangs_array : list = []

    # 2. loop over the array of messages for each message
    for message in messages:
        # 2a. split the message string into an array
        # of words using the .split() string method 
        words = message.split()

        # 2b. create an empty array for the good words
        good_words = []
        # 2c. create an empty array for the bad words
        bad_words = []

        # 2d. for each word in the message
        for word in words:
            # 2di. if the word is dang add it to the array of bad words
            if word == "dang":
                bad_words.append(word)
            # 2dii. if the word is not dang add it to the array of good words
            else:
                good_words.append(word)
        
        # 2e. join the list of good words into a single
        # string using the .join() string method
        sentance = " ".join(good_words)

        # 2f. append the new filtered message to the array
        # of filtered messages
        filtered_messages_array.append(sentance)

        # 2g. append the length of the list of bad words
        # to the array that counts the number of bad words
        num_of_dangs_array.append(len(bad_words))

    # 3. return the filtered messages, then the number of "dangs"
    return filtered_messages_array, num_of_dangs_array




run_cases = [
    (
        ["darn it", "this dang thing won't work", "lets fight one on one"],
        ["darn it", "this thing won't work", "lets fight one on one"],
        [0, 1, 0],
    ),
]

submit_cases = run_cases + [
    (
        [
            "well dang it",
            "dang the whole dang thing",
            "kill that knight, dang it",
            "get him!",
            "donkey kong",
            "oh come on, get them",
            "run away from the dang baddies",
        ],
        [
            "well it",
            "the whole thing",
            "kill that knight, it",
            "get him!",
            "donkey kong",
            "oh come on, get them",
            "run away from the baddies",
        ],
        [1, 2, 1, 0, 0, 0, 1],
    ),
]


def test(input, expected_output1, expected_output2):
    print("---------------------------------")
    print(f"Input:")
    print(f" * messages: {input}")
    print("Expected:")
    print(f" * filtered messages: {expected_output1}")
    print(f" * words removed: {expected_output2}")
    print("Actual:")
    try:
        result = filter_messages(input)
        print(f" * filtered messages: {result[0]}")
        print(f" * words removed: {result[1]}")
    except Exception as e:
        print(f"Error: {e}")
        print("Fail")
        return False

    if result == (expected_output1, expected_output2):
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
