from nltk.metrics.distance import edit_distance
from config import VERBEN


def possible_answer(message):
    verbs = VERBEN
    possible_verbs = []
    for verb in verbs:
        dist = edit_distance(message.text.lower(), verb)
        if dist <= 2:
            possible_verbs.append(verb)
    return possible_verbs
