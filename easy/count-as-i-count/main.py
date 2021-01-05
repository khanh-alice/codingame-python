initialScore = int(input())


def count_solutions(score, turn):
    if score > 50 or turn > 4:
        return 0

    if score == 50:
        return 1

    result = count_solutions(score + 1, turn + 1)

    for i in range(2, 13):
        result += 2 * count_solutions(score + i, turn + 1)

    return result


print(count_solutions(initialScore, 0))
