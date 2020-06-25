leftKeys = "qwertasdfgzxcvb"
rightKeys = "yuiophjklnm"

#Part One - All words, sorted by length
with open("words.txt") as file:
	wordList = file.read().split()
wordList = sorted(wordList, key=len)
input(wordList)

#Part Two - All words typable with my right hand
outWords = []
for word in wordList:
	for letter in word:
		if letter.lower() in rightKeys:
			break
	else:
		outWords.append(word)
input(outWords)

#Part Three - All words typable with my left hand
outWords = []
for word in wordList:
	for letter in word:
		if letter.lower() in leftKeys:
			break
	else:
		outWords.append(word)
input(outWords)

#Part Four - All words typable with alternating hands
outWords = []
for word in wordList:
	checkLeft = True
	for letter in word:
		if checkLeft and letter in rightKeys:
			break
		if not checkLeft and letter in leftKeys:
			break
		checkLeft = not checkLeft
	else:
		outWords.append(word)
input(outWords)