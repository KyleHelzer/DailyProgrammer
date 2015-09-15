#DPE232 Palindromes bonus
from datetime import datetime
startTime = datetime.now()

words = []
dict = {}
foundPalindromes = []
counter = 0

#reads the txt file and puts all words into a list
with open('enable1.txt', 'r') as f:
	words = f.readlines()

#CREATE DICTIONATARY
#removes whitespace and creates a dictionary where the keys are unique two
#letter strings and the value is a list containg all the words from the file
#that have those letters as their last two letters. Thus the words 'foobar'
#and 'car' would be placed in the same list which has the dictionary key 'ar'
for word in words:
	word = word.strip()
	dict.setdefault(word[len(word)-2:], []).append(word)

#takes each word in the file and only compares it to the bin in the dictionary
#with the key 
for word in words:
	word = word.strip()
	value = dict.get(word[:2][::-1]) #reverses the first two letters of word
	if value == None:
		pass
	else:
		for i in dict[word[:2][::-1]]:
			compoundWord = word + i
			if word == i:
				pass
			elif compoundWord == compoundWord[::-1]:
				palindromePair = []
				palindromePair.append(word)
				palindromePair.append(i)
				foundPalindromes.append(palindromePair)
				f = open('foundPalindromes.txt','a')
				f.write(word + ' ' + i + '\n')
				f.close()
				counter += 1
			else:
				pass

#print foundPalindromes
print "DONE!"
print counter, 'palindromes found'
print datetime.now() - startTime
			



