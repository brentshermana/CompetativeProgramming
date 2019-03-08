# an alien dictionary is sorted. Determine the order of characters
# in that language

# assume that the input will introduce enough constraints
# such that the sorted alphabet can be determined uniquely

from collections import defaultdict

def find_order(words):
    edges = defaultdict(set)
    indegree = defaultdict(int)

    allchars = set()

    # handles edge case of only one word:
    if len(words[0]) > 0:
        allchars.add(words[0][0])

    for i in range(len(words)-1):
        a = words[i]
        b = words[i+1]
        for j in range(min(len(a), len(b))):
            if a[j] != b[j]:
                # we need the check to avoid
                # incrementing indegree
                # unnecessarily
                if b[j] not in edges[a[j]]:
                    allchars.add(a[j])
                    allchars.add(b[j])
                    edges[a[j]].add(b[j])
                    indegree[b[j]] += 1
                break

    todo = [c for c in allchars if indegree[c] == 0]
    order = []
    while len(todo) > 0:
        c = todo.pop()
        order.append(c)
        for after in edges[c]:
            indegree[after] -= 1
            if indegree[after] == 0:
                todo.append(after)

    return ''.join(order)

print(find_order(["baa", "abcd", "abca", "cab", "cad"]))
