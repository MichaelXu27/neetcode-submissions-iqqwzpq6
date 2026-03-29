class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        zipped = list(zip(position, speed))
        zipped.sort(reverse = True)
        timeToTarget = [((target - position) / speed) for position, speed in zipped]
        stack = []
        for time in timeToTarget:
            if not stack:
                stack.append(time)
            else:
                popped = stack.pop()
                if popped < time:
                    stack.append(popped)
                    stack.append(time)
                else:
                    stack.append(popped)
        return len(stack)
