def getInts(s): #convert string into a list of numbers
	return [ord(char)-65 for char in s.upper()]

def vigenere(text, keyphrase):
	text = text.replace(' ', '') #remove spaces
	keyphrase = keyphrase.replace(' ', '')
	textInts = getInts(text)
	keyInts = getInts((keyphrase + text)[:-(len(keyphrase))])
	codedInts = []

	for index, item in enumerate(textInts): #build coded int list
		codedInts.append((item+keyInts[index])%26)

	codedString = ''.join([chr(num+65) for num in codedInts])
	return codedString

#test
text = "TAKEACOPYOFYOURPOLICYTONORMAWILCOXONTHETHIRDFLOOR"
keyphrase = "QUARK"
print ("\nOriginal text: %s\nKeyphrase:     %s" % (text, keyphrase))
encodedString = vigenere(text, keyphrase)
print ("Encoded text:  %s\n" % encodedString)
