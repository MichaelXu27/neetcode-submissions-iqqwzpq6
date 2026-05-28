class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        dic = defaultdict(set)
        wordList = set(wordList)
        for word in wordList:
            for i in range(len(word)):
                temp = word[0:i] + "*" + word[i + 1:]
                dic[temp].add(word)
        
        queue = deque()
        queue.append(beginWord)
        seen = set()
        seen.add(beginWord)
        count = 1

        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                for i in range(len(word)):
                    temp = word[0:i] + "*" + word[i + 1:]
                    for candidate in dic[temp]:
                        if candidate in seen:
                            continue
                        seen.add(candidate)
                        queue.append(candidate)
                        if candidate == endWord:
                            return count + 1
            count += 1
        return 0
