q_a = {
    "What's after A?": "b",
    "What's Fastest Animal in the world?": "cheetah",
    "What is the Capital of Nigeria?": "abuja"
}

def CalculateScorePercentage(Score):
    return (Score/len(q_a)) * 100
def ask_questions():
    score = 0
    for Questions in q_a:
        answer = input(Questions)
        if answer.lower() == q_a.get(Questions):
            score += 1
    return score
ask_questions()