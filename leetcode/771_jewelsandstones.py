"""
input: str, output: int

Example 1:
	Input: J = "aA", S = "aAAbbbb"
	Output: 3

Example 2:
	Input: J = "z", S = "ZZ"
	Output: 0

** The letters in J are guaranteed distinct, and all characters in J and S are letters. 
   Letters are case sensitive, so "a" is considered a different type of stone from "A".
"""

def numJewelsInStones(self, J: str, S: str) -> int:
	cnt = 0

	for j in J:

		for s in S:
			if s == j:
				cnt += 1

	return (cnt)

# J = "aA"
# S = "aAAbbbb"

J = "z" 
S = "ZZ"

numJewelsInStones(J, S)
