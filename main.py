"""
This program allows you to convert normal text to morse code and to translate
morse to the normal alphabet. 
"""
import argparse #https://docs.python.org/3/library/argparse.html

#Morse code
characters = {"A":".-", "B":"-...", "C":"-.-.", "D":"-..", "E":".",
"F":"..-.", "G":"--.", "H":"....", "I":"..", "J":".---", "K":"-.-", 
"L":".-..", "M":"--", "N":"-.", "O":"---", "P":".--.", "Q":"--.-", "R":".-.", 
"S":"...", "T":"-", "U":"..-", "V":"...-","W":".--", "X":"-..-", "Y":"-.--", "Z":"--..", 
"0":"-----", "1":".----", "2":"..---", "3":"...--", "4":"....-", "5":".....", 
"6":"-....", "7":"--...", "8":"---..", "9":"----."}

#Get dict key
def get_key(val):
    for key, value in characters.items():
         if val == value:
             return key

#Translate to morse code
def trans_to_morse(sentence: str):
	"""
	Converts the given sentence in normal alphabet into morse code.

	Args: 
		sentence(str): sentence to translate.
	Returns:
		morse(str): given sentence converted into morse code.
	"""

	#check if there isn´t any special characters:
	for ch in sentence.replace(" ", ""):
		assert ch.upper() in characters, "You can't enter special characters."

	morse = ""
	#convert into morse:
	for ch in sentence:
		try:
			morse += f"{characters[ch.upper()]} "
		except:
			morse += " "
	return morse 

#Translate into normal alphabet 
def trans_to_alpha(sentence: str):
	"""
	Converts morse code into normal alphabet.

	Args:
		sentence(str): morse code to translate.
	Returns:
		translation(str): morse converted into normal alphabet.
	"""

	#Check if sentence is only morse code:
	for ch in sentence.replace(" ", ""):
		assert ch == "-" or ch == ".", "You can only enter morse code."

	translation = ""
	spaces = [ ] #index of spaces in text

	#get the spaces in the text
	index = 0
	for ch in sentence:
		if ch == " ":
			if sentence[index+1] + sentence[index+2] == "  ":
				spaces.append(int(index+1))
		index += 1
	#change the spaces to "*"
	for i in spaces:
		sentence = sentence[:i] + "*" + sentence[i+1:]
	#convert morse code into normal alphabet
	for ch in sentence.split():
		if ch == "*":
			translation += " "
		else:
			assert ch in list(characters.values()), "You had entered a character that doesn´t exists"
			translation += get_key(ch)

	return translation



#CLI 
parser = argparse.ArgumentParser(description='Convert alphanumeric text into morse code and vice versa.')
parser.add_argument('-trans', '--translate', type=str, 
	choices=['alpha', 'morse'], required=True, help='''
	alpha: translate alphanumeric text into morse code. | 
	morse: translate morse code into alphanumeric.(Separate a letter: " ", Separate a word: "   ")''')

args = parser.parse_args()

if args.translate == "alpha":
	print("Input the alphanumeric text to convert into morse code.")
	sentence = input(">>>")
	print(trans_to_morse(sentence))
elif args.translate == "morse":
	print('Input a morse code sentence to convert into alphanumeric text. (Separate a letter: " ", Separate a word: "   ")')
	sentence = input(">>>")
	print(trans_to_alpha(sentence))





