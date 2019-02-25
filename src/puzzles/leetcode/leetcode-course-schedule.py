# This is an algorithm! I don't remember what it's called...
# The idea is that you have some defined dependencies, so you track how many
# Things still need to happen before a thing. Just keep taking the things
# that have zero dependencies, and decrement the things that are waiting on them

class Solution:
    def canFinish(self, numCourses: 'int', prerequisites: 'List[List[int]]') -> 'bool':
        in_count = [0] * numCourses
        
        depends_on = [] # list o' lists
        for _ in range(numCourses):
            depends_on.append([])
        
        for after, before in prerequisites:
            depends_on[before].append(after)
            in_count[after] += 1
            
        # now, run the algorithm
        #  todo === the ones with nothing requiring them
        todo = [x for x in range(numCourses) if in_count[x] == 0]
        while len(todo) > 0:
            current = todo.pop()
            # all things that need current now need one less thing
            for after_current in depends_on[current]:
                in_count[after_current] -= 1
                # add to todo if appropriate
                if in_count[after_current] == 0:
                    todo.append(after_current)
                    
        return all( (count == 0 for count in in_count) )
    