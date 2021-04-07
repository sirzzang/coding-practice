import re
from itertools import permutations


def check(user_id, banned_id):
    for i in range(len(user_id)):
        if len(banned_id[i]) != len(user_id[i]):
            return False
        if not re.fullmatch(banned_id[i], user_id[i]):
            return False
    return True


def solution(user_id, banned_id):
    banned_id = [_id.replace('*', '.') for _id in banned_id]
    bad_users = []

    for perm in permutations(user_id, len(banned_id)):
        if check(perm, banned_id) and set(perm) not in bad_users:
            bad_users.append(set(perm))
    return len(bad_users)
