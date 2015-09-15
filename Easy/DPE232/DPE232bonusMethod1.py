import itertools

words = []

with open('enable1.txt', 'r') as f:
	words = f.readlines()

palindromes = []
	
for a,b in itertools.permutations(words,2):
	a = a.strip()
	b = b.strip()
	mergedWord = ''.join(a + b)
	if mergedWord == mergedWord[::-1]:
		pair = []
		pair.append(a)
		pair.append(b)
		palindromes.append(pair)
		f = open('foundPalindromes.txt','a')
		f.write(a + ' ' + b + '\n')
		f.close()
	else:
		pass
		
print palindromes
	
# for word in range(len(words)):
	# for j in range(words[
	# word = word.strip()
	# if word == word[::-1]:
		# palindromes.append(word)
	# else:
		# pass

# print "These palindromes were found: ", '\n'
# for word in palindromes:
	# print word, '\n'

# string = raw_input("Enter string: ")
# compactString = ''.join(i for i in string if i.isalnum())

# if compactString.lower() == compactString[::-1].lower():
	# print '\n', "Palindrome", '\n'
# else:
	# print '\n' "Not a Palindrome", '\n'