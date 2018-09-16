import itertools


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# next earliest time with some permutation of these digits:
# "HH:MM"
# returns string matching that new permutation

def valid_time(timeStr):
    return valid_hour(timeStr[:2]) and valid_minute(timeStr[3:])


def valid_hour(hourStr):
    i = int(hourStr)
    return i < 24


def valid_minute(minuteStr):
    i = int(minuteStr)
    return i < 60


def dist(a, b):
    # a and b are times. returns the minutes between a and b
    if a == b: return 60 * 24

    hDiff = int(b[:2]) - int(a[:2])
    mDiff = int(b[3:]) - int(a[3:])
    if hDiff <= -1:
        return (24 + hDiff) * 60 + mDiff
    elif hDiff == 0 and mDiff <= -1:
        return 24 * 60 + mDiff
    else:
        return hDiff * 60 + mDiff


def solution(S):
    # generate all the permutations
    numbers = list(filter(lambda c: c != ':', S))
    times = [''.join(p[:2] + (':',) + p[2:]) for p in itertools.permutations(numbers)]
    print(times)
    times = list(filter(valid_time, times))
    print(times)
    return min(times, key=lambda t: dist(S, t))


while True:
    a = input()
    print(solution(a))