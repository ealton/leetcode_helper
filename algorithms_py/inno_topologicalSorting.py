# Think of topological sort as a course schedule problem, a directed tree, we need to schedule the courses in an order, so each course is only taken when all of its preceding courses are taken


import collections
from typing import List


courses = [[1,0],[1,2],[3,1],[3,2],[2,4],[4,5],[2,5]]
# where courses[i] = [current, pre]


def topologicalSort(conditions: List[List[int]]) -> bool:
    courseMap = collections.defaultdict(list)
    courseSet = set()
    for c, p in conditions:
        courseSet.add(p)
    for c, p in conditions:
        courseMap[p].append(c)
        if c in courseSet:
            courseSet.remove(c)
    courseDegree = {}

    def dfs(course) -> int:
        if len(courseMap[course]) == 0:
            # a leaf course, has a degree of zero
            courseDegree = courseDegree[course] = 0
            return 0
        d = 0
        for nextCourse in courseMap[course]:
            nextCourseDegree = dfs(nextCourse)
            d = min(d, nextCourseDegree-1)
        if course not in courseDegree or d < courseDegree[course]:
            courseDegree[course] = d
        return courseDegree[course]

    for c in courseSet:
        dfs(c)

    print(courseDegree)
    return courseDegree

