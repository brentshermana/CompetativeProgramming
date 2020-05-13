INITIAL_SIZE = 20
LOAD_FACTOR = .7

class hashmap:
    def __init__(self, size = None):
        if size == None:
            size = INITIAL_SIZE
        self.K = []
        self.V = []
        for _ in range(size):
            self.K.append([])
            self.V.append([])
        self.size = 0
        self.cap = size*LOAD_FACTOR

    def put_elem(self, x, y):
        if self.size >= self.cap:
            self.resize()

        i = hash(x) % len(self.K)
        if x not in self.K[i]:
            self.K[i].append(x)
            self.V[i].append(y)
        else:
            j = self.K.index(x)
            self.V[i][j] = y

        self.size += 1

    def resize(self):
        # double size
        new = hashmap(size=len(self.K)*2)
        # copy over elements
        for kl, vl in zip(self.K, self.V):
            # print(type(kl))
            # print(type(vl))
            for k, v in zip(kl, vl):
                new.put_elem(k, v)

        self.__dict__ = new.__dict__ # copies over everything!

    def get_elem(self, x):
        i = hash(x) % len(self.K)
        j = self.K[i].index(x) # throws error if not present
        return self.V[i][j]

if __name__ == "__main__":
    x = 100

    h = hashmap()
    for i in range(x):
        h.put_elem(i,i)
    for i in range(x):
        print(h.get_elem(i))


