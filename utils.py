import json


def load_candidates():
    with open('candidates.json', 'r', encoding='UTF-8') as f:
        data = json.load(f)
    return data


def get_all():
    return load_candidates()


def get_by_pk(pk):
    for candidate in load_candidates():
        if candidate['pk'] == pk:
            return candidate
    return


def get_by_skill(skills):
    candidates = []
    for candidate in load_candidates():
        if skills.lower() in candidate['skills'].lower().split(', '):
            candidates.append(candidate)
    return candidates
