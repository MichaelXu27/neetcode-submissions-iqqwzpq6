class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        stack = []
        position_speed = [(p, s) for p, s in zip(position, speed)]

        position_speed.sort()

        for pos, speed in position_speed:
            time = (target - pos) / speed

            while stack and stack[-1] <= time:
                stack.pop()
                
            stack.append(time)

        return len(stack)