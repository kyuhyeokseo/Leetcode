class Solution:
    def outerTrees(self, points: List[List[int]]) -> List[List[int]]:
        
        def lessCounterClockwise(p, q, r):
            return (q[1]-p[1]) * (r[0]-p[0]) - (q[0]-p[0]) * (r[1]-p[1]) > 0

        def constructHull(points):
            stack = []
            for p in points:
                while len(stack) >= 2 and lessCounterClockwise(stack[-2], stack[-1], p):
                    stack.pop()
                stack.append(tuple(p))
                #print(stack)

            return stack

        points.sort()
        left2right = constructHull(points)
        #print('-----------------------')
        right2left = constructHull(points[::-1])

        return list(set(left2right + right2left))