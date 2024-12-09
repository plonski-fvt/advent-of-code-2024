import re

# file = open("day07-test.txt")
file = open("day07-input.txt")


def count_answers(result, arguments):
    if len(arguments) == 1:
        return result == arguments[0]
    if result < arguments[0]:
        return 0  # since there's no way to decrease
    next_arguments_plus = [arguments[0] + arguments[1]] + arguments[2:]
    next_arguments_times = [arguments[0] * arguments[1]] + arguments[2:]
    next_argument_concat = [int(str(arguments[0]) + str(arguments[1]))] + arguments[2:]
    return (
        count_answers(result, next_arguments_plus)
        + count_answers(result, next_arguments_times)
        + count_answers(result, next_argument_concat)
    )


total_result = 0
for line in file:
    matches = re.findall(r"(\d+)", line)
    result = int(matches[0])
    arguments = [int(m) for m in matches[1:]]
    print(result)
    print(arguments)
    answers = count_answers(result, arguments)
    print(answers)
    if answers > 0:
        total_result += result

print(total_result)
