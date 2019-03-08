# input is a square binary matrix, like the following:
# 110 <- each row is a zombie. 1 means 'connected'.
# 110    so this guy is connected to himself and zombie #1
# 001 <- This guy is an island, he is just connected to himself

# return the number of clusters

# we can just do a 'fill' type traversal
# fundamentally, the input is an adjacency matrix

# Complete the zombieCluster function below.
def zombieCluster(zombies):
    n = len(zombies)

    # an array will be faster than a normal set
    visited = [False for _ in range(n)]

    clusters = 0

    for start in range(n):
        if not visited[start]:
            # print("CLUSTER BEGIN")

            clusters += 1

            # "fill" the cluster
            visited[start] = True
            stack = [start]
            while len(stack) > 0:
                i = stack.pop()
                # print("  current: {}".format(i))
                for j in range(n):
                    if zombies[i][j] == '1' and not visited[j]:
                        # print("    adj: {}".format(j))
                        visited[j] = True
                        stack.append(j)

    return clusters

print(zombieCluster([[1,1,0,0],[1,1,1,0],[0,1,1,0],[0,0,0,1]]))