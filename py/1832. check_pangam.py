# 2
# letters are lowercase
class Solution:
	def checkIfPangram(self, sentence: str) -> bool:
			seen = set(sentence)
			return len(seen) == 26


#1
# if letters are lowercase and uppercase
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
            o = set(char)
            for i in range(len(sentence)):
                char = sentence[i]
                n = ord(char.lower()) - ord('a') + 1
                o.add(n)
            return len(o) == 26
            