def touchToneLetters(codeIn):
	codeIn = codeIn.replace(" "," 0 ")
	codeIn = codeIn.replace("-"," ")
	stringOut = ""
	for i in codeIn.split():
		stringOut += phoneLetters[int(i[0])][len(i)-1]
	return stringOut

phoneLetters = [[" "],[]]
phoneLetters.append(["a","b","c"])
phoneLetters.append(["d","e","f"])
phoneLetters.append(["g","h","i"])
phoneLetters.append(["j","k","l"])
phoneLetters.append(["m","n","o"])
phoneLetters.append(["p","q","r","s"])
phoneLetters.append(["t","u","v"])
phoneLetters.append(["w","x","y","z"])

print(touchToneLetters("666-55 22-666-666-6-33-777"))
input()
