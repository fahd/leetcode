class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
            o = set()
            for i in range(len(sentence)):
                char = sentence[i]
                n = ord(char.lower()) - ord('a') + 1
                o.add(n)
            return len(o) == 26
            