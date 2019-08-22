# def toLowerCase(self, str: str) -> str:
	
	# python in built fn
	# str = str.lower()

str = "AHelloZ"
strlst = list(str)
result = ""

for i in range(len(strlst)):
	# print (strlst[i])

	if ((ord(strlst[i])>=65) and (ord(strlst[i])<=90)):
		strlst[i] = chr(ord(strlst[i])+32)
	
	result = result + strlst[i]


print (result)



