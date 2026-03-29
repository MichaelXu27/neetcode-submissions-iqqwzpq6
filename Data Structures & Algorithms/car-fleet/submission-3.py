class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        zipped = list(zip(position, speed))
        zipped.sort(reverse = True)
        times = []
        for pos, spe in zipped:
            times.append((target-pos)/spe)
        stack = []
        for time in times:
            if not stack:
                stack.append(time)
            else:
                mostRecent = stack[-1]
                if mostRecent < time:
                    stack.append(time)
        return len(stack)