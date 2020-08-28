def ranking_scores(scores):
    lists = sorted(scores)

    if len(scores) < 3:
        raise ValueError;

    reScores = []
    count = 0
    for i in range(len(scores)):
        if count < 5:
            reScores.append(lists[i])
            count += 1
    return reScores


class Test:
    print(ranking_scores([68, 72, 73, 69, 69, 64, 63, 75]))