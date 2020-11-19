def latest(scores):
    return scores[-1]

def personal_best(scores):
    scores.sort()
    return scores[-1]


def personal_top_three(scores):
    scores.sort()
    scores.reverse()
    l = len(scores)
    if l == 0:
        return "input is a empty list"
    if l <= 3:
        top = scores[0:l]
        print(top)
        return top
    top = scores[0:3]
    return top





