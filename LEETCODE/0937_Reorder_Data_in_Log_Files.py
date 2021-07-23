from typing import List


def reorderLogFiles(logs: List[str]) -> List[str]:

    # classify log types
    letter_logs, digit_logs = [], []
    for log in logs:
        identifier, content = log.split(
            maxsplit=1)[0], log.split(maxsplit=1)[1]
        if content.replace(' ', '').isdigit():
            digit_logs.append([identifier, content])
        else:
            letter_logs.append([identifier, content])
    print(letter_logs, digit_logs)

    # sort letter logs by their contents and then identifier lexicographically
    letter_logs.sort(key=lambda x: (x[1], x[0]))

    # letter logs come before digit logs
    letter_logs = [' '.join(letter_log) for letter_log in letter_logs]
    digit_logs = [' '.join(digit_log) for digit_log in digit_logs]

    return letter_logs + digit_logs


reorderLogFiles(["dig1 8 1 5 1", "let1 art can", "dig2 3 6",
                 "let2 own kit dig", "let3 art zero"])
