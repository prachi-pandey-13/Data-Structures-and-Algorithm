from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:

        wordset = set(wordList)

        if endWord not in wordset:
            return []

        parents = defaultdict(list)
        queue = deque([beginWord])

        wordset.discard(beginWord)
        found = False

        # BFS
        while queue and not found:

            levelsize = len(queue)
            chosenwords = set()

            for _ in range(levelsize):

                word = queue.popleft()

                for i in range(len(word)):

                    for ch in "abcdefghijklmnopqrstuvwxyz":

                        if ch == word[i]:
                            continue

                        newword = word[:i] + ch + word[i+1:]

                        if newword in wordset:

                            parents[newword].append(word)

                            if newword not in chosenwords:
                                chosenwords.add(newword)
                                queue.append(newword)

                            if newword == endWord:
                                found = True

            wordset -= chosenwords

        # Backtracking
        result = []
        path = [endWord]

        def dfs(word):

            if word == beginWord:
                result.append(path[::-1])
                return

            for parent in parents[word]:
                path.append(parent)
                dfs(parent)
                path.pop()

        if found:
            dfs(endWord)

        return result