import re

with open("regex_sum_1831259.txt") as f:
    text = f.read()
    matches = re.findall("[0-9]+", text)

    sum = 0
    for match in matches:
        sum += int(match)

    print(sum)
