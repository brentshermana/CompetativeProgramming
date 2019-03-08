# You need to take n courses, labeled 0 -> n-1
# Some courses have prerequisites
# prequisites are given in the form
# [x, y], where y must be taken before x

# if there is no such ordering, return [-1]

# This is just plain old topological sort


def course_schedule(n, prerequisites):
    edges = [list() for _ in range(n)]
    indegree = [0 for _ in range(n)]

    for after, before in prerequisites:
        edges[before].append(after)
        indegree[after] += 1

    todo = [i for i in range(n) if indegree[i] == 0]
    done = []
    while len(todo) > 0:
        cur = todo.pop()
        done.append(cur)

        # adjust in-degrees of things cur points to
        for after in edges[cur]:
            indegree[after] -= 1
            if indegree[after] == 0:
                todo.append(after)

    if len(done) == n:
        return done
    else:
        return [-1]
