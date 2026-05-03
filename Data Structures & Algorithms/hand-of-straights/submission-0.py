class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        counts = Counter(hand)
        hand.sort()
        for num in hand:
            if counts[num] == 0:
                continue
            else:
                counts[num] -= 1
                for i in range(1, groupSize):
                    if counts[num + i] == 0:
                        return False
                    counts[num + i] -= 1

        return True